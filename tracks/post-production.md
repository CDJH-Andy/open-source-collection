# 后期（深度版）

> 后期分两条支线：**照片后期**（显影、修图、合成）与**视频后期**（剪辑、调色、特效、音频）。开源工具在这两条线上都已经能撑起完整交付。

## 一、主线三件套

| 支线 | 选它 | 为什么 |
|---|---|---|
| 照片 | **darktable** | RAW 显影 + 局部调整，非破坏性 |
| 修图/合成 | **GIMP** / **Krita** | GIMP 做修补与合成，Krita 做绘画与贴图 |
| 视频 | **ffmpeg**（底层）+ **Kdenlive**（剪辑） | 一个负责一切转码，一个负责时间线 |

## 二、照片后期链路

```
RAW → 显影（darktable/RawTherapee）
    → 精修（GIMP：污点修复、透视、合成）
    → 风格化（G'MIC 滤镜、Krita 笔刷）
    → 输出（ImageMagick/libvips 批量多尺寸）
```

| 环节 | 项目 | 说明 |
|---|---|---|
| 显影 | [darktable-org/darktable](https://github.com/darktable-org/darktable) | 场景参照 + filmic，动态范围可控 |
| 显影备选 | [RawTherapee/RawTherapee](https://github.com/RawTherapee/RawTherapee) | 降噪与细节还原强 |
| 位图精修 | [GNOME/gimp](https://github.com/GNOME/gimp) | 修复画笔、内容感知填充、图层合成 |
| 绘画/贴图 | [KDE/krita](https://github.com/KDE/krita) | 笔刷引擎接近商业绘画软件 |
| 滤镜集合 | [GreycLab/gmic](https://github.com/GreycLab/gmic) | 500+ 滤镜，可脚本化批量 |
| 批处理 | [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick) | 命令行批量裁剪/水印/格式转换 |
| 高性能缩放 | [libvips/libvips](https://github.com/libvips/libvips) | 超大图不爆内存，适合生成缩略图服务 |
| 色彩管线 | [AcademySoftwareFoundation/OpenColorIO](https://github.com/AcademySoftwareFoundation/OpenColorIO) | ACES 工作流，跳软件色彩一致 |

## 三、视频后期链路

| 环节 | 项目 | 适用场景 |
|---|---|---|
| 剪辑 | [KDE/kdenlive](https://github.com/KDE/kdenlive) | 纪录片、活动片、长视频 |
| 轻量剪辑 | [mltframework/shotcut](https://github.com/mltframework/shotcut) | 快速出片、配置低的机器 |
| 转码/压制 | [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | 一切格式转换、抽帧、加水印 |
| 合成/特效 | [NatronGitHub/Natron](https://github.com/NatronGitHub/Natron) | 节点式合成，类似 Nuke |
| 合成备选 | [blender/blender](https://github.com/blender/blender) | 3D 场景 + 合成一体 |
| 二维动画 | [opentoonz/opentoonz](https://github.com/opentoonz/opentoonz) | 手绘动画、逐帧 |
| 矢量动画 | [synfig/synfig](https://github.com/synfig/synfig) | 参数化动画，适合片头 |
| 音频后期 | [audacity/audacity](https://github.com/audacity/audacity) | 降噪、均衷、混音 |
| 音乐制作 | [Ardour/ardour](https://github.com/Ardour/ardour) | 多轨录音与混音 |
| 字幕 | [Aegisub/Aegisub](https://github.com/Aegisub/Aegisub) | 时间轴精确、样式丰富 |
| 转写 | [openai/whisper](https://github.com/openai/whisper) | 自动字幕初稿 |
| 代码化视频 | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 模板化批量出片（片头、数据视频） |

## 四、调色与色彩科学

| 概念 | 实践 |
|---|---|
| **ACES** | 跳软件统一的色彩空间，Blender、Natron、darktable 都能接 |
| **LUT** | 快速套用风格，但注意输入色彩空间要匹配 |
| **示波器看片** | 用 [ffmpeg](https://github.com/FFmpeg/FFmpeg) 的 `waveform`/`vectorscope` 滤镜检查曝光与肤色 |
| **一致性检查** | 同一批素材先统一白平衡与曝光，再做风格 |

```bash
# 用 ffmpeg 生成波形图，检查曝光分布
ffmpeg -i shot.mov -vf "waveform" -frames:v 1 waveform.png
```

## 五、批量交付（工作室最值钱的部分）

| 需求 | 方案 |
|---|---|
| 一套图出 5 种尺寸 | ImageMagick / libvips 脚本循环 |
| 批量加水印 | `magick composite` 或 libvips overlay |
| 批量清 GPS/版权 | ExifTool `-all=` 后写入版权 |
| 视频批量转 H.264 + 封面 | ffmpeg 一条命令 + `-ss` 抽帧 |
| 模板化短视频批量生产 | Remotion（React 写模板） |

## 六、学习路径

| 阶段 | 内容 | 时间 |
|---|---|---|
| 1 | 掌握一款显影软件（darktable 或 RawTherapee） | 1 周 |
| 2 | 学会图层、蒙版、修补（GIMP） | 1 周 |
| 3 | 色彩管理：校准 + ACES 概念 | 3 天 |
| 4 | 视频剪辑基础：时间线、转场、音频 | 1 周 |
| 5 | ffmpeg 常用参数（`-ss/-to/-vf/-c:v`） | 2 小时 |
| 6 | 合成入门：Natron 或 Blender 合成器 | 2 周 |
| 7 | 批量化：把重复动作写成脚本 | 持续 |

## 七、闭源替代关系

| 商业方案 | 开源对应 | 差距 |
|---|---|---|
| Lightroom + Photoshop | darktable + GIMP | 云同步和 AI 一键功能弱，但可控性更强 |
| DaVinci Resolve | Kdenlive + Natron + OCIO | 调色台与协作功能差一个层级，剪辑够用 |
| Premiere | Kdenlive / Shotcut | 大型工程稳定性略逊 |
| After Effects | Natron / Blender / Remotion | 表达式生态不如 AE |
| 剪映 | ffmpeg + Whisper + Kdenlive | 缺一键模板，但可完全自动化 |

## 八、三条经验

1. **先把一条链路走通，再学第二个软件。** 显影→修图→导出跑通一次，比同时开五个软件有用。
2. **批量处理写成脚本。** 后期真正的瓶颈不是调色水平，是重复劳动。
3. **视频的色彩问题，80% 出在素材阶段。** 拍的时候白平衡和曝光对了，后期能省一半时间。
