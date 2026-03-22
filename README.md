# ConvertRules

mihomo 规则自动转换为 QuantumultX / Loon 可用的规则集。

## 文件说明

| 文件 | 说明 |
|------|------|
| `mihomo_template.yaml` | mihomo 配置模板（无订阅链接） |
| `QuantumultX_template.conf` | QX 配置模板  |
| `Loon_template.conf` | Loon 配置模板  |

## 工作原理

1. GitHub Actions 每天自动运行 `scripts/convert-rules.py`
2. 从 [MetaCubeX/meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat) 下载 `.list` 规则
3. 转换为 `DOMAIN-SUFFIX` / `IP-CIDR` 格式（QX/Loon 通用）
4. 提交到 main 分支的 `rules/` 目录

## 使用方法

### 1. 初始化仓库

```bash
git init
git add .
git commit -m "init"
git remote add origin git@github.com:YOUR_USERNAME/ConvertRules.git
git push -u origin main
```

### 2. 替换 OWNER 占位符

在 `QuantumultX_template.conf` 和 `Loon_template.conf` 中，将所有 `OWNER` 替换为你的 GitHub 用户名。

### 3. 触发 Action

推送到 main 后，GitHub Actions 会自动运行并生成 `rules` 分支。也可以在 Actions 页面手动触发。

### 4. CDN 地址

规则集通过 jsdelivr CDN 访问：
```
https://cdn.jsdelivr.net/gh/YOUR_USERNAME/ConvertRules@main/rules/规则名.list
```

## 规则对应关系

| mihomo rule-provider | MetaCubeX geosite/geoip | 策略 |
|---------------------|------------------------|------|
| private | geosite/private | 直连 |
| cn_domain | geosite/cn | 直连 |
| apple_domain | geosite/apple-cn | Apple |
| ai_domain | geosite/category-ai-chat-!cn | AI |
| github_domain | geosite/github | GitHub |
| docker_domain | geosite/docker | GitHub |
| youtube_domain | geosite/youtube | YouTube |
| google_domain | geosite/google | Google |
| microsoft_domain | geosite/microsoft | Microsoft |
| tiktok_domain | geosite/tiktok | TikTok |
| telegram_domain | geosite/telegram | Telegram |
| netflix_domain | geosite/netflix | Netflix |
| paypal_domain | geosite/paypal | PayPal |
| speedtest_domain | geosite/ookla-speedtest | Speedtest |
| porn_domain | geosite/category-porn | Pornhub |
| not_cn_domain | geosite/geolocation-!cn | 节点选择 |
| google_ip | geoip/google | Google |
| netflix_ip | geoip/netflix | Netflix |
| telegram_ip | geoip/telegram | Telegram |
| cn_ip | geoip/cn | 直连 |
