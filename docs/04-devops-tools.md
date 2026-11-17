# 开发者工具

> 这一类项目的共同点：装上之后你不会特意想起它，但换一台新电脑第一件事就是把它装回去。

## 编辑器与终端

| 项目 | 一句话定位 | 平台 |
|---|---|---|
| [microsoft/vscode](https://github.com/microsoft/vscode) | 最主流的代码编辑器，插件生态无敌 | 全平台 |
| [neovim/neovim](https://github.com/neovim/neovim) | 终端里的编辑器，可编程、启动快 | 全平台 |
| [Microsoft/terminal](https://github.com/microsoft/terminal) | Windows 上的现代终端 | Windows |
| [tmux/tmux](https://github.com/tmux/tmux) | 终端复用，断线不丢会话 | Linux/macOS |
| [junegunn/fzf](https://github.com/junegunn/fzf) | 模糊搜索一切：文件、历史命令、分支 | 全平台 |
| [jesseduffield/lazygit](https://github.com/jesseduffield/lazygit) | 终端里的 Git 图形界面，键盘操作飞快 | 全平台 |
| [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | Zsh 配置框架，主题和插件开箱即用 | Linux/macOS |

## 命令行神器

| 项目 | 一句话定位 | 为什么会回不去 |
|---|---|---|
| [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep) | 递归搜索文本，速度远超 grep | 几万个文件里搜索是毫秒级 |
| [sharkdp/bat](https://github.com/sharkdp/bat) | 带语法高亮的 cat | 看代码和配置不再瞎 |
| [sharkdp/fd](https://github.com/sharkdp/fd) | 更友好的 find 替代 | 语法简单到不用查文档 |
| [jqlang/jq](https://github.com/jqlang/jq) | 命令行 JSON 处理器 | 处理 API 返回值的必备 |
| [httpie/httpie](https://github.com/httpie/httpie) | 人类可读的 HTTP 客户端 | 比 curl 的语法直观太多 |
| [tldr-pages/tldr](https://github.com/tldr-pages/tldr) | 命令的「示例版」手册 | 只给最常见的几个用法 |
| [mikefarah/yq](https://github.com/mikefarah/yq) | YAML/JSON/XML 命令行处理 | 改 K8s 配置不用手抖缩进 |

## DevOps 与基础设施

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | 容器编排的事实标准 | 团队 <5 人时通常不需要 |
| [moby/moby](https://github.com/moby/moby) | Docker 引擎本体 | 一切容器化的起点 |
| [git/git](https://github.com/git/git) | 版本控制 | 不会也得会 |
| [traefik/traefik](https://github.com/traefik/traefik) | 云原生反向代理，自动发现服务并签发证书 | 自托管必备 |
| [ansible/ansible](https://github.com/ansible/ansible) | 无 Agent 的配置管理 | 管几台机器比手敲强 |
| [hashicorp/terraform](https://github.com/hashicorp/terraform) | 基础设施即代码 | 云资源可复现 |
| [prometheus/prometheus](https://github.com/prometheus/prometheus) | 指标采集与告警 | 监控的标准答案 |
| [grafana/grafana](https://github.com/grafana/grafana) | 可视化面板 | 和 Prometheus 天生一对 |
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | 轻量自建 Git 服务 | 一台小机器就能跑 |

## 提效小工具

| 项目 | 用途 |
|---|---|
| [dani-garcia/vaultwarden](https://github.com/dani-garcia/vaultwarden) | 自建密码库，兼容 Bitwarden 客户端 |
| [localsend/localsend](https://github.com/localsend/localsend) | 局域网跨设备传文件，替代微信传文件助手 |
| [ShareX/ShareX](https://github.com/ShareX/ShareX) | Windows 截图与录屏全能工具 |
| [microsoft/PowerToys](https://github.com/microsoft/PowerToys) | Windows 效率增强套件（窗口管理、批量重命名等） |
| [logseq/logseq](https://github.com/logseq/logseq) | 本地优先的大纲式笔记，数据存本地 |

---

## 上手建议

1. **先把 ripgrep、fd、bat、fzf 装上。** 这四个是纯增量收益，没有任何学习成本。
2. **别花一周配 Neovim。** 除非你确定要长期投入，否则 VS Code + Vim 插件是性价比最高的组合。
3. **自托管 Git 优先 Gitea 而不是 GitLab。** 单机 2G 内存就能跑，GitLab 起步要 4G 以上。
