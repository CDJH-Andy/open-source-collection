# AI 与大模型

> 这一块是 2024 年之后 GitHub 上最卷的领域。卷的好处是：你几乎不需要自己写底层，缺什么都有现成的。

## 同类怎么选（先看结论）

| 你想干的事 | 选它 | 不要选 |
|---|---|---|
| 在自己电脑上跑模型，图省事 | **Ollama** | 别一上来就编译 llama.cpp |
| 要榨干硬件性能、做量化实验 | **llama.cpp** | Ollama 的可调参数不够 |
| 部署给几十上百人用，要高吞吐 | **vLLM** | 别拿 Ollama 当生产推理服务 |
| 搭带知识库的 AI 应用，不写代码 | **Dify** | LangChain 需要写代码 |
| 要做复杂的自定义 Agent 逻辑 | **LangChain / LangGraph** | Dify 的灵活性有上限 |
| 解析复杂 PDF/表格做企业知识库 | **RAGFlow** | 轻量场景用 Dify 就够 |
| 跑图（Stable Diffusion 系） | **ComfyUI** | WebUI 更适合新手但扩展性弱 |

---

## 本地推理与模型运行时

| 项目 | 一句话定位 | 适合谁 | 上手 |
|---|---|---|---|
| [ollama/ollama](https://github.com/ollama/ollama) | `ollama run llama3` 就能跑，模型管理、API 一体 | 所有人，尤其是非科班 | 极低 |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | C++ 实现的本地推理引擎，量化格式的事实标准 | 想压性能、玩量化的人 | 中 |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 高吞吐推理服务，PagedAttention 出处 | 部署生产 API 的人 | 中高 |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 模型加载与微调的核心库，AI 界的「标准库」 | 要做训练/微调的人 | 中 |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 给 Ollama/vLLM 套一个 ChatGPT 式界面 | 想给团队一个内网 ChatGPT | 低（Docker） |

## Agent 与应用框架

| 项目 | 一句话定位 | 适合谁 | 上手 |
|---|---|---|---|
| [langgenius/dify](https://github.com/langgenius/dify) | 可视化搭 AI 应用：知识库、工作流、Agent、发布 API | 产品/运营也能上手的团队 | 低 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | LLM 应用开发的连接层，工具链最全 | 要写自定义逻辑的开发者 | 中 |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | LangChain 的可视化编排器，拖拽成流程 | 想快速验证想法的人 | 低 |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 深度文档理解的 RAG 引擎，复杂 PDF 解析强 | 做企业知识库的人 | 中 |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | 400+ 集成的自动化平台，原生支持 AI 节点 | 想把 AI 接进日常流程的人 | 低 |

## 图像 / 视频 / 语音生成

| 项目 | 一句话定位 | 适合谁 | 上手 |
|---|---|---|---|
| [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI) | 节点式图像生成工作流，SD 生态最强前端 | 想精细控制出图的人 | 中 |
| [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 最经典的 SD 网页界面，插件生态庞大 | 新手入门 | 低 |
| [openai/whisper](https://github.com/openai/whisper) | 语音转文字，多语言识别质量标杆 | 做会议纪要、字幕的人 | 低 |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Whisper 的加速实现，速度提升数倍 | 要批量转写的人 | 中 |
| [coqui-ai/TTS](https://github.com/coqui-ai/TTS) | 开源语音合成，多说话人、多语言 | 要做配音/朗读的人 | 中 |

## 值得关注的新势力

| 项目 | 说明 |
|---|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 2026 年爆红的本地个人 AI 助手，能接 50+ 聊天与办公集成、可自行扩展技能。**注意**：权限范围很大，装之前先看清它要访问哪些数据。 |

---

## 上手建议

1. **先 Ollama，再考虑其他的。** 显卡 8G 显存起步就能跑 7B 量化模型，先确认「本地 AI 到底能帮我干什么」，再决定要不要上 vLLM。
2. **RAG 的难点不在模型，在文档解析。** 大部分「知识库答得不准」其实是 PDF 里的表格和版式没解析对，这时候换 RAGFlow 比换模型有用。
3. **别为了用框架而用框架。** 一个提示词 + 一次函数调用能解决的事，不需要 LangChain。
