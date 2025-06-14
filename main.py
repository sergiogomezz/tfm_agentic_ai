from agents.task_specifier import TaskSpecifierAgent
from config.loader import load_keys, get_api_key
from config import config as cfg
from clients.openai_client import OpenAIClient
from clients.ollama_client import LocalLLMClient


def main():
    if cfg.USE_LOCAL_MODEL:
        client = LocalLLMClient(model=cfg.LOCAL_MODEL_NAME)

    else:
        keys = load_keys()
        api_key = get_api_key(keys)
        client = OpenAIClient(api_key=api_key, model=cfg.OPENAI_MODEL_NAME)


    agent = TaskSpecifierAgent(client=client)

    user_input = input('What do you want to do? ')
    result = agent.specify_task(user_input)

    print("\n Task Specified:")
    print(result)

if __name__ == "__main__":
    main()
