#!/usr/bin/env python3
"""
Generate Script Hub conversion links for Loon plugins.

The output is a Markdown checklist. It does not fetch plugin contents; Stash +
Script Hub will do the actual conversion inside the client.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from urllib.parse import quote


PLUGIN_LINE = re.compile(r"^(https?://[^,\s]+)(?:,\s*(.*))?$")
CORE_PLUGINS = {"Block_HTTPDNS", "BlockAdvertisers"}


def parse_plugins(path: Path) -> list[tuple[str, str | None]]:
    in_plugin = False
    plugins: list[tuple[str, str | None]] = []

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        if line.startswith("[") and line.endswith("]"):
            in_plugin = line.lower() == "[plugin]"
            continue

        if not in_plugin:
            continue

        match = PLUGIN_LINE.match(line)
        if not match:
            continue

        url, options = match.groups()
        if "enabled=false" in (options or "").lower():
            continue

        plugins.append((url, options))

    return plugins


def plugin_name(url: str) -> str:
    name = url.rstrip("/").rsplit("/", 1)[-1]
    name = re.sub(r"\.lpx$", "", name, flags=re.IGNORECASE)
    return name or "loon-plugin"


def build_convert_url(url: str, name: str) -> str:
    filename = f"{name}.stoverride"
    return (
        f"http://script.hub/file/_start_/{url}/_end_/{filename}"
        "?type=loon-plugin&target=stash-stoverride&synMitm=true"
    )


def plugin_row(url: str, options: str | None) -> tuple[str, str, str, str]:
    name = plugin_name(url)
    convert_url = build_convert_url(url, name)
    install_url = "stash://install-override?url=" + quote(convert_url, safe="")
    note = ""
    if options:
        policy_match = re.search(r"(?:^|,\s*)policy\s*=\s*([^,]+)", options)
        if policy_match:
            note = policy_match.group(1).strip()

    return name, install_url, convert_url, note


def append_plugins(
    lines: list[str],
    title: str,
    rows: list[tuple[str, str, str, str]],
    *,
    collapsed: bool = False,
) -> None:
    if not rows:
        return

    if collapsed:
        lines.extend(["<details>", f"<summary>{title}</summary>", ""])
    else:
        lines.extend([f"## {title}", ""])

    for name, install_url, convert_url, note in rows:
        lines.extend(
            [
                f"### {name}",
                "",
                f"- 外部打开：[Install]({install_url})",
                f"- Stash 里点“从 URL 安装”时粘贴：`{convert_url}`",
            ]
        )
        if note:
            lines.append(f"- 策略：`{note}`")
        lines.append("")

    lines.append("")
    if collapsed:
        lines.extend(["</details>", ""])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("loon_conf", nargs="?", default="Loon_template.conf")
    parser.add_argument("-o", "--output", default="stash_overrides.md")
    args = parser.parse_args()

    plugins = parse_plugins(Path(args.loon_conf))
    core: list[tuple[str, str, str]] = []
    ads: list[tuple[str, str, str]] = []
    optional: list[tuple[str, str, str]] = []

    for url, options in plugins:
        row = plugin_row(url, options)
        name = row[0]
        if name in CORE_PLUGINS:
            core.append(row)
        elif "remove_ads" in name.lower() or "redpaper" in name.lower():
            ads.append(row)
        else:
            optional.append(row)

    lines = [
        "# Stash 简化导入",
        "",
        "最短路径：",
        "",
        "1. 在 Stash 导入 `stash.yaml`。",
        "2. 打开 `http://script.hub`，确认 Script Hub 页面能打开。",
        "3. 回到这里，先装“最少先装”里的两个插件。",
        "",
        "`stash.yaml` 是主配置；本文件只负责安装 Loon 插件转换后的 Stash 覆写。",
        "如果你已经在 Stash 的覆写页面，点“从 URL 安装”，复制每个插件下面的 `http://script.hub/...` 地址粘贴进去。",
        "App 去广告和工具插件都折叠在下面，需要哪个再展开安装。",
        "如果某个安装链接没有反应，通常是插件源站临时不可访问，稍后重试即可。",
        "",
    ]

    append_plugins(lines, "最少先装", core)
    append_plugins(lines, "App 去广告，可选展开", ads, collapsed=True)
    append_plugins(lines, "工具和解锁，可选展开", optional, collapsed=True)

    Path(args.output).write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.output} ({len(plugins)} plugins)")


if __name__ == "__main__":
    main()
