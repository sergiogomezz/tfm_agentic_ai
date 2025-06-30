from config.loader import save_output_json_agents

class BaseWorkingAgent:
    def __init__(self, client, task_id, agent_id, subtask_id, agent_type, objective, prompt, context):
        self.client = client
        self.task_id = task_id
        self.subtask_id = subtask_id
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.objective = objective
        self.prompt = prompt
        self.context = context

    def work(self):
        sys_prompt = f"""You are a {self.agent_type} agent. Your goal is to {self.prompt}.
            The context from previous subtasks that you MUST take into account is {self.context}.
            You must respond in strict valid JSON format with the following structure:

            {{
                "task_desc": "{self.task_id}",
                "subtask_id": "{self.subtask_id}",
                "agent_id": "{self.agent_id}",
                "answer": <your detailed answer here as a string or structured object>
            }}"""

        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": self.objective}
        ]

        response = self.client.chat(messages)

        agents_path = save_output_json_agents(response)

        return agents_path