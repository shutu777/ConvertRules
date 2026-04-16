#!/usr/bin/env python3
"""
从 MetaCubeX/meta-rules-dat 下载 .list 规则文件，
转换为 QuantumultX 和 Loon 可用的规则集格式。
"""

import os
import sys
import urllib.request
import urllib.error

# MetaCubeX CDN 基础 URL
BASE_DOMAIN = "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite"
BASE_IP = "https://cdn.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geoip"

# 域名规则映射: mihomo rule-provider name -> MetaCubeX geosite name
DOMAIN_RULES = {
    "private": "private",
    "cn_domain": "cn",
    "apple_domain": "apple-cn",
    "github_domain": "github",
    "youtube_domain": "youtube",
    "google_domain": "google",
    "telegram_domain": "telegram",
    "netflix_domain": "netflix",
    "ai_domain": "category-ai-chat-!cn",
    "microsoft_domain": "microsoft",
    "tiktok_domain": "tiktok",
    "paypal_domain": "paypal",
    "speedtest_domain": "ookla-speedtest",
    "games_domain": "category-games",
    "accelerator_cn_domain": "category-game-accelerator-cn",
    "porn_domain": "category-porn",
    "docker_domain": "docker",
    "not_cn_domain": "geolocation-!cn",
    "pt_cn_domain": "category-pt",
    "binance_domain": "binance-pt",
}

# IP 规则映射: mihomo rule-provider name -> MetaCubeX geoip name
IP_RULES = {
    "private_ip": "private",
    "cn_ip": "cn",
    "google_ip": "google",
    "netflix_ip": "netflix",
    "telegram_ip": "telegram",
}

# YAML 格式规则映射: mihomo rule-provider name -> 自定义 URL
YAML_RULES = {
    "seedbox_domain": "https://nini618.oss-cn-hangzhou.aliyuncs.com/Clash/SeedBox.yaml",
    "manual_direct_domain": "https://nini618.oss-cn-hangzhou.aliyuncs.com/Clash/ManualDirect.yaml",
}


def download(url, retries=3):
    """下载文件内容，支持重试"""
    import ssl
    ctx = ssl.create_default_context()
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60, context=ctx) as resp:
                return resp.read().decode("utf-8")
        except Exception as e:
            print(f"  [WARN] 第{attempt}次下载失败: {e}")
            if attempt == retries:
                print(f"  [ERROR] 最终下载失败: {url}")
                return None
            import time
            time.sleep(2)


def convert_domain_line(line):
    """
    转换单行域名规则:
    +.domain.com -> DOMAIN-SUFFIX,domain.com
    domain.com   -> DOMAIN,domain.com
    """
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    if line.startswith("+."):
        return f"DOMAIN-SUFFIX,{line[2:]}"
    else:
        return f"DOMAIN,{line}"


def convert_ip_line(line):
    """
    转换单行 IP 规则:
    x.x.x.x/xx  -> IP-CIDR,x.x.x.x/xx,no-resolve
    xxxx::/xx    -> IP-CIDR6,xxxx::/xx,no-resolve
    """
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    if ":" in line:
        return f"IP-CIDR6,{line},no-resolve"
    else:
        return f"IP-CIDR,{line},no-resolve"


def convert_yaml_rules(content):
    """
    转换 YAML 格式规则:
    解析 Clash YAML 格式的 domain 和 ip 规则，转换为 QuantumultX 格式
    """
    import re
    lines = []

    # 提取 domain 规则
    domain_pattern = re.compile(r"^\s*-\s+['\"]?([\w\.\-\*]+)['\"]?$")
    # 提取 ip-cidr 规则
    ip_pattern = re.compile(r"^\s*-\s+['\"]?([\d\./:]+)['\"]?,.*no-resolve")

    for line in content.splitlines():
        # 尝试匹配 domain 规则
        domain_match = domain_pattern.match(line)
        if domain_match:
            domain = domain_match.group(1)
            if domain.startswith("+."):
                lines.append(f"DOMAIN-SUFFIX,{domain[2:]}")
            elif domain.startswith("."):
                lines.append(f"DOMAIN-SUFFIX,{domain[1:]}")
            else:
                lines.append(f"DOMAIN,{domain}")
            continue

        # 尝试匹配 IP 规则
        ip_match = ip_pattern.match(line)
        if ip_match:
            ip = ip_match.group(1)
            if ":" in ip:
                lines.append(f"IP-CIDR6,{ip},no-resolve")
            else:
                lines.append(f"IP-CIDR,{ip},no-resolve")

    return lines


def process_rules(output_dir):
    """处理所有规则"""
    os.makedirs(output_dir, exist_ok=True)

    # 处理域名规则
    print("=== 处理域名规则 ===")
    for name, geosite in DOMAIN_RULES.items():
        url = f"{BASE_DOMAIN}/{geosite}.list"
        print(f"  下载: {name} <- {geosite}.list")
        content = download(url)
        if content is None:
            continue

        lines = []
        for raw_line in content.splitlines():
            converted = convert_domain_line(raw_line)
            if converted:
                lines.append(converted)

        out_path = os.path.join(output_dir, f"{name}.list")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"  写入: {out_path} ({len(lines)} 条规则)")

    # 处理 IP 规则
    print("\n=== 处理 IP 规则 ===")
    for name, geoip in IP_RULES.items():
        url = f"{BASE_IP}/{geoip}.list"
        print(f"  下载: {name} <- {geoip}.list")
        content = download(url)
        if content is None:
            continue

        lines = []
        for raw_line in content.splitlines():
            converted = convert_ip_line(raw_line)
            if converted:
                lines.append(converted)

        out_path = os.path.join(output_dir, f"{name}.list")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"  写入: {out_path} ({len(lines)} 条规则)")

    # 处理 YAML 格式规则
    print("\n=== 处理 YAML 格式规则 ===")
    for name, url in YAML_RULES.items():
        print(f"  下载: {name} <- {url}")
        content = download(url)
        if content is None:
            continue

        lines = convert_yaml_rules(content)

        out_path = os.path.join(output_dir, f"{name}.list")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"  写入: {out_path} ({len(lines)} 条规则)")


if __name__ == "__main__":
    output_dir = sys.argv[1] if len(sys.argv) > 1 else "rules"
    process_rules(output_dir)
    print("\n✅ 规则转换完成!")
