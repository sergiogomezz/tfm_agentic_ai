import json
import os
from config.loader import load_keys
from tools.openai_client import OpenAIClient


class TaskSpecifierAgent:
    def __init__(self, client, model='gpt-4o-mini'):
        self.client = client
        self.system_prompt = self._load_prompt()


    def _load_prompt(self):
        prompt_path = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'task_specifier_prompt.txt')

        with open(prompt_path, 'r') as f:
            return f.read()
        

    def specify_task(self, user_prompt):
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        response = self.client.chat(messages)
        
        try:
            parsed_output = json.loads(response.strip())
            return parsed_output
        except json.JSONDecodeError:
            print("Warning: Could not parse the response as JSON.")
            return {"raw_response": response}
        