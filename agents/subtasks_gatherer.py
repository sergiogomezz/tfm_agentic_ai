# This agent serves to gather the results of the different agents
from config.config import AGENT_SUBTASK_GATHERER
from config.loader import load_prompt, parse_json, load_root_path

import os
import json


class SubtasksGatherer():
    def __init__(self, client):
        self.client = client
        self.system_prompt = load_prompt(AGENT_SUBTASK_GATHERER)

    def gather_subtasks(self, task_id):
        user_message = self.get_user_input_messages(task_id)
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message}
        ]
        final_output = self.client.chat(messages)
        return final_output


    def get_user_subtasks(self, task_id):
        root_path = load_root_path()
        base_path = f"{root_path}/outputs/{task_id}/work_agents"
        messages = []
        for agent_folder in sorted(os.listdir(base_path)):
            agent_path = os.path.join(base_path, agent_folder)
            if os.path.isdir(agent_path):
                json_files = [f for f in os.listdir(agent_path) if f.endswith(".json")]
                if json_files:
                    with open(os.path.join(agent_path, json_files[0]), "r") as f:
                        data = json.load(f)
                        answer = data.get("answer", "")
                        if isinstance(answer, dict):
                            formatted_answer = json.dumps(answer, indent=2, ensure_ascii=False)
                        else:
                            formatted_answer = str(answer)
                        messages.append(f"Subtask {agent_folder}:\n{formatted_answer}")

        return "\n\n".join(messages)