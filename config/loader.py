import json

def load_keys(path='keys.json'):
    with open(path, 'r') as f:
        return json.load(f)
