# agents/base_agent.py
class BaseAgent:
    def __init__(self, client, agent_id, agent_type, objective, prompt):
        self.client = client
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.objective = objective
        self.sys_prompt = prompt

    def run(self):
        sys_prompt = f"You are a {self.agent_type} agent. Your goal is to {self.sys_prompt}"
        
        messages = [
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": self.objective}
        ]
        return self.client.chat(messages)