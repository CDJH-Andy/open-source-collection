# 前端（深度版）

> 目标不是"会写组件"，是**能独立交付一个上线可用的 Web 应用**：从脚手架到部署、从性能到可访问性。

## 一、主线三件套

| 层 | 选它 | 为什么 |
|---|---|---|
| 构建 | **Vite** | 冷启动秒级，配置少，生态已成熟 |
| 语言 | **TypeScript** | 大型项目不写类型等于给自己挖坑 |
| 框架 | **React**（要生态与招人）/ **Vue 3**（要开发体验） | 二选一，别纠结第三个 |

```bash
pnpm create vite@latest my-app --template react-ts
```

## 二、必装工具链

| 用途 | 项目 | 说明 |
|---|---|---|
| 包管理 | [pnpm/pnpm](https://github.com/pnpm/pnpm) | 硬链接省磁盘，monorepo 友好 |
| 格式化 + Lint | [biomejs/biome](https://github.com/biomejs/biome) | Rust 实现，一个替掉 Prettier + ESLint |
| 单元测试 | [vitest-dev/vitest](https://github.com/vitest-dev/vitest) | 和 Vite 同一套配置，几乎零成本 |
| 端到端测试 | [microsoft/playwright](https://github.com/microsoft/playwright) | 跳浏览器，能截图对比 |
| 组件文档 | [storybookjs/storybook](https://github.com/storybookjs/storybook) | 组件先在这里活，再进业务 |
| Monorepo | [vercel/turborepo](https://github.com/vercel/turborepo) | 多包项目缓存构建，省一半时间 |

## 三、样式与设计系统

| 项目 | 定位 | 什么时候用 |
|---|---|---|
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 原子化 CSS | 默认选择，配合设计 token |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 可复制组件（Radix + Tailwind） | 要能改样式的中后台/官网 |
| [radix-ui/primitives](https://github.com/radix-ui/primitives) | 无样式、可访问性完备的底层组件 | 自己造设计系统时当地基 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | 企业级组件库 | 中后台赶工期 |
| [vanilla-extract-css/vanilla-extract](https://github.com/vanilla-extract-css/vanilla-extract) | 类型安全的 CSS-in-TS | 要强约束的设计系统 |
| [csstools/postcss-plugins](https://github.com/csstools/postcss-plugins) | 新 CSS 特性的兼容层 | 想用 container query 等新特性 |

## 四、动效与交互

| 项目 | 定位 | 备注 |
|---|---|---|
| [motiondivision/motion](https://github.com/motiondivision/motion) | 声明式动画（原 Framer Motion） | React 项目首选 |
| [greensock/GSAP](https://github.com/greensock/GSAP) | 时间轴动画，复杂编排强 | 核心免费，部分插件收费 |
| [airbnb/lottie-web](https://github.com/airbnb/lottie-web) | 播放 AE 导出的 JSON 动画 | 运营位动效常用 |
| [rive-app/rive-react](https://github.com/rive-app/rive-react) | 可交互矢量动画 | 状态机驱动，比 Lottie 更"活" |
| [theatre-js/theatre](https://github.com/theatre-js/theatre) | 可视化动画编辑器 | 做复杂镜头序列 |

## 五、性能与质量

| 项目 | 用来干什么 |
|---|---|
| [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | 一次性体检：性能、可访问性、SEO |
| [GoogleChrome/web-vitals](https://github.com/GoogleChrome/web-vitals) | 线上采集真实用户指标（LCP/CLS/INP） |
| [vercel/next.js](https://github.com/vercel/next.js) | 需要 SSR/SSG 时的全栈方案 |
| [unjs/unplugin](https://github.com/unjs/unplugin) | 一套插件适配 Vite/Webpack/Rollup |
| [a11yproject/a11yproject.com](https://github.com/a11yproject/a11yproject.com) | 可访问性检查清单，交付前过一遍 |

## 六、跳端与桌面

| 项目 | 能做什么 | 坑 |
|---|---|---|
| [expo/expo](https://github.com/expo/expo) | React Native 工具链，一套代码出 iOS/Android | 原生能力仍要写桥接 |
| [tauri-apps/tauri](https://github.com/tauri-apps/tauri) | 用前端技术做桌面应用，产物比 Electron 小一个量级 | 依赖系统 WebView，兼容性要测 |
| [electron/electron](https://github.com/electron/electron) | 桌面应用老牌方案 | 包体大、内存高 |

## 七、学习路径（8 周）

| 周 | 目标 | 产出 |
|---|---|---|
| 1 | HTML/CSS 基本功 + Flex/Grid | 一个纯 CSS 的响应式页面 |
| 2 | JS 基础：作用域、异步、事件循环 | 三个小 demo（计时器、请求、表单校验） |
| 3 | TypeScript 类型系统 | 把第 2 周的 demo 全部改写成 TS |
| 4 | React/Vue 组件与状态 | 一个带增删改查的待办应用 |
| 5 | 路由、请求、状态管理 | 接真实 API 的列表页 |
| 6 | 工程化：Lint/测试/CI | 给项目配齐 Biome + Vitest + Actions |
| 7 | 性能与可访问性 | Lighthouse 分数刷到 90+ |
| 8 | 部署 | 用 Docker + Caddy 上线一个真站点 |

## 八、闭源替代关系

| 商业方案 | 开源对应 | 差距 |
|---|---|---|
| Webflow / Framer | Vite + Tailwind + 自建 CMS | 可视化拖拽需要自己写或换开源 CMS |
| Figma 交付 | Penpot（见 [web-design.md](./web-design.md)） | 生态插件少，但协作够用 |
| Vercel 托管 | 自建 Docker + Caddy/Traefik | 少了自动预览部署，可用 Actions 补 |

## 九、三条经验

1. **先跑通再优化。** 把 Lighthouse 刷到 100 分再发第一个版本，是把项目做死的常见方式。
2. **状态管理别提前上。** 一个 `useState` + 一个请求库能撑到 90% 的应用，Redux 是给复杂场景准备的。
3. **组件库选一个，然后闭嘴用。** 两套设计语言混用，返工成本远高于省下的时间。
