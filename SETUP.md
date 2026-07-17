# Deep Search 项目框架搭建完成

## 创建的文件和目录结构

```
deep-search/
├── agent/
│   ├── __init__.py
│   ├── sub_agents/
│   │   ├── __init__.py
│   │   ├── db_sub_agent.py
│   │   ├── internet_sub_agent.py
│   │   └── rag_sub_agent.py
│   ├── llm.py
│   ├── load_prompt.py
│   └── main_agent.py
├── api/
│   ├── __init__.py
│   ├── context.py
│   ├── monitor.py
│   └── server.py
├── prompt/
│   └── prompts.yaml
├── tools/
│   ├── __init__.py
│   ├── internet_search_tool.py
│   ├── markdown_tools.py
│   ├── mysql_tools.py
│   ├── pdf_tools.py
│   ├── ragflow_tools.py
│   └── upload_file_read_tool.py
├── utils/
│   ├── __init__.py
│   ├── logger_utils.py
│   ├── path_utils.py
│   └── converter_utils.py
├── output/
├── upload/
├── logs/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## 下一步操作建议

1. **配置环境变量**
   ```bash
   cp .env.example .env
   # 编辑.env文件，填写实际的API密钥和配置
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **启动服务**
   ```bash
   python -m api.server
   ```

4. **访问API文档**
   - 打开浏览器访问: `http://localhost:8000/docs`

## 核心模块说明

### Agent模块
- **MainAgent**: 主Agent，负责路由和协调子Agent
- **DBSubAgent**: 处理数据库相关查询
- **InternetSubAgent**: 处理网络搜索查询
- **RAGSubAgent**: 处理文档检索查询

### API模块
- **server.py**: FastAPI服务入口，提供RESTful API
- **context.py**: 使用ContextVars实现会话隔离
- **monitor.py**: WebSocket监控，实时推送任务状态

### Tools模块
- **internet_search_tool.py**: 搜索引擎集成
- **mysql_tools.py**: MySQL数据库操作
- **ragflow_tools.py**: RAGFlow API集成
- **pdf_tools.py**: PDF文件处理
- **markdown_tools.py**: Markdown文件生成
- **upload_file_read_tool.py**: 上传文件读取

### Utils模块
- **logger_utils.py**: 统一日志配置
- **path_utils.py**: 路径操作工具
- **converter_utils.py**: 文件格式转换

## 注意事项

1. 部分工具类（如MySQLTool、RAGFlowTool）需要配置相应的API密钥
2. 可以根据实际需求修改`prompts.yaml`中的Prompt模板
3. 建议在生产环境使用更安全的日志和错误处理机制
4. 考虑添加单元测试和集成测试
