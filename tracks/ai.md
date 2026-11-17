# AI（深度版）

> 目标：**让 AI 真的替你干活**，而不是收藏一堆框架。分三层：跑模型 → 搭应用 → 做训练。

## 一、主线三件套

| 层 | 选它 | 为什么 |
|---|---|---|
| 本地推理 | **Ollama** | 一条命令跑模型，模型管理省心 |
| 应用搭建 | **Dify** | 可视化 + 知识库 + API 发布，不写后端 |
| 图像工作流 | **ComfyUI** | 节点式可控，商业出图的主力 |

```bash
ollama run qwen3:8b          # 中文场景先试这个量级
docker compose up -d        # Dify 自托管
```

## 二、三层能力模型

| 层 | 你要解决的问题 | 需要的东西 |
|---|---|---|
| **跑模型** | 让模型在我机器上响应 | 推理引擎 + 显存 + 模型文件 |
| **搭应用** | 让模型接我的数据和流程 | RAG + 工作流 + 工具调用 |
| **做训练** | 让模型学会我的领域 | 数据 + 微调框架 + 评测 |

90% 的人只需要前两层。第三层在你有 5000 条以上高质量标注数据之前，性价比极低。

## 三、推理引擎

| 项目 | 定位 | 选它的理由 |
|---|---|---|
| [ollama/ollama](https://github.com/ollama/ollama) | 本地模型管理与服务 | 最省事，自带 OpenAI 兼容 API |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | C++ 推理引擎 | 量化格式标准，可深度调参 |
| [vllm-project/vllm](https://github.com/vllm-project/vllm) | 高吞吐服务 | 多人并发、生产部署 |
| [huggingface/transformers](https://github.com/huggingface/transformers) | 模型加载与微调 | 一切 HF 生态的入口 |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | 前端界面 | 给团队一个内网 ChatGPT |

## 四、应用与 Agent

| 项目 | 定位 | 什么时候用 |
|---|---|---|
| [langgenius/dify](https://github.com/langgenius/dify) | 可视化 AI 应用平台 | 团队里有人不写代码 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 开发框架，工具链最全 | 需要高度定制的逻辑 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | 有状态的 Agent 编排 | 多步任务、需要回退与重试 |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | 拖拽式流程编排 | 快速验证想法 |
| [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | 深度文档解析 RAG | 合同、财报、扫描件 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | 多智能体协作框架 | 需要多个角色分工 |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | 让 Agent 操作浏览器 | 自动填表、抓数据 |
| [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | 能写代码的 Agent | 自动化改代码、跑测试 |

## 五、RAG 全链路

| 环节 | 工具 | 关键经验 |
|---|---|---|
| 文档解析 | RAGFlow / [datalab-to/marker](https://github.com/datalab-to/marker) | 表格和版式解析决定上限 |
| 切分 | 语义切分优于定长切分 | 按标题层级切，保留上下文 |
| 向量库 | [qdrant/qdrant](https://github.com/qdrant/qdrant)、[pgvector/pgvector](https://github.com/pgvector/pgvector) | 10 万条以下 pgvector 够用 |
| 检索 | 混合检索（向量 + BM25） | 纯向量会漏关键词查询 |
| 重排 | [AnswerDotAI/rerankers](https://github.com/AnswerDotAI/rerankers) | 重排能把准确率拉高一档 |
| 评测 | 自己攒 100 条问答对 | 没有评测集的 RAG 是玄学 |

## 六、图像 / 视频 / 语音

| 项目 | 能做什么 | 备注 |
|---|---|---|
| [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI) | 节点式图像生成 | 可复用工作流，适合批量出图 |
| [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 经典 WebUI | 新手友好，插件多 |
| [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI) | 统一画布式生成 | 偏向设计师工作流 |
| [huggingface/diffusers](https://github.com/huggingface/diffusers) | 扩散模型库 | 自己写推理脚本时用 |
| [openai/whisper](https://github.com/openai/whisper) | 语音转写 | 字幕、会议纪要 |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Whisper 加速版 | 批量转写首选 |
| [coqui-ai/TTS](https://github.com/coqui-ai/TTS) | 语音合成 | 配音、朗读 |
| [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | 音视频处理 | 生成结果的后处理 |

## 七、训练与微调

| 项目 | 用途 |
|---|---|
| [huggingface/peft](https://github.com/huggingface/peft) | LoRA/QLoRA，消费级显卡也能微调 |
| [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | 一站式微调界面，中文文档好 |
| [unslothai/unsloth](https://github.com/unslothai/unsloth) | 训练加速，显存占用显著降低 |
| [huggingface/trl](https://github.com/huggingface/trl) | RLHF/DPO 等对齐训练 |
| [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 标准评测，避免"感觉变好了" |

## 八、学习路径

| 阶段 | 内容 | 时间 |
|---|---|---|
| 入门 | Ollama 跑通 3 个模型，理解参数量/量化/上下文 | 1 天 |
| 会用 | Dify 搭一个带知识库的问答机器人 | 2–3 天 |
| 调优 | 学会写系统提示词、调温度、做 few-shot | 1 周 |
| 深入 | RAG 全链路：解析、切分、混合检索、重排 | 2–3 周 |
| 生产 | vLLM 部署 + 并发压测 + 成本核算 | 1 周 |
| 训练 | LoRA 微调一个小模型，跑评测对比 | 2 周 |

## 九、闭源替代关系

| 商业方案 | 开源对应 | 差距 |
|---|---|---|
| ChatGPT / Claude | Ollama + Open WebUI | 模型能力有差距，但数据不出内网 |
| 各类 SaaS 知识库 | Dify + RAGFlow | 开箱体验略差，可控性强得多 |
| Midjourney | ComfyUI + SD 生态 | 出图审美需自己调，但可批量可复现 |
| 剪映自动字幕 | faster-whisper | 准确率接近，缺一键成片 |

## 十、三条经验

1. **本地模型先解决"有没有"，再谈"好不好"。** 8B 量化模型能跑起来，你就已经能判断哪些活值得交给 AI。
2. **RAG 效果差，八成是解析和切分的问题。** 换模型是最贵且最没用的解法。
3. **别在没有评测集的情况下调提示词。** 你会陷入"感觉这次更好了"的循环。
