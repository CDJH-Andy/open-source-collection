# 自托管与生活

> 自托管的核心不是省钱，是**数据在你自己手里**。这一类的共同门槛是一台能跑 Docker 的机器（NAS、旧笔记本、云主机都行）。

## 先看结论：按需求挑

| 我想要 | 装这个 | 内存起步 |
|---|---|---|
| 手机照片自动备份、替代 iCloud | **Immich** | 4 GB |
| 私有网盘、多端同步 | **Nextcloud** 或 **Seafile** | 2 GB |
| 影视库，海报墙刮削 | **Jellyfin** | 2 GB |
| 密码管理 | **Vaultwarden** | 256 MB |
| 家庭自动化、智能家居中枢 | **Home Assistant** | 2 GB |
| 文档扫描归档、全文检索 | **Paperless-ngx** | 2 GB |
| 服务监控与告警 | **Uptime Kuma** | 256 MB |
| 稍后读、书签收集 | **memos** 或 **Hoarder** | 512 MB |

---

## 家庭与媒体

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [home-assistant/core](https://github.com/home-assistant/core) | 开源智能家居中枢，集成上千种设备 | 米家、HomeKit 都能接 |
| [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin) | 完全自由开源的媒体服务器 | 替代 Plex/Emby，无收费墙 |
| [immich-app/immich](https://github.com/immich-app/immich) | 自建 Google Photos，人脸识别、地图、相册时光 | 目前最接近成品的自建相册 |
| [blakeblackshear/frigate](https://github.com/blakeblackshear/frigate) | 本地 NVR，摄像头目标检测 | 需要一定算力 |
| [syncthing/syncthing](https://github.com/syncthing/syncthing) | 点对点文件同步，不经过任何服务器 | 两台设备直连 |

## 效率与知识

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [nextcloud/server](https://github.com/nextcloud/server) | 私有云盘 + 协作套件 | 插件多，略重 |
| [haiwen/seafile](https://github.com/haiwen/seafile) | 轻量私有网盘，同步稳定 | 国内团队作品，中文友好 |
| [laurent22/joplin](https://github.com/laurent22/joplin) | 开源笔记，端到端加密同步 | 支持 Markdown |
| [usememos/memos](https://github.com/usememos/memos) | 极简碎片笔记，一条命令部署 | 「自建 flomo」 |
| [paperless-ngx/paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | 纸质文档扫描 + OCR + 标签归档 | 合同、发票、证件神器 |
| [wallabag/wallabag](https://github.com/wallabag/wallabag) | 稍后读服务，正文提取 | 替代 Pocket |
| [hoarder-app/hoarder](https://github.com/hoarder-app/hoarder) | 书签 + 截图 + AI 自动打标签 | 信息囤积者的解药 |

## 运维与協作

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [louislam/uptime-kuma](https://github.com/louislam/uptime-kuma) | 好看的服务可用性监控 | 部署 5 分钟 |
| [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden) | Bitwarden 的轻量服务端实现 | 手机电脑浏览器全通 |
| [gchq/CyberChef](https://github.com/gchq/CyberChef) | 网页版数据处理/编解码瑞士军刀 | 查编码、做取证分析 |
| [mattermost/mattermost](https://github.com/mattermost/mattermost) | 自建团队沟通平台 | 替代 Slack |
| [element-hq/element-web](https://github.com/element-hq/element-web) | Matrix 协议的客户端 | 去中心化聊天 |

---

## 上手建议

1. **先备份，再自托管。** 自托管意味着「数据丢了是你的责任」。至少做到：重要数据异地一份，配置有版本管理。
2. **别一次装十个服务。** 从 Immich 或 Vaultwarden 开始，跑稳一个月再扩。
3. **反向代理用 Traefik 或 Nginx Proxy Manager**，别直接暴露端口到公网。
4. **注意许可证。** 有些项目是 fair-code 或 BSL，商用前要看清楚条款。
