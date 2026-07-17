# LLM初始化模块
# 负责初始化和管理LLM实例
import os

import dotenv
from langchain.chat_models import init_chat_model

dotenv.load_dotenv()

llm=init_chat_model(
    model=os.getenv("LLM_MODEL"),
    model_provider="openai",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
)