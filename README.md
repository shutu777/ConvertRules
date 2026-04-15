# ConvertRules

mihomo 规则自动转换为 QuantumultX / Loon / Surge 可用的规则集。

## 文件说明

| 文件 | 说明 |
|------|------|
| `mihomo_template.yaml` | mihomo 配置模板（无订阅链接） |
| `QuantumultX_template.conf` | QX 配置模板  |
| `Loon_template.conf` | Loon 配置模板  |
| `surge_template.conf` | Surge 配置模板  |

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

在 `QuantumultX_template.conf`、`Loon_template.conf` 和 `surge_template.conf` 中，将所有 `OWNER` 替换为你的 GitHub 用户名。

### 3. 触发 Action

推送到 main 后，GitHub Actions 会自动运行并生成 `rules` 分支。也可以在 Actions 页面手动触发。

### 4. CDN 地址

规则集通过 jsdelivr CDN 访问：
```
https://cdn.jsdelivr.net/gh/YOUR_USERNAME/ConvertRules@main/rules/规则名.list
```

### 5. Surge 使用方法

1. 下载 `surge_template.conf` 文件
2. 将文件中的 `OWNER` 替换为你的 GitHub 用户名
3. 在 `[Proxy]` 部分添加你的代理节点
4. 根据需要调整 `[Proxy Group]` 中的节点分组
5. 将配置文件导入 Surge 即可使用

Surge 配置集成了 Loyalsoldier/surge-rules 项目的规则集，同时保留了自定义规则集，提供更全面的分流策略。

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

## Surge 配置说明

Surge 配置文件参考了 [Loyalsoldier/surge-rules](https://github.com/Loyalsoldier/surge-rules) 项目，集成了以下规则集：

### Loyalsoldier/surge-rules 规则集
- `private.txt` - 私有网络专用域名列表
- `apple.txt` - Apple 在中国大陆可直连的域名列表
- `google.txt` - Google 在中国大陆可直连的域名列表
- `tld-not-cn.txt` - 非中国大陆使用的顶级域名列表
- `cncidr.txt` - 中国大陆 IP 地址列表
- `telegramcidr.txt` - Telegram 使用的 IP 地址列表

### 自定义规则集
- `cn_domain.list` - 中国大陆域名列表
- `ai_domain.list` - AI 相关域名列表
- `github_domain.list` - GitHub 域名列表
- `youtube_domain.list` - YouTube 域名列表
- `microsoft_domain.list` - Microsoft 域名列表
- `tiktok_domain.list` - TikTok 域名列表
- `telegram_domain.list` - Telegram 域名列表
- `netflix_domain.list` - Netflix 域名列表
- `paypal_domain.list` - PayPal 域名列表
- `speedtest_domain.list` - Speedtest 域名列表
- `porn_domain.list` - 成人内容域名列表
- `docker_domain.list` - Docker 域名列表
- `games_domain.list` - 游戏域名列表
- `accelerator_cn_domain.list` - 游戏加速器域名列表
- `google_ip.list` - Google IP 地址列表
- `netflix_ip.list` - Netflix IP 地址列表
- `telegram_ip.list` - Telegram IP 地址列表
- `private.list` - 私有网络域名列表
