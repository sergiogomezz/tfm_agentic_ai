import json
import os

def load_keys(path='keys.json'):
    with open(path, 'r') as f:
        return json.load(f)
    

def get_api_key(keys):
    api_key = keys.get('openai', {}).get('api_key')

    if not api_key:
        raise ValueError("API key not found in keys.json")
    
    return api_key


def load_root_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(base_dir, ".."))
    return root_dir


def load_prompt(prompt_name):
    root_dir = load_root_path()
    prompts_dir = os.path.join(root_dir, "prompts")
    prompt_path = os.path.join(prompts_dir, prompt_name)
    with open(prompt_path, 'r') as f:
        return f.read()
    

def parse_json(response):
    try:
        parsed_output = json.loads(response.strip())
        return parsed_output
    except json.JSONDecodeError:
        print("Warning: Could not parse the response as JSON.")
        return response