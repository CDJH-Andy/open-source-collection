# 后端（深度版）

> 目标：**一个人能扛起一个能上线的服务**——接口、数据、鉴权、部署、监控，五件套闭环。

## 一、主线三件套

| 层 | 选它 | 为什么 |
|---|---|---|
| 框架 | **FastAPI**（Python）/ **Hono**（Node/TS） | 代码量最少，OpenAPI 文档自动生成 |
| 数据库 | **PostgreSQL** | 关系型 + JSON + 全文检索 + 向量，一个顶四个 |
| 部署 | **Docker + Caddy** | 容器化 + 自动 HTTPS，两台命令上线 |

```bash
# 一个能跑的最小服务
pip install fastapi uvicorn
uvicorn main:app --reload
```

## 二、语言与框架怎么选

| 场景 | 组合 | 理由 |
|---|---|---|
| 快速起 API、做 AI 服务后端 | Python + FastAPI | 类型提示 + Pydantic 校验 + 自动文档 |
| 前端同学做全栈 | TypeScript + Hono / Next.js Route Handlers | 一套语言，类型共享 |
| 企业级、要招人 | Java + Spring Boot | 生态与岗位最稳 |
| 高并发、部署简单 | Go + Gin | 单二进制，内存占用低 |
| 极致性能 | Rust + Axum | 编译期排错，无 GC |

## 三、数据层

| 项目 | 用途 | 关键点 |
|---|---|---|
| [postgres/postgres](https://github.com/postgres/postgres) | 主库 | 默认选它，别犹豫 |
| [redis/redis](https://github.com/redis/redis) | 缓存、限流、排行榜 | 许可证已变更，可用 [valkey-io/valkey](https://github.com/valkey-io/valkey) |
| [pgvector/pgvector](https://github.com/pgvector/pgvector) | 向量检索扩展 | RAG 小规模场景不用另装数据库 |
| [drizzle-team/drizzle-orm](https://github.com/drizzle-team/drizzle-orm) | 类型安全 ORM（TS） | SQL 风格，迁移透明 |
| [prisma/prisma](https://github.com/prisma/prisma) | ORM（TS） | 上手最快，复杂查询要绕 |
| [sqlalchemy/sqlalchemy](https://github.com/sqlalchemy/sqlalchemy) | Python ORM | 生态成熟，异步支持已完善 |

## 四、接口与集成

| 项目 | 用途 |
|---|---|
| [OAI/OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification) | 接口契约，前后端并行开发的基准 |
| [trpc/trpc](https://github.com/trpc/trpc) | TS 端到端类型安全，不写 REST 样板 |
| [taskforcesh/bullmq](https://github.com/taskforcesh/bullmq) | 队列：发邮件、跑转码、跑 AI 任务 |
| [nats-io/nats-server](https://github.com/nats-io/nats-server) | 轻量消息系统，比 Kafka 好维护 |
| [keycloak/keycloak](https://github.com/keycloak/keycloak) | 单点登录与权限，企业项目绕不开 |
| [nextauthjs/next-auth](https://github.com/nextauthjs/next-auth) | Next.js 认证，接第三方登录最快 |

## 五、部署与运维

| 项目 | 用途 | 备注 |
|---|---|---|
| [moby/moby](https://github.com/moby/moby) | 容器运行时 | 一切从 Dockerfile 开始 |
| [caddyserver/caddy](https://github.com/caddyserver/caddy) | 反向代理 + 自动 HTTPS | 配置比 Nginx 少一个量级 |
| [traefik/traefik](https://github.com/traefik/traefik) | 云原生反代，自动发现服务 | 多服务编排时更顺 |
| [coollabsio/coolify](https://github.com/coollabsio/coolify) | 自建 PaaS，类似迷你 Vercel | 自托管部署很省心 |
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | 自建 Git + Actions | 私有代码托管 |
| [open-telemetry/opentelemetry-collector](https://github.com/open-telemetry/opentelemetry-collector) | 统一埋点与追踪 | 可观测性的标准入口 |
| [prometheus/prometheus](https://github.com/prometheus/prometheus) | 指标与告警 | 配 [grafana/grafana](https://github.com/grafana/grafana) 看板 |

## 六、安全底线

| 检查项 | 工具 |
|---|---|
| 依赖漏洞 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy) |
| 密钥泄露 | [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) |
| 镜像扫描 | Trivy（同一套，`trivy image`） |
| 接口限流 | 框架中间件 + Redis 计数器 |
| 备份 | [restic/restic](https://github.com/restic/restic) 定时全量 + 异地一份 |

## 七、学习路径（10 周）

| 周 | 内容 | 产出 |
|---|---|---|
| 1–2 | HTTP、状态码、REST 语义 | 用 FastAPI/Hono 写 5 个接口 |
| 3 | 数据库基础：范式、索引、事务 | 设计并建出业务表 |
| 4 | 认证鉴权：Session/JWT/OAuth | 接入登录，区分角色 |
| 5 | 文件上传与对象存储 | 图片上传 + 缩略图 |
| 6 | 队列与异步任务 | 一个后台任务队列 |
| 7 | 缓存与性能 | 接口 P95 降到 100ms 内 |
| 8 | Docker 化与部署 | 上线一个可访问服务 |
| 9 | 日志与监控 | 接 Prometheus + Grafana |
| 10 | 安全与备份 | 跑通 Trivy + restic 恢复演练 |

## 八、闭源替代关系

| 商业方案 | 开源对应 | 差距 |
|---|---|---|
| AWS RDS | 自建 PostgreSQL + restic 备份 | 高可用要自己搭 |
| Auth0 | Keycloak / Supabase Auth | 控制台体验差一些 |
| Datadog | Prometheus + Grafana + OTel | 需要自己维护采集端 |
| Vercel | Coolify / Dokku | 边缘网络没有替代品 |

## 九、三条经验

1. **数据库设计错了，后面全是补丁。** 上线前把表关系和索引过一遍，比任何架构优化都值。
2. **先单体，后拆分。** 一个进程 + 一个数据库能撑很久，微服务是规模问题不是技术问题。
3. **备份要演练恢复。** 没恢复过的备份，等于没有备份。
