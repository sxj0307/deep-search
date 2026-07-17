# Deep Search

一个基于多Agent架构的智能搜索系统，支持数据库查询、网络搜索和文档检索。

## 特性

- **多Agent架构**：智能协调多个子Agent处理不同类型的查询
- **数据库助手**：支持MySQL数据库查询和操作
- **网络查询助手**：集成搜索引擎进行互联网信息检索
- **RAGFlow助手**：基于RAGFlow的文档检索和问答
- **文件上传支持**：支持PDF、Excel、CSV等多种文件格式
- **实时监控**：通过WebSocket实时推送任务状态
- **RESTful API**：提供完整的API接口

## 项目结构

```
deep-search/
├── agent/              # Agent模块
│   ├── sub_agents/     # 子Agent
│   ├── llm.py         # LLM初始化
│   ├── load_prompt.py # Prompt加载
│   └── main_agent.py  # 主Agent
├── api/               # API模块
│   ├── context.py     # 会话上下文
│   ├── monitor.py     # WebSocket监控
│   └── server.py      # FastAPI服务
├── prompt/            # Prompt配置
│   └── prompts.yaml
├── tools/             # 工具模块
│   ├── internet_search_tool.py
│   ├── markdown_tools.py
│   ├── mysql_tools.py
│   ├── pdf_tools.py
│   ├── ragflow_tools.py
│   └── upload_file_read_tool.py
├── utils/             # 工具函数
│   ├── logger_utils.py
│   ├── path_utils.py
│   └── converter_utils.py
├── output/            # 输出目录
├── upload/            # 上传目录
└── .env               # 环境变量
```

## 快速开始

### 1. 环境要求

- Python 3.8+
- MySQL (可选)
- RAGFlow (可选)

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制`.env.example`为`.env`并填写实际配置：

```bash
cp .env.example .env
```

### 4. 运行服务

```bash
python -m api.server
```

服务将在 `http://localhost:8000` 启动。

## API文档

访问 `http://localhost:8000/docs` 查看自动生成的API文档。

## 使用示例

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

## 开发

### 项目依赖

```txt
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.0.0
python-dotenv>=1.0.0
PyYAML>=6.0
mysql-connector-python>=8.0.0
requests>=2.31.0
pandas>=2.0.0
```

### 代码风格

使用black和flake8进行代码格式化和检查：

```bash
black .
flake8 .
```

## 许可证

MIT License
