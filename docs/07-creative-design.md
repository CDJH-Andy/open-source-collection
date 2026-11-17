# 创作与设计

> 这一类项目的价值不是「免费替代 Adobe」，而是它们能做商业软件做不到的事：脚本化、可批量、可嵌入自己的流程。

## 先看结论

| 你要做什么 | 用这个 | 说明 |
|---|---|---|
| 3D 建模、动画、渲染 | **Blender** | 全流程覆盖，插件与 Python API 极强 |
| 做 2D/3D 游戏 | **Godot** | 轻量、开源、无版税分成 |
| 矢量设计、UI 稿 | **Penpot** | 浏览器里的 Figma 替代，可自托管 |
| 位图修图与绘画 | **Krita**（绘画）/ **GIMP**（修图） | Krita 的笔刷体验接近商业软件 |
| 视频剪辑 | **Kdenlive** / **Shotcut** | 需要脚本化就用 ffmpeg |
| 批量图像处理 | **ImageMagick** | 命令行批量裁剪、加水印 |
| 视频转码、抽帧、压制 | **ffmpeg** | 所有视频工具的下游 |
| 做设计系统/图标 | **Lucide** / **Tabler Icons** | 一致性好的开源图标集 |

---

## 3D 与游戏

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [blender/blender](https://github.com/blender/blender) | 全流程 3D 创作套件 | 建模、绑定、动画、渲染、合成一体 |
| [godotengine/godot](https://github.com/godotengine/godot) | 开源游戏引擎，2D/3D 均可 | 导出体积小，社区活跃 |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | 浏览器 3D 渲染 | Web 端 3D 的基础 |
| [bevyengine/bevy](https://github.com/bevyengine/bevy) | Rust 的 ECS 游戏引擎 | 数据驱动，性能好 |
| [assimp/assimp](https://github.com/assimp/assimp) | 3D 模型格式转换库 | 处理各种模型格式的万金油 |

## 图像与矢量

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [penpot/penpot](https://github.com/penpot/penpot) | 开源设计協作平台，基于 Web | 可自托管，团队協作免费 |
| [KDE/krita](https://github.com/KDE/krita) | 数字绘画，笔刷引擎强 | 插画师主力 |
| [GNOME/gimp](https://github.com/GNOME/gimp) | 位图编辑 | 修图、批处理 |
| [Inkscape/inkscape](https://github.com/Inkscape/inkscape) | 矢量图形编辑 | SVG 处理最专业 |
| [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick) | 命令行图像处理 | 批量裁切、格式转换 |
| [libvips/libvips](https://github.com/libvips/libvips) | 低内存高性能图像处理库 | 处理超大图不爆内存 |
| [lucide-icons/lucide](https://github.com/lucide-icons/lucide) | 风格统一的图标库 | 前后端都能用 |

## 视频与音频

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | 音视频处理的底层工具 | 转码、抽帧、压制、滤镜 |
| [KDE/kdenlive](https://github.com/KDE/kdenlive) | 非线性视频剪辑 | Linux 上最成熟的开源剪辑 |
| [mltframework/shotcut](https://github.com/mltframework/shotcut) | 跳平台视频编辑器 | 轻量、稳定 |
| [audacity/audacity](https://github.com/audacity/audacity) | 音频录制与编辑 | 播客、配音后期 |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 用 React 代码生成视频 | 批量做模板化视频的神器 |
| [openai/whisper](https://github.com/openai/whisper) | 语音识别，字幕生成 | 剪视频配字幕的效率工具 |

---

## 上手建议

1. **Blender 的学习曲线是真的陡。** 别从「做一个完整的作品」开始，先跟着官方 donut 教程走一遍，把所有界面区域摸熟。
2. **ffmpeg 值得单独花两小时学。** 学会 `-ss/-to/-vf/-c:v` 这几个参数，日常视频处理基本不求人。
3. **Remotion 这类「代码生成视频」的工具，适合模板化批量生产**，不适合做需要手工调度的创意片。
