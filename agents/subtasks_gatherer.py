# This agent serves to gather the results of the different agents
from config.config import AGENT_SUBTASK_GATHERER
from config.loader import load_prompt, parse_json


class SubtasksGatherer():
    def __init__(self, client):
        self.client = client
        self.system_prompt = load_prompt(AGENT_SUBTASK_GATHERER)

    def gather_subtasks(self):

        #leer los work_agent outputs

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": "AAAAAAAA"}
        ]

        response = self.client.chat(messages)

        response_parsed = parse_json(response)

        return response