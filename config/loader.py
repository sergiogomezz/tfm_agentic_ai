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