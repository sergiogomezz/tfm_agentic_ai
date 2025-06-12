import json
import openai

with open('keys.json', 'r') as f:
    keys = json.load(f)

# Extraer la clave de OpenAI
openai_api_key = keys.get('openai_api_key')

if not openai_api_key:
    raise ValueError("La clave 'openai_api_key' no se encontró en keys.json.")

openai.api_key = openai_api_key