import configparser
from pathlib import Path

import yaml


def _load_config(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        config_dict=yaml.safe_load(f)
        return config_dict

_file_path=Path(__file__).parents[1]/"prompt/prompts.yaml"
_yaml_dict=_load_config(_file_path)

main_agent_config=_yaml_dict["main_agent"]

sub_agents_config=_yaml_dict["sub_agents"]

if __name__=="__main__":
    print(main_agent_config)
    print(sub_agents_config)