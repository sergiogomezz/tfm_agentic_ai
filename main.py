from agents.task_specifier import TaskSpecifierAgent
from config.loader import load_keys
from tools.openai_client import OpenAIClient

def main():
    keys = load_keys()
    api_key = keys.get('openai_api_key')

    if not api_key:
        raise ValueError("API key not found in keys.json")
    
    client = OpenAIClient(api_key=api_key)
    agent = TaskSpecifierAgent(client)

    user_input = input('What do you want to do? ')
    result = agent.specify_task(user_input)

    print("\n Task Specified:")
    print(result)

if __name__ == "__main__":
    main()
