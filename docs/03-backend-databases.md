# 后端与数据库

## 同类怎么选（先看结论）

| 你的场景 | 选它 | 理由 |
|---|---|---|
| 中小项目快速起 API | **FastAPI**（Python）/ **Hono**（Node） | 代码量最少，文档自动生成 |
| 要稳定、要生态、要招人 | **Spring Boot** | 国内后端岗位与生态最成熟 |
| 高并发微服务 | **Go + Gin** | 部署简单，内存占用低 |
| 要极致性能、能接受学习成本 | **Rust + Axum** | 无 GC，编译期排除大量问题 |
| 关系型数据库不确定 | **PostgreSQL** | 能扛住 90% 的场景，剩下 10% 也能靠扩展顶住 |
| 缓存/队列/排行榜 | **Redis** | 几乎无替代 |
| 单机、嵌入式、零运维 | **SQLite** | 一台机器一个文件，别小看它 |
| 向量检索（RAG 必备） | **Qdrant / Milvus** | 小规模用 Qdrant，大规模用 Milvus |
| 分析型查询、日志 | **ClickHouse** | OLAP 场景性能断层领先 |

---

## 语言与运行时

| 项目 | 一句话定位 | 适合谁 |
|---|---|---|
| [nodejs/node](https://github.com/nodejs/node) | JS 服务端运行时，生态最大 | 前端转全栈的第一站 |
| [denoland/deno](https://github.com/denoland/deno) | 默认安全、原生 TS 的运行时 | 想要更现代工具链的人 |
| [golang/go](https://github.com/golang/go) | 简单、快、部署省心的语言 | 做基础服务与 CLI |
| [rust-lang/rust](https://github.com/rust-lang/rust) | 内存安全 + 零成本抽象 | 愿意投入学习时间的人 |
| [python/cpython](https://github.com/python/cpython) | 数据与 AI 领域的通用语言 | 所有人（尤其做 AI） |
| [oven-sh/bun](https://github.com/oven-sh/bun) | 打包 + 运行时 + 测试一体，速度极快 | 想用一个工具干三件事 |

## Web 框架

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | 类型驱动的 Python API 框架，自动生成 OpenAPI 文档 | 做 AI 服务后端首选 |
| [django/django](https://github.com/django/django) | 全家桶式框架，后台管理开箱即用 | 内容型站点效率极高 |
| [spring-projects/spring-boot](https://github.com/spring-projects/spring-boot) | Java 企业级开发的标准答案 | 生态与招聘市场最稳 |
| [gin-gonic/gin](https://github.com/gin-gonic/gin) | Go 的高性能 HTTP 框架 | 上手快，中间件生态成熟 |
| [tokio-rs/axum](https://github.com/tokio-rs/axum) | Rust 异步 Web 框架，类型安全 | 学习曲线陡，性能好 |

## 数据库

| 项目 | 一句话定位 | 备注 |
|---|---|---|
| [postgres/postgres](https://github.com/postgres/postgres) | 最强开源关系型数据库，扩展生态惊人 | 有 pgvector 就能直接做向量检索 |
| [redis/redis](https://github.com/redis/redis) | 内存数据结构存储，缓存/队列/排行榜 | 注意许可证已变更，可用 Valkey 替代 |
| [sqlite/sqlite](https://github.com/sqlite/sqlite) | 嵌入式数据库，全世界部署量最大 | 单机应用、移动端、边缘计算首选 |
| [mongodb/mongo](https://github.com/mongodb/mongo) | 文档型数据库，schema 灵活 | 结构不固定的早期项目合适 |
| [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse) | 列式 OLAP 数据库，亿级聚合秒级返回 | 日志分析、埋点统计 |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | 分布式向量数据库，面向大规模检索 | RAG 大规模场景 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Rust 写的向量数据库，轻量好部署 | 中小规模 RAG 更划算 |
| [supabase/supabase](https://github.com/supabase/supabase) | 开源的 Firebase 替代，Postgres + 认证 + 存储 | 想快速出原型的全栈项目 |
| [prisma/prisma](https://github.com/prisma/prisma) | 类型安全的 ORM，迁移工具好用 | Node/TS 项目常用 |

---

## 上手建议

1. **默认选 PostgreSQL，除非你有明确理由。** JSON 字段、全文检索、向量检索它都能干，少一个组件就少一个故障点。
2. **别在项目第一天就上 Kubernetes。** 一台 4C8G 的机器 + Docker Compose，能撑到绝大多数产品的第一个十万用户。
3. **ORM 会骗你。** 出现慢查询时，老老实实看 `EXPLAIN`，不要相信 ORM 生成的 SQL 一定合理。
