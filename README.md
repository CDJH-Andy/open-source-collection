# Open Source Collection

> GitHub 上那些**真的很强、真的出名、真的好用**的开源项目，按场景归档在这里。
> 不是把 star 榜抄一遍，而是按「我现在要解决的问题」来编排。

![status](https://img.shields.io/badge/status-maintained-brightgreen)
![scope](https://img.shields.io/badge/scope-curated-blue)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

---

## 这份清单怎么用

别从头读到尾，按你当下的状态挑一条路径：

| 你的状态 | 直接看 | 大概能省下 |
|---|---|---|
| 想让手上的活儿变快（写代码、写文档、查资料） | [开发者工具](./docs/04-devops-tools.md) | 每天 1–2 小时 |
| 想在自己电脑/服务器上搭点东西（网盘、相册、笔记、AI 助手） | [自托管与生活](./docs/05-selfhosted-life.md) | 一年几千块订阅费 |
| 想搞 AI（本地跑模型、做知识库、搭 Agent 工作流） | [AI 与大模型](./docs/01-ai-llm.md) | 少走半年弯路 |
| 想正经学一门手艺（前端、后端、算法、系统设计） | [学习与资源](./docs/06-learning-resources.md) | 一份培训班的钱 |
| 手头有个项目要选型（框架、数据库、部署方式） | [后端与数据库](./docs/03-backend-databases.md) | 一次返工 |

---

## 闭眼装：十个不需要犹豫的项目

如果只装十个，就是这十个。它们共同的特征是：**装上当天就能用，用了就回不去。**

| # | 项目 | 它替你解决什么 | 平台 |
|---|---|---|---|
| 1 | [Ollama](https://github.com/ollama/ollama) | 一条命令在本地跑大模型，不用折腾 CUDA 和环境 | Win / macOS / Linux |
| 2 | [VS Code](https://github.com/microsoft/vscode) | 写代码这件事的默认答案，插件生态无敌 | 全平台 |
| 3 | [Logseq](https://github.com/logseq/logseq) | 大纲式双向链接笔记，本地存储不怕跑路 | 全平台 |
| 4 | [Immich](https://github.com/immich-app/immich) | 自建相册，手机自动备份，替代 iCloud/Google 相册 | Docker |
| 5 | [n8n](https://github.com/n8n-io/n8n) | 把重复的跨应用操作变成自动化流程，自带 AI 节点 | Docker / 云端 |
| 6 | [Dify](https://github.com/langgenius/dify) | 拖拽就能搭出带知识库的 AI 应用，不用写后端 | Docker |
| 7 | [Excalidraw](https://github.com/excalidraw/excalidraw) | 手绘风白板，画架构图和流程图最快的工具 | Web |
| 8 | [ripgrep](https://github.com/BurntSushi/ripgrep) | 在几万个文件里秒级搜索，比 IDE 搜索快一个量级 | CLI |
| 9 | [Vaultwarden](https://github.com/dani-garcia/vaultwarden) | 自建密码管理器，兼容 Bitwarden 全客户端 | Docker |
| 10 | [ffmpeg](https://github.com/FFmpeg/FFmpeg) | 一切视频音频处理的底层工具，转码剪辑抽帧全靠它 | CLI |

---

## 分类目录

| 分类 | 内容概要 | 文档 |
|---|---|---|
| **AI 与大模型** | 本地推理、Agent 框架、RAG 知识库、图像与语音生成 | [docs/01-ai-llm.md](./docs/01-ai-llm.md) |
| **Web 与前端** | 框架、构建工具、UI 组件库、可视化 | [docs/02-web-frontend.md](./docs/02-web-frontend.md) |
| **后端与数据库** | 语言运行时、Web 框架、关系型/向量/时序数据库 | [docs/03-backend-databases.md](./docs/03-backend-databases.md) |
| **开发者工具** | 编辑器、终端、CLI 神器、DevOps 与可观测性 | [docs/04-devops-tools.md](./docs/04-devops-tools.md) |
| **自托管与生活** | 相册、网盘、媒体库、家庭自动化、效率服务 | [docs/05-selfhosted-life.md](./docs/05-selfhosted-life.md) |
| **学习与资源** | 免费课程、路线图、Awesome 系列、面试与系统设计 | [docs/06-learning-resources.md](./docs/06-learning-resources.md) |
| **创作与设计** | 3D、游戏引擎、图像处理、视频合成、设计工具 | [docs/07-creative-design.md](./docs/07-creative-design.md) |

---

## 三条选型原则

收藏夹最容易变成垃圾场，所以这里只留经过这三条筛选的项目：

1. **有人在真用它干活**，不是只有 README 写得漂亮。判断标准：issue 区有真实用户在问具体问题，而不是清一色的 "great project"。
2. **维护还活着**。最近一次 commit 在半年内，或者明确是稳定完成态（比如 SQLite 这种不需要天天更新的）。
3. **卸载成本低**。数据能导出、能自建、不锁死在你机器之外。这条最容易被忽略，但决定了你三年后还能不能把东西搬走。

关于「同类到底选哪个」，每个分类文档开头都有一节 **「同类怎么选」**，直接给结论，不列一堆参数让你自己比。

---

## 仓库结构

```
open-source-collection/
├── README.md                 # 你正在看的导航
├── docs/                     # 按分类展开的清单
├── scripts/check_links.py    # 链接存活检测，防止清单腐烂
├── .github/workflows/        # 每周自动跑一次链接检测
├── CONTRIBUTING.md           # 收录标准
└── LICENSE
```

清单会腐烂，所以这个仓库带了自动化的链接巡检：每周一自动检查所有外链是否 404，结果直接开 issue。**一个没人维护的 awesome 列表，三个月后就是一堆死链。**

---

## 维护说明

- 收录标准见 [CONTRIBUTING.md](./CONTRIBUTING.md)
- 清单更新节奏：随缘，但每次更新都会跑一遍链接检测
- 如果你发现链接失效或项目已经烂尾，欢迎直接提 issue

> 说明：本项目是一个**人工策展的索引**，不包含上述任何项目的源码，版权归各原作者所有。清单里的评价为主观判断，仅供选型参考。
