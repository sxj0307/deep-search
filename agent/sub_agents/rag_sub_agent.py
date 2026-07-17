from langchain.agents import create_agent

from agent.load_prompt import sub_agents_config
from tools.ragflow_tools import create_ask_delete, get_assistant_list

rag_sub_agent={
    "name": sub_agents_config["ragflow"]["name"],
    "description": sub_agents_config["ragflow"]["description"],
    "system_prompt": sub_agents_config["ragflow"]["system_prompt"],
    "tools":[create_ask_delete,get_assistant_list]
}