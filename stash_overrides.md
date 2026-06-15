# Stash 简化导入

最短路径：

1. 在 Stash 导入 `stash.yaml`。
2. 打开 `http://script.hub`，确认 Script Hub 页面能打开。
3. 回到这里，只点“最少先装”里的两个 `Install`。

`stash.yaml` 是主配置；本文件只负责安装 Loon 插件转换后的 Stash 覆写。
App 去广告和工具插件都折叠在下面，需要哪个再展开安装。
如果某个安装链接没有反应，通常是插件源站临时不可访问，稍后重试即可。

## 最少先装

| 插件 | 安装 | 备注 |
| --- | --- | --- |
| Block_HTTPDNS | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FBlock_HTTPDNS.lpx%2F_end_%2FBlock_HTTPDNS.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) |  |
| BlockAdvertisers | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FBlockAdvertisers.lpx%2F_end_%2FBlockAdvertisers.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) |  |

<details>
<summary>App 去广告，可选展开</summary>

| 插件 | 安装 | 备注 |
| --- | --- | --- |
| QQMusic_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FQQMusic_remove_ads.lpx%2F_end_%2FQQMusic_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| Spotify_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FSpotify_remove_ads.lpx%2F_end_%2FSpotify_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| YouTube_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FYouTube_remove_ads.lpx%2F_end_%2FYouTube_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| Tieba_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FTieba_remove_ads.lpx%2F_end_%2FTieba_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| Bilibili_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FBilibili_remove_ads.lpx%2F_end_%2FBilibili_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| DiDi_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FDiDi_remove_ads.lpx%2F_end_%2FDiDi_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| Amap_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FAmap_remove_ads.lpx%2F_end_%2FAmap_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| JD_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FJD_remove_ads.lpx%2F_end_%2FJD_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| CoolApk_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FCoolApk_remove_ads.lpx%2F_end_%2FCoolApk_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| PinDuoDuo_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FPinDuoDuo_remove_ads.lpx%2F_end_%2FPinDuoDuo_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| smzdm_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2Fsmzdm_remove_ads.lpx%2F_end_%2Fsmzdm_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| Taobao_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FTaobao_remove_ads.lpx%2F_end_%2FTaobao_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| Tencent_Video_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FTencent_Video_remove_ads.lpx%2F_end_%2FTencent_Video_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| Weibo_intl_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FWeibo_intl_remove_ads.lpx%2F_end_%2FWeibo_intl_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| Weibo_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FWeibo_remove_ads.lpx%2F_end_%2FWeibo_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| NeteaseCloudMusic_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FNeteaseCloudMusic_remove_ads.lpx%2F_end_%2FNeteaseCloudMusic_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| Weixin_Official_Accounts_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FWeixin_Official_Accounts_remove_ads.lpx%2F_end_%2FWeixin_Official_Accounts_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| FleaMarket_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FFleaMarket_remove_ads.lpx%2F_end_%2FFleaMarket_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| RedPaper_remove_ads | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FRedPaper_remove_ads.lpx%2F_end_%2FRedPaper_remove_ads.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |

</details>

<details>
<summary>工具和解锁，可选展开</summary>

| 插件 | 安装 | 备注 |
| --- | --- | --- |
| QuickSearch | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FQuickSearch.lpx%2F_end_%2FQuickSearch.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) |  |
| Prevent_DNS_Leaks | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FPrevent_DNS_Leaks.lpx%2F_end_%2FPrevent_DNS_Leaks.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | 节点选择 |
| Node_detection_tool | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FNode_detection_tool.lpx%2F_end_%2FNode_detection_tool.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) |  |
| BoxJs | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FBoxJs.lpx%2F_end_%2FBoxJs.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | 节点选择 |
| Sub-Store | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FSub-Store.lpx%2F_end_%2FSub-Store.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | 节点选择 |
| Script-Hub | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FScript-Hub.lpx%2F_end_%2FScript-Hub.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | 节点选择 |
| TestFlightRegionUnlock | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FTestFlightRegionUnlock.lpx%2F_end_%2FTestFlightRegionUnlock.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| QQ_Redirect | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FQQ_Redirect.lpx%2F_end_%2FQQ_Redirect.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |
| Weixin_external_links_unlock | [Install](stash://install-override?url=http%3A%2F%2Fscript.hub%2Ffile%2F_start_%2Fhttps%3A%2F%2Fkelee.one%2FTool%2FLoon%2FLpx%2FWeixin_external_links_unlock.lpx%2F_end_%2FWeixin_external_links_unlock.stoverride%3Ftype%3Dloon-plugin%26target%3Dstash-stoverride%26synMitm%3Dtrue) | DIRECT |

</details>
