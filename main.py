from config import config as cfg
from config.loader import load_keys, get_api_key
from clients.openai_client import OpenAIClient
from clients.ollama_client import LocalLLMClient

from agents.task_specifier import TaskSpecifierAgent
from agents.task_divider import TaskDividerAgent



def main():

    # Improvement: Select diff model to each agent

    if cfg.USE_LOCAL_MODEL:
        client = LocalLLMClient(model=cfg.LOCAL_MODEL_NAME)

    else:
        keys = load_keys()
        api_key = get_api_key(keys)
        client = OpenAIClient(api_key=api_key, model=cfg.OPENAI_MODEL_NAME)
    
    # Invoke (1) Specifier Agent 
    specifier_agent = TaskSpecifierAgent(client=client)

    first_user_input = input('What do you want to do? ')
    specifier_agent_result = specifier_agent.specify_task(first_user_input)

    print("\n Task Specified:")
    print(specifier_agent_result)

    # Invoke (2) Divider Agent
    divider_agent = TaskDividerAgent(client=client)

    divider_agent_result = divider_agent.divide_tasks(specifier_agent_result)

    print("\n Task Divided:")
    print(divider_agent_result)

if __name__ == "__main__":
    main()
