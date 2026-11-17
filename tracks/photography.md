# 摄影（深度版）

> 这个方向的开源工具不解决"怎么拍"，解决的是**拍完之后那 80% 的脏活**：备份、选片、建库、检索、色彩一致性。

## 一、主线三件套

| 环节 | 选它 | 为什么 |
|---|---|---|
| RAW 处理 | **darktable** | 开源里最完整的暗房，非破坏性编辑 |
| 元数据 | **ExifTool** | 一切元数据的终极工具，脚本化基础 |
| 资产管理 | **PhotoPrism**（或 Immich） | 人脸、地点、AI 标签，照片能被"找得到" |

## 二、完整工作流

```
① 拍摄        相机/联机（gPhoto2、darktable tethering）
      ↓
② 导入备份    Rapid Photo Downloader 统一命名 → rclone 云备份 + restic 异地
      ↓
③ 建库检索    PhotoPrism / digiKam：人脸、地点、关键词、相似图
      ↓
④ 选片        darktable 灯箱视图，星级 + 色标，一次过
      ↓
⑤ 显影调色    darktable：场景参照工作流 + 遮罩 + 色彩校准
      ↓
⑥ 精修        GIMP / Krita（像素级修补、合成、文字）
      ↓
⑦ 交付        ImageMagick/libvips 批量出多尺寸，ExifTool 清元数据
```

## 三、RAW 处理与显影

| 项目 | 定位 | 适合谁 |
|---|---|---|
| [darktable-org/darktable](https://github.com/darktable-org/darktable) | 非破坏性 RAW 工作台 | 想要完整流程 + 可脚本化的人 |
| [RawTherapee/RawTherapee](https://github.com/RawTherapee/RawTherapee) | 另一个 RAW 引擎，降噪与细节强 | 追求画质极限的人 |
| [LibRaw/LibRaw](https://github.com/LibRaw/LibRaw) | RAW 解码库 | 自己写批处理脚本 |
| [Beep6581/RawTherapee](https://github.com/Beep6581/RawTherapee) | RawTherapee 主仓（镜像） | 同上 |

**darktable 的三个关键概念**（新手最容易卡住的地方）：

| 概念 | 说明 |
|---|---|
| 场景参照（scene-referred） | 先用 `filmic rgb` 把动态范围压下来，再谈风格 |
| 模块顺序 | 显示顺序 ≠ 处理顺序，遮罩与色彩模块要注意位置 |
| 遮罩（mask） | 局部调整全靠它：画笔、渐变、路径、参数化 |

## 四、色彩管理（专业与否的分水岭）

| 项目 | 用途 | 说明 |
|---|---|---|
| [OpenColorIO/OpenColorIO](https://github.com/AcademySoftwareFoundation/OpenColorIO) | 统一色彩管线 | ACES 工作流的核心 |
| [AcademySoftwareFoundation/OpenColorIO-Config-ACES](https://github.com/AcademySoftwareFoundation/OpenColorIO-Config-ACES) | ACES 配置 | 影视级色彩一致性 |
| [mm2/Little-CMS](https://github.com/mm2/Little-CMS) | ICC 色彩管理引擎 | 显示器/打印机特性文件 |
| [eoyilmaz/displaycal-py3](https://github.com/eoyilmaz/displaycal-py3) | 显示器校准（DisplayCAL 新版） | 校色仪配套 |
| [ArgyllCMS 官网](https://www.argyllcms.com/) | 色彩测量底层工具 | 配合校色仪使用 |

> 一句话：**没有校准过的显示器，调色是在猜。** 先花 500 块买个校色仪 + DisplayCAL，比换镜头更能提升成片一致性。

## 五、镜头、畸变与合成

| 项目 | 用途 |
|---|---|
| [lensfun/lensfun](https://github.com/lensfun/lensfun) | 镜头畸变/暗角/色差数据库，darktable 自动调用 |
| [Hugin 官网](https://hugin.sourceforge.io/) | 全景拼接、透视校正 |
| [LuminanceHDR/LuminanceHDR](https://github.com/LuminanceHDR/LuminanceHDR) | HDR 合成与色调映射 |
| [aurelienpierreeng/ansel](https://github.com/aurelienpierreeng/ansel) | darktable 作者的分支，更专注摄影 |

## 六、素材管理与备份

| 项目 | 用途 | 关键点 |
|---|---|---|
| [photoprism/photoprism](https://github.com/photoprism/photoprism) | 照片库 + AI 标签 + 人脸 | 支持 RAW，适合工作室建库 |
| [immich-app/immich](https://github.com/immich-app/immich) | 手机自动备份 + 相册 | 移动端体验最好 |
| [KDE/digikam](https://github.com/KDE/digikam) | 本地照片管理（KDE） | 元数据写入文件，不锁库 |
| [exiftool/exiftool](https://github.com/exiftool/exiftool) | 元数据读写 | 改名、加版权、清 GPS |
| [rclone/rclone](https://github.com/rclone/rclone) | 云盘同步 | 支持几乎所有对象存储 |
| [restic/restic](https://github.com/restic/restic) | 加密增量备份 | 异地备份 + 版本回滚 |
| [syncthing/syncthing](https://github.com/syncthing/syncthing) | 点对点同步 | 现场拍摄时电脑↔NAS |
| [damonlynch/rapid-photo-downloader](https://github.com/damonlynch/rapid-photo-downloader) | 导入与统一命名 | 按日期/机身/项目自动归档 |
| [gphoto/gphoto2](https://github.com/gphoto/gphoto2) | 联机拍摄与相机控制 | 脚本化延时、包围曝光 |

## 七、常见场景配方

| 场景 | 推荐组合 |
|---|---|
| 婚礼/活动跟拍 | Rapid Photo Downloader 导入 → darktable 批量选片 → 统一预设 → 批量导出 |
| 商业产品图 | 联机拍摄（gPhoto2）→ darktable 色彩校准 → GIMP 修瑕疵 → 批量多尺寸 |
| 风光 | 包围曝光 → LuminanceHDR 合成 → darktable 局部遮罩 |
| 全景 | Hugin 拼接 → 透视校正 → darktable 统一色调 |
| 素材库长期运营 | PhotoPrism 建库 → 人脸/地点标签 → 按项目导出 |

## 八、闭源替代关系

| 商业方案 | 开源对应 | 差距 |
|---|---|---|
| Lightroom Classic | darktable | 图库与云同步弱，显影质量接近甚至更专业 |
| Capture One | darktable / RawTherapee | 联机拍摄与色彩编辑体验有差距 |
| Photo Mechanic | Rapid Photo Downloader + ExifTool | 选片速度略慢 |
| 百度网盘/坚果云 | rclone + restic + 自建 NAS | 需要自己维护硬件 |

## 九、三条经验

1. **先建备份，再谈调色。** 一次硬盘故障能抹掉三年作品，这个顺序不能反。
2. **色彩管理是复利。** 校准一次显示器，之后每一张照片、每一次客户交付都受益。
3. **别用文件夹管理照片。** 用元数据（人脸、地点、关键词、星级）管理，文件夹只是物理存放。
