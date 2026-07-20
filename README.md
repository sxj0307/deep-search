# Deep Search — 多 Agent 智能搜索系统

基于多 Agent 架构的智能搜索系统，协调三个子 Agent 分别处理数据库查询、网络搜索和文档检索任务。

## 架构

```
用户查询
    │
    ▼
 主 Agent (deepagents)
    │
    ├── 意图识别 + 任务分配
    │
    ▼
┌──────────────────┬───────────────────┬──────────────┐
│ DB Sub-Agent     │ Internet Sub-Agent│ RAG Sub-Agent│
│ (数据库查询)      │ (网络搜索)         │ (文档检索)    │
│                  │                   │              │
│ · SQL 生成执行    │ · Tavily 搜索      │ · RAGFlow     │
│ · MySQL 操作     │ · 网页内容提取     │ · 文档问答    │
└──────────────────┴───────────────────┴──────────────┘
    │
    ▼
 结果聚合 + 流式推送 (WebSocket)
```

## 技术栈

| 层面 | 技术 |
|------|------|
| Agent 框架 | deepagents |
| 推理 | LangChain + OpenAI 兼容 API |
| 数据库 | MySQL |
| 网络搜索 | Tavily Search API |
| 文档检索 | RAGFlow SDK |
| 文件处理 | PyPDF / python-docx / openpyxl / pandas |
| 服务框架 | FastAPI + WebSocket (SSE 实时推送) |
| 运行环境 | Python 3.12+ / uv |

## 项目结构

```
deep-search/
├── agent/                     # Agent 模块
│   ├── main_agent.py          # 主 Agent (deepagents 编排)
│   ├── llm.py                 # LLM 初始化
│   ├── load_prompt.py         # Prompt 加载
│   └── sub_agents/            # 子 Agent
│       ├── db_sub_agent.py         # 数据库查询子 Agent
│       ├── internet_sub_agent.py   # 网络搜索子 Agent
│       └── rag_sub_agent.py        # RAGFlow 文档检索子 Agent
├── api/                       # FastAPI 接口层
│   ├── server.py              # 应用启动 + 路由注册
│   ├── context.py             # 会话上下文管理
│   └── monitor.py             # WebSocket 实时状态推送
├── tools/                     # 工具模块
│   ├── mysql_tools.py              # MySQL 查询工具
│   ├── internet_search_tool.py     # 网络搜索工具
│   ├── ragflow_tools.py            # RAGFlow 检索工具
│   ├── upload_file_read_tool.py    # 上传文件读取
│   ├── pdf_tools.py                # PDF 处理
│   └── markdown_tools.py           # Markdown 转换
├── utils/                     # 工具函数
│   ├── logger_utils.py        # 彩色日志
│   ├── path_utils.py          # 路径管理
│   └── converter_utils.py     # 格式转换
├── prompt/                    # Prompt YAML 模板
│   └── prompts.yaml
├── sql/                       # SQL 脚本
├── output/                    # 输出目录
├── upload/                    # 文件上传目录
├── main.py                    # 启动入口
├── pyproject.toml
├── requirements.txt
└── SETUP.md                   # 详细安装指南
```

## 功能特性

- **多 Agent 协作** — 主 Agent 智能调度三个子 Agent 处理不同类型查询
- **数据库查询** — 自然语言转 SQL，支持 MySQL 读写操作
- **网络搜索** — 集成 Tavily 搜索引擎进行互联网信息检索
- **RAGFlow 检索** — 基于 RAGFlow 的文档检索和问答
- **多格式文件支持** — PDF、Excel、CSV、Word
- **WebSocket 实时推送** — 任务状态实时监控
- **RESTful API** — 完整的搜索和上传 API

## 快速开始

### 环境要求

- Python 3.12+
- MySQL (可选，用于数据库查询)
- RAGFlow (可选，用于文档检索)

### 安装

```bash
# uv (推荐)
uv sync

# 或 pip
pip install -r requirements.txt
```

### 配置

```bash
cp .env.example .env
# 编辑 .env 填写:
#   - LLM API Key / Base URL
#   - Tavily API Key
#   - MySQL 连接信息
#   - RAGFlow API 配置
```

### 运行

```bash
python -m api.server
# 或
python main.py
```

服务启动在 `http://localhost:8000`，API 文档在 `/docs`。

## API

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/api/search` | 多 Agent 搜索查询 |
| POST | `/api/upload` | 上传文件 |
| WS | `/ws/monitor` | WebSocket 任务状态推送 |

### 搜索查询

```bash
curl -X POST http://localhost:8000/api/search \
  -F "query=请帮我查找最新的AI新闻"
```

### 文件上传

```bash
curl -X POST http://localhost:8000/api/upload \
  -F "file=@/path/to/file.pdf"
```
