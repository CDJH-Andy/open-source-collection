# 模型建模（深度版）

> 建模分两条完全不同的路线，别混着学：
> **美术建模**（Blender，做视觉、渲染、动画）与 **参数化/CAD 建模**（FreeCAD/OpenSCAD，做结构、尺寸、可制造）。
> 摄影师做产品视觉走第一条，做实体道具/支架走第二条。

## 一、主线三件套

| 路线 | 选它 | 为什么 |
|---|---|---|
| 美术建模 | **Blender** | 建模、材质、动画、渲染、合成一体 |
| 参数化/CAD | **FreeCAD** 或 **OpenSCAD** | 尺寸驱动，改一个参数整件跟着变 |
| Web 交付 | **three.js** / **model-viewer** | 把模型放进网页，做产品展示 |

## 二、两条路线怎么分

| 你要做的 | 走哪条 | 工具 |
|---|---|---|
| 产品渲染图、场景搭建、角色 | 美术建模 | Blender |
| 机械结构、道具、支架、可打印件 | 参数化 CAD | FreeCAD / OpenSCAD / CadQuery |
| 网页 3D 展示、交互配置器 | Web 3D | three.js / Babylon.js |
| 扫描件修复、减面、格式转换 | 网格处理 | MeshLab / Instant Meshes / assimp |

## 三、美术建模链路

```
参考图 → 白模（blockout）→ 细化 → UV → 材质 → 灯光 → 渲染 → 后期合成
```

| 环节 | 项目 | 说明 |
|---|---|---|
| 主建模 | [blender/blender](https://github.com/blender/blender) | 官方 donut 教程必做一遍 |
| 材质绘制 | [RodZill4/material-maker](https://github.com/RodZill4/material-maker) | 程序化材质生成 |
| 3D 绘画 | [armory3d/armorpaint](https://github.com/armory3d/armorpaint) | 直接在模型上画贴图 |
| 网格处理 | [cnr-isti-vclab/meshlab](https://github.com/cnr-isti-vclab/meshlab) | 修复、简化、测量 |
| 自动减面 | [wjakob/instant-meshes](https://github.com/wjakob/instant-meshes) | 扫描模型重拓扑 |
| 格式转换 | [assimp/assimp](https://github.com/assimp/assimp) | 几十种 3D 格式互转 |
| 渲染加速 | [blender/blender](https://github.com/blender/blender) Cycles | GPU 渲染，摄影级真实感 |

**产品渲染的关键三件事**（摄影师最该掌握的）：
1. **HDRI 环境光**决定 80% 的质感，比加灯更重要
2. **材质粗糙度**的微小差异，会产生完全不同的商业感
3. **相机焦距与景深**照搬真实摄影参数，产品图才不"假"

## 四、参数化 / CAD 链路

| 项目 | 定位 | 适合什么 |
|---|---|---|
| [FreeCAD/FreeCAD](https://github.com/FreeCAD/FreeCAD) | 参数化 CAD，带装配与工程图 | 结构件、道具、可制造零件 |
| [openscad/openscad](https://github.com/openscad/openscad) | 代码建模（CSG） | 参数化小物件、批量变体 |
| [CadQuery/cadquery](https://github.com/CadQuery/cadquery) | Python 代码建模 | 要接脚本与数据 |
| [slic3r/Slic3r](https://github.com/slic3r/Slic3r) | 3D 打印切片（老牌） | 打印前处理 |
| [prusa3d/PrusaSlicer](https://github.com/prusa3d/PrusaSlicer) | 切片器，配置强 | 主流 FDM 打印 |
| [Ultimaker/Cura](https://github.com/Ultimaker/Cura) | 切片器，易用 | 新手友好 |

```python
# OpenSCAD 的思路：改参数，整件跟着变
// 一个可调参数的支架
w = 60; d = 40; h = 8; hole = 5;
difference() {
  cube([w, d, h], center = true);
  translate([0, 0, 0]) cylinder(d = hole, h = h + 2, center = true);
}
```

## 五、Web 3D 交付

| 项目 | 用途 | 备注 |
|---|---|---|
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | Web 3D 引擎 | 事实标准，生态最大 |
| [BabylonJS/Babylon.js](https://github.com/BabylonJS/Babylon.js) | 另一个 Web 3D 引擎 | 工具链与物理更完整 |
| [KhronosGroup/glTF](https://github.com/KhronosGroup/glTF) | 3D 模型格式标准 | 网页交付就用 glTF/GLB |
| [google/model-viewer](https://github.com/google/model-viewer) | 一行标签展示 3D 模型 | 产品页最省事的方案 |
| [pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber) | 用 React 写 three.js | 前端团队友好 |
| [donmccurdy/glTF-Transform](https://github.com/donmccurdy/glTF-Transform) | glTF 优化与压缩 | 控制网页模型体积 |

**网页模型的体积底线**：单模型压缩后 < 3MB，贴图用 KTX2/Basis，面数控制在 10 万以内，否则手机端加载会崩。

## 六、摄影 × 建模的交叉玩法

| 玩法 | 做法 |
|---|---|
| 产品图合成 | Blender 渲染产品 → 与实拍背景合成 → darktable 统一色调 |
| 场景扩展 | 实拍照片 + 3D 元素（Blender 摄像机反求） |
| 影棚替代 | HDRI + 区域光模拟真实影棚，省下布光时间 |
| 视频片头 | Blender 建模 + 动画 → 渲染序列帧 → ffmpeg 合成 |

Blender 的 **Motion Tracking** 能把实拍素材的相机运动解算出来，再把 3D 物体"放"进真实画面，这是低成本特效的核心技能。

## 七、学习路径

**美术建模（12 周）**

| 周 | 内容 |
|---|---|
| 1–2 | Blender 界面、视图操作、基础建模（官方 donut 教程） |
| 3–4 | 硬表面建模：倒角、布尔、拓扑 |
| 5–6 | UV 展开与贴图绘制 |
| 7–8 | 材质节点、PBR 原理 |
| 9–10 | 灯光与 HDRI，产品渲染 |
| 11–12 | 动画基础 + 渲染输出 + 合成 |

**参数化建模（6 周）**

| 周 | 内容 |
|---|---|
| 1–2 | FreeCAD 草图与约束 |
| 3–4 | 实体特征、装配、工程图 |
| 5 | 导出 STL → 切片 → 打印验证 |
| 6 | OpenSCAD/CadQuery 参数化脚本 |

## 八、闭源替代关系

| 商业方案 | 开源对应 | 差距 |
|---|---|---|
| 3ds Max / Maya | Blender | 工业级动画管线略弱，建模渲染够用 |
| Cinema 4D | Blender | 动态图形生态有差距 |
| SolidWorks | FreeCAD | 曲面与装配稳定性有差距，简单结构够用 |
| KeyShot | Blender Cycles | 上手慢，但可控性与成本优势明显 |
| Sketchfab | model-viewer + 自建站 | 少了社区与托管 |

## 九、三条经验

1. **先学拓扑，再学材质。** 拓扑错了，后面所有环节都在还债。
2. **渲染的真实感来自参考图，不来自参数。** 找一张真实产品照，对着调 HDRI 和粗糙度。
3. **CAD 和美术建模别混着学。** 一个是"尺寸正确"，一个是"看起来对"，思维模型完全不同。
