# 网页设计（深度版）

> 网页设计不是"会用 Figma"，是**能从设计稿一路推到上线，并且保证多尺寸、多语言、可访问**。
> 开源世界的重点在：设计工具、设计系统、字体与图标、动效、可访问性。

## 一、主线三件套

| 层 | 选它 | 为什么 |
|---|---|---|
| 设计工具 | **Penpot** | 浏览器里做设计，可自托管，CSS 属性直接可见 |
| 样式系统 | **Tailwind + 设计 token** | 设计与代码共用一套变量 |
| 字体 | **Fontsource + 开源中文字体** | 字体自托管，不依赖第三方 CDN |

## 二、从设计稿到上线

```
① 结构      Excalidraw / tldraw 画线框，先定信息层级
      ↓
② 视觉      Penpot 做高保真，用组件与 token 组织
      ↓
③ 设计系统  色彩/字阶/间距/圆角定成变量，与 Tailwind 对齐
      ↓
④ 实现      Tailwind + shadcn 落地，组件即文档
      ↓
⑤ 动效      Motion / Lottie / Rive 按需加
      ↓
⑥ 验收      对比度、键盘操作、多尺寸、性能四项检查
```

## 三、设计工具

| 项目 | 定位 | 说明 |
|---|---|---|
| [penpot/penpot](https://github.com/penpot/penpot) | 开源设计協作平台 | 设计稿本身就是 CSS 语义，交付摩擦最小 |
| [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) | 手绘风线框 | 前期讨论最快 |
| [tldraw/tldraw](https://github.com/tldraw/tldraw) | 无限画布 SDK | 想嵌到自己产品里 |
| [penpot/penpot-exporter-figma-plugin](https://github.com/penpot/penpot-exporter-figma-plugin) | Figma 导入 Penpot | 迁移老稿子用 |

## 四、设计系统

| 项目 | 提供什么 |
|---|---|
| [radix-ui/colors](https://github.com/radix-ui/colors) | 12 阶色板，自动生成深色模式与对比度 |
| [argyleink/open-props](https://github.com/argyleink/open-props) | 一套 CSS 变量：颜色、阴影、字阶、缓动 |
| [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss) | 把 token 变成类名 |
| [shadcn-ui/ui](https://github.com/shadcn-ui/ui) | 组件代码 + token，天然可改 |
| [radix-ui/primitives](https://github.com/radix-ui/primitives) | 可访问性完备的交互原语 |
| [design-tokens/community-group](https://github.com/design-tokens/community-group) | 设计 token 的标准格式（DTCG） |

**一条经验**：设计系统最小的可用集合是 **4 个色阶 + 5 个字阶 + 4 个间距档 + 2 个圆角 + 2 个阴影**。先定这些，再谈组件库。

## 五、字体与图标

| 项目 | 用途 | 备注 |
|---|---|---|
| [fontsource/fontsource](https://github.com/fontsource/fontsource) | 字体自托管，按需加载 | 不再依赖 Google Fonts 网络 |
| [google/fonts](https://github.com/google/fonts) | 开源字体仓库（OFL） | 商用基本安全，注意个别字体条款 |
| [adobe-fonts/source-han-sans](https://github.com/adobe-fonts/source-han-sans) | 思源黑体 | 中文正文首选，字重齐全 |
| [adobe-fonts/source-han-serif](https://github.com/adobe-fonts/source-han-serif) | 思源宋体 | 中文标题/长文排版 |
| [atelier-anchor/smiley-sans](https://github.com/atelier-anchor/smiley-sans) | 得意黑 | 中文标题的高辨识度选择 |
| [lxgw/LxgwWenKai](https://github.com/lxgw/LxgwWenKai) | 霸鹜文楷 | 文艺气质，适合海报式页面 |
| [lucide-icons/lucide](https://github.com/lucide-icons/lucide) | 统一风格图标 | 线性、可调线宽 |
| [tabler/tabler-icons](https://github.com/tabler/tabler-icons) | 5000+ 图标 | 覆盖广 |
| [phosphor-icons/phosphor-icons](https://github.com/phosphor-icons/phosphor-icons) | 多字重图标 | 三种线重可选 |

**中文排版三个坑**：字重不要超过两个（加载成本）、行高 1.6–1.8（汉字方块感强）、标点避开行首行尾（用 `text-spacing-trim` 或手工处理）。

## 六、动效

| 项目 | 适合什么 | 注意 |
|---|---|---|
| [motiondivision/motion](https://github.com/motiondivision/motion) | 布局动画、手势、滚动驱动 | React/Vue 都有适配 |
| [airbnb/lottie-web](https://github.com/airbnb/lottie-web) | AE 导出的矢量动画 | 文件体积要控制 |
| [rive-app/rive-react](https://github.com/rive-app/rive-react) | 可交互角色/图标动画 | 状态机驱动，交互强 |
| [theatre-js/theatre](https://github.com/theatre-js/theatre) | 可视化编排复杂序列 | 适合品牌页 |
| [greensock/GSAP](https://github.com/greensock/GSAP) | 时间轴、滚动叙事 | 核心免费，插件部分收费 |

## 七、可访问性与验收

| 项目 | 用途 |
|---|---|
| [dequelabs/axe-core](https://github.com/dequelabs/axe-core) | 自动化可访问性检测 |
| [a11yproject/a11yproject.com](https://github.com/a11yproject/a11yproject.com) | 检查清单与常见模式 |
| [w3c/wcag](https://github.com/w3c/wcag) | WCAG 标准原文 |
| [GoogleChrome/lighthouse](https://github.com/GoogleChrome/lighthouse) | 性能 + 可访问性 + SEO 综合评分 |

**上线前四项检查**：
1. 正文对比度 ≥ 4.5:1（用 axe 扫一遍）
2. 所有交互元素可键盘操作，焦点可见
3. 320px / 768px / 1440px 三个宽度不塌
4. 首屏 LCP < 2.5s

## 八、学习路径

| 阶段 | 内容 | 产出 |
|---|---|---|
| 1 | 版式四原则：对齐、亲密、重复、对比 | 三个模仿页面 |
| 2 | 栅格与间距系统 | 一套 8pt 栅格稿 |
| 3 | 色彩与对比度 | 一套配色 token |
| 4 | 中英混排 | 一个双语落地页 |
| 5 | 组件与状态设计 | 一个含 12 个组件的设计系统 |
| 6 | 动效节奏 | 三个微交互 |
| 7 | 交付与验收 | 用 Penpot → Tailwind 完整落地一版 |

## 九、闭源替代关系

| 商业方案 | 开源对应 | 差距 |
|---|---|---|
| Figma | Penpot | 插件生态与自动布局细节有差距，協作够用 |
| Sketch | Penpot | 平台限制消失 |
| Webflow | Vite + Tailwind + CMS | 可视化程度低，但性能与可控性更好 |
| Adobe Fonts | Fontsource + 开源字体 | 字体数量少，但版权清晰 |

## 十、三条经验

1. **设计稿的价值在于约束，不在好看。** 有 token 的设计稿能直接变成代码，没有 token 的只是图片。
2. **中文字体是网页设计的分水岭。** 用系统默认字体的中文页面，一眼就是"没做完"。
3. **动效要少而慢。** 一页三个以上动效，用户就开始等你了。
