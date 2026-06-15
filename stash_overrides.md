# Stash 简化导入

最短路径：

1. 在 Stash 导入 `stash.yaml`。
2. 打开 `http://script.hub`，确认 Script Hub 页面能打开。
3. 回到这里，先装“最少先装”里的两个插件。

`stash.yaml` 是主配置；本文件只负责安装 Loon 插件转换后的 Stash 覆写。
如果你已经在 Stash 的覆写页面，点“从 URL 安装”，复制每个插件下面的 `http://script.hub/...` 地址粘贴进去。
App 去广告和工具插件都折叠在下面，需要哪个再展开安装。
如果某个安装链接没有反应，通常是插件源站临时不可访问，稍后重试即可。

## 最少先装

### Block_HTTPDNS

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FBlock_HTTPDNS.lpx%2F_end_%2FBlock_HTTPDNS.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Block_HTTPDNS.lpx/_end_/Block_HTTPDNS.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`

### BlockAdvertisers

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FBlockAdvertisers.lpx%2F_end_%2FBlockAdvertisers.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/BlockAdvertisers.lpx/_end_/BlockAdvertisers.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`


<details>
<summary>App 去广告，可选展开</summary>

### QQMusic_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FQQMusic_remove_ads.lpx%2F_end_%2FQQMusic_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/QQMusic_remove_ads.lpx/_end_/QQMusic_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### Spotify_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FSpotify_remove_ads.lpx%2F_end_%2FSpotify_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Spotify_remove_ads.lpx/_end_/Spotify_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### YouTube_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FYouTube_remove_ads.lpx%2F_end_%2FYouTube_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/YouTube_remove_ads.lpx/_end_/YouTube_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### Tieba_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FTieba_remove_ads.lpx%2F_end_%2FTieba_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Tieba_remove_ads.lpx/_end_/Tieba_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### Bilibili_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FBilibili_remove_ads.lpx%2F_end_%2FBilibili_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Bilibili_remove_ads.lpx/_end_/Bilibili_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### DiDi_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FDiDi_remove_ads.lpx%2F_end_%2FDiDi_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/DiDi_remove_ads.lpx/_end_/DiDi_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### Amap_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FAmap_remove_ads.lpx%2F_end_%2FAmap_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Amap_remove_ads.lpx/_end_/Amap_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### JD_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FJD_remove_ads.lpx%2F_end_%2FJD_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/JD_remove_ads.lpx/_end_/JD_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### CoolApk_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FCoolApk_remove_ads.lpx%2F_end_%2FCoolApk_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/CoolApk_remove_ads.lpx/_end_/CoolApk_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### PinDuoDuo_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FPinDuoDuo_remove_ads.lpx%2F_end_%2FPinDuoDuo_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/PinDuoDuo_remove_ads.lpx/_end_/PinDuoDuo_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### smzdm_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2Fsmzdm_remove_ads.lpx%2F_end_%2Fsmzdm_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/smzdm_remove_ads.lpx/_end_/smzdm_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### Taobao_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FTaobao_remove_ads.lpx%2F_end_%2FTaobao_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Taobao_remove_ads.lpx/_end_/Taobao_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### Tencent_Video_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FTencent_Video_remove_ads.lpx%2F_end_%2FTencent_Video_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Tencent_Video_remove_ads.lpx/_end_/Tencent_Video_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### Weibo_intl_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FWeibo_intl_remove_ads.lpx%2F_end_%2FWeibo_intl_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Weibo_intl_remove_ads.lpx/_end_/Weibo_intl_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### Weibo_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FWeibo_remove_ads.lpx%2F_end_%2FWeibo_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Weibo_remove_ads.lpx/_end_/Weibo_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### NeteaseCloudMusic_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FNeteaseCloudMusic_remove_ads.lpx%2F_end_%2FNeteaseCloudMusic_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/NeteaseCloudMusic_remove_ads.lpx/_end_/NeteaseCloudMusic_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### Weixin_Official_Accounts_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FWeixin_Official_Accounts_remove_ads.lpx%2F_end_%2FWeixin_Official_Accounts_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Weixin_Official_Accounts_remove_ads.lpx/_end_/Weixin_Official_Accounts_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### FleaMarket_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FFleaMarket_remove_ads.lpx%2F_end_%2FFleaMarket_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/FleaMarket_remove_ads.lpx/_end_/FleaMarket_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### RedPaper_remove_ads

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FRedPaper_remove_ads.lpx%2F_end_%2FRedPaper_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/RedPaper_remove_ads.lpx/_end_/RedPaper_remove_ads.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`


</details>

<details>
<summary>工具和解锁，可选展开</summary>

### QuickSearch

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FQuickSearch.lpx%2F_end_%2FQuickSearch.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/QuickSearch.lpx/_end_/QuickSearch.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`

### Prevent_DNS_Leaks

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FPrevent_DNS_Leaks.lpx%2F_end_%2FPrevent_DNS_Leaks.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Prevent_DNS_Leaks.lpx/_end_/Prevent_DNS_Leaks.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`节点选择`

### Node_detection_tool

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FNode_detection_tool.lpx%2F_end_%2FNode_detection_tool.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Node_detection_tool.lpx/_end_/Node_detection_tool.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`

### BoxJs

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FBoxJs.lpx%2F_end_%2FBoxJs.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/BoxJs.lpx/_end_/BoxJs.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`节点选择`

### Sub-Store

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FSub-Store.lpx%2F_end_%2FSub-Store.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Sub-Store.lpx/_end_/Sub-Store.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`节点选择`

### Script-Hub

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FScript-Hub.lpx%2F_end_%2FScript-Hub.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Script-Hub.lpx/_end_/Script-Hub.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`节点选择`

### TestFlightRegionUnlock

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FTestFlightRegionUnlock.lpx%2F_end_%2FTestFlightRegionUnlock.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/TestFlightRegionUnlock.lpx/_end_/TestFlightRegionUnlock.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### QQ_Redirect

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FQQ_Redirect.lpx%2F_end_%2FQQ_Redirect.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/QQ_Redirect.lpx/_end_/QQ_Redirect.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`

### Weixin_external_links_unlock

- 外部打开：[Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FWeixin_external_links_unlock.lpx%2F_end_%2FWeixin_external_links_unlock.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue)
- Stash 里点“从 URL 安装”时粘贴：`http://script.hub/file/_start_/https://kelee.one/Tool/Loon/Lpx/Weixin_external_links_unlock.lpx/_end_/Weixin_external_links_unlock.stoverride?type=loon-plugin&target=stash-stoverride&synMitm=true`
- 策略：`DIRECT`


</details>
