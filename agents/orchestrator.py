import json

from config.config import AGENT_ORCHESTRATOR_PROMPT
from config.loader import load_prompt, save_output_json_orchestrator


class OrchestratorAgent:
    def __init__(self, client, task_id):
        self.client = client
        self.system_prompt = load_prompt(AGENT_ORCHESTRATOR_PROMPT)
        self.task_id = task_id

    def create_agents(self, subtask: dict):
        subtask_id = subtask["id"]
        prompt = json.dumps({
            "task_desc": self.task_id,
            "subtask_id": subtask["id"],
            "title": subtask["title"],
            "description": subtask["description"]
        }, indent=2)

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]

        response = self.client.chat(messages)

        response_parsed = save_output_json_orchestrator(response)

        return response_parsed