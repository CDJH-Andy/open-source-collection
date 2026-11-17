# Open Source Collection

> 七条主攻线：**前端 / 后端 / AI / 摄影 / 后期 / 网页设计 / 模型建模**。
> 每条线只留真正会用到的工具，按「先装什么 → 再学什么 → 怎么串成工作流」组织。

![status](https://img.shields.io/badge/status-maintained-brightgreen)
![tracks](https://img.shields.io/badge/tracks-7-blue)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 七条主攻线

| # | 主攻线 | 主线三件套（先装这三个） | 深度文档 |
|---|---|---|---|
| 1 | **前端** | Vite + TypeScript + React（或 Vue） | [tracks/frontend.md](./tracks/frontend.md) |
| 2 | **后端** | FastAPI 或 Hono + PostgreSQL + Docker | [tracks/backend.md](./tracks/backend.md) |
| 3 | **AI** | Ollama + Dify + ComfyUI | [tracks/ai.md](./tracks/ai.md) |
| 4 | **摄影** | darktable + ExifTool + PhotoPrism | [tracks/photography.md](./tracks/photography.md) |
| 5 | **后期** | darktable + GIMP/Krita + ffmpeg | [tracks/post-production.md](./tracks/post-production.md) |
| 6 | **网页设计** | Penpot + Tailwind + Fontsource | [tracks/web-design.md](./tracks/web-design.md) |
| 7 | **模型建模** | Blender + FreeCAD + three.js | [tracks/modeling.md](./tracks/modeling.md) |

---

## 这七条线怎么串起来

这不是七个孤立的技能，而是一条**内容生产链**。你是摄影师、又在做传媒公司，这套串联方式比单独学任何一项都值钱：

```
拍摄（摄影）          现场用 gPhoto2 联机拍摄、ExifTool 记录参数
   ↓
素材管理（摄影）      rclone/restic 双备份 → PhotoPrism 建库检索
   ↓
选片与调色（后期）    darktable 批量选片 + 色彩管理（OCIO/ACES）
   ↓
成片与特效（后期）    GIMP/Krita 修图，Natron/Blender 合成，ffmpeg 压制
   ↓
三维补充（建模）      Blender 搭场景/做产品渲染，或 FreeCAD 出结构件
   ↓
对外呈现（网页设计）  Penpot 出设计稿 → 设计系统 → Tailwind 落地
   ↓
系统承载（前端/后端） Next.js/Hono + PostgreSQL 做作品集站与客户后台
   ↓
效率放大（AI）        Dify 做客服知识库，ComfyUI 做批量出图，Whisper 做字幕
```

一条实际场景：**给客户做一套产品视觉**——Blender 建模渲染 → darktable 调色 → 网页设计出落地页 → 前端实现 → AI 批量生成多尺寸物料。五条线各出一段力，交付周期能压掉一半。

---

## 如果你只有一周

别七条线一起开。按这个顺序，一周能拿到第一个闭环：

| 天 | 做什么 | 用哪个项目 |
|---|---|---|
| Day 1 | 装好编辑器与命令行基本功 | VS Code + ripgrep + fzf |
| Day 2 | 跑通本地大模型，建立"AI 能帮我干什么"的直觉 | Ollama + Open WebUI |
| Day 3 | 把照片管起来（备份 + 建库 + 检索） | Immich 或 PhotoPrism |
| Day 4 | 调一张照片，走完 RAW → 导出 | darktable |
| Day 5 | 用 Blender 跟完官方 donut 教程 | Blender |
| Day 6 | 用 Penpot 画一版落地页 | Penpot |
| Day 7 | 把落地页实现出来，部署上线 | Vite + Hono + Docker |

---

## 资料库（非主攻，但迟早用得上）

| 分类 | 内容 | 文档 |
|---|---|---|
| 开发者工具全览 | 终端、CLI、DevOps、可观测性 | [docs/04-devops-tools.md](./docs/04-devops-tools.md) |
| 自托管与生活 | 相册、网盘、媒体库、家庭自动化 | [docs/05-selfhosted-life.md](./docs/05-selfhosted-life.md) |
| 学习与资源 | 路线图、免费课程、Awesome 系列 | [docs/06-learning-resources.md](./docs/06-learning-resources.md) |
| 通用前端清单 | 框架、组件库、可视化 | [docs/02-web-frontend.md](./docs/02-web-frontend.md) |
| 通用后端清单 | 语言、框架、数据库 | [docs/03-backend-databases.md](./docs/03-backend-databases.md) |
| AI 通用清单 | 推理、Agent、生成模型 | [docs/01-ai-llm.md](./docs/01-ai-llm.md) |
| 创作与设计清单 | 3D、图像、音视频工具 | [docs/07-creative-design.md](./docs/07-creative-design.md) |

主攻线文档是**深挖版**（含学习路径和工作流），资料库文档是**广度版**（含同类对比）。同一个项目可能两边都出现，这是故意的：深挖版告诉你「怎么用它」，广度版告诉你「还能换什么」。

---

## 三条筛选原则

1. **有人在真用它干活**：issue 区有具体使用问题，不是清一色的 "great project"。
2. **维护还活着**：半年内有实质提交，或属于稳定完成态（SQLite、ffmpeg 这类）。
3. **卸载成本低**：数据能导出、能自建、不锁死在你机器之外。

---

## 关于商业软件的边界

这个仓库只收**开源**项目。但你日常绕不开 Lightroom、Capture One、DaVinci Resolve、Figma 这些闭源工具，所以每条主攻线文档里都有一节「闭源替代关系」，说明：**它在开源世界里对应谁、能替代到什么程度、哪一步还是得回商业软件。**不装作开源能解决一切。

---

## 仓库结构

```
open-source-collection/
├── README.md                 # 七条主攻线的导航
├── tracks/                   # 七份深度文档（主攻线）
│   ├── frontend.md
│   ├── backend.md
│   ├── ai.md
│   ├── photography.md
│   ├── post-production.md
│   ├── web-design.md
│   └── modeling.md
├── docs/                     # 七份广度清单（资料库）
├── scripts/check_links.py    # 链接存活检测
├── .github/workflows/        # 每周自动巡检，死链自动开 issue
├── CONTRIBUTING.md
└── LICENSE
```

> 说明：本仓库是人工策展的索引，不包含任何第三方项目的源码，版权归各原作者所有。文档中的评价为主观判断，仅供选型参考。
