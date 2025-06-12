from config.loader import load_keys
from tools.openai_client import OpenAIClient

class MyAgent:
    def __init__(self):
        keys = load_keys()
        self.client = OpenAIClient(api_key=keys['openai_api_key'])

    def run(self):
        response = self.client.chat("Hola, ¿qué tal?")
        print("Respuesta del agente:", response)
