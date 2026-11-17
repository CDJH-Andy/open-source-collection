# Web 与前端

## 同类怎么选（先看结论）

| 你的场景 | 选它 | 理由 |
|---|---|---|
| 新项目、要生态、要招人 | **React + Next.js** | 生态和岗位需求都最大，遇到问题搜得到答案 |
| 想要更好的开发体验和性能 | **Vue 3 + Nuxt** | 单文件组件顺手，中文资料极多 |
| 讨厌虚拟 DOM 和运行时包袂 | **Svelte / SvelteKit** | 编译期解决，产物小 |
| 内容站、博客、文档站 | **Astro** | 默认零 JS，天生为内容优化 |
| 只想要一套能直接用的组件 | **shadcn/ui** | 代码复制到你项目里，想怎么改怎么改 |

---

## 框架

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [facebook/react](https://github.com/facebook/react) | UI 的事实标准，生态最庞大 | 学习曲线中等，坑也多，但答案最多 |
| [vercel/next.js](https://github.com/vercel/next.js) | React 的全栈框架，SSR/SSG/边缘函数 | 部署 Vercel 最顺，自托管也行 |
| [vuejs/core](https://github.com/vuejs/core) | 渐进式框架，模板语法直观 | 国内团队首选之一 |
| [nuxt/nuxt](https://github.com/nuxt/nuxt) | Vue 的全栈框架 | 类似 Next.js 之于 React |
| [sveltejs/svelte](https://github.com/sveltejs/svelte) | 编译期框架，运行时极小 | 写起来最像「写普通 JS」 |
| [withastro/astro](https://github.com/withastro/astro) | 内容优先的站点框架 | 博客、文档站神器 |
| [honojs/hono](https://github.com/honojs/hono) | 为边缘计算优化的极速 Web 框架 | 想在 Cloudflare Workers 上跑 API 就用它 |

## 构建与语言

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [vitejs/vite](https://github.com/vitejs/vite) | 新一代构建工具，冷启动秒开 | 已基本取代 webpack 做新项目 |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | 给 JS 加类型，2025 年起 GitHub 语言榜第一 | 大型项目几乎必选 |
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 原子化 CSS，写样式不用起名字 | 初期会别扭，一周后回不去 |
| [biomejs/biome](https://github.com/biomejs/biome) | Rust 写的格式化 + lint，一个换掉 Prettier+ESLint | 速度提升明显 |

## UI 组件与可视化

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 可复制的组件集合，基于 Radix + Tailwind | 不是 npm 包，是「把代码给你」 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | 企业级中后台组件库 | 国内中后台事实标准 |
| [element-plus/element-plus](https://github.com/element-plus/element-plus) | Vue 3 组件库 | 和 Ant Design 对应 |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 手绘风白板，可嵌入自己的应用 | 画架构图最快的工具 |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | 可编程的无限画布 SDK | 想自己做白板产品就用它 |
| [mrdoob/three.js](https://github.com/mrdoob/three.js) | Web 3D 的默认答案 | 学习曲线陡，但绕不开 |
| [apache/echarts](https://github.com/apache/echarts) | 图表库，中文文档完善，样式可控 | 国内数据可视化常用 |
| [d3/d3](https://github.com/d3/d3) | 数据驱动文档，可视化的底层语言 | 不是「图表库」，是工具箱 |

---

## 上手建议

1. **先确定交付形态再选框架。** 内容站选 Astro，后台系统选 React/Vue + 组件库，别用 Next.js 硬做一个只有十页的官网。
2. **组件库别混用。** Ant Design 和 shadcn 混在一个项目里，两套设计语言打架，改到怀疑人生。
3. **Tailwind 的价值在约束。** 它逼你用统一的设计 token，比「随手写个 13px」长期好维护。
