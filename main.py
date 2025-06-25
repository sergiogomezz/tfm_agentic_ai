from config import config as cfg
from config.loader import load_keys, get_api_key, load_json
from tools.utils import landing_intro, loading_animation

from clients.openai_client import OpenAIClient
from clients.ollama_client import LocalLLMClient

from agents.task_specifier import TaskSpecifierAgent
from agents.task_divider import TaskDividerAgent
from agents.task_evaluator import TaskEvaluatorAgent
from agents.orchestrator import OrchestratorAgent


def main():

    # Improvement: Select diff model to each agent

    if cfg.USE_LOCAL_MODEL:
        client = LocalLLMClient(model=cfg.LOCAL_MODEL_NAME)

    else:
        keys = load_keys()
        api_key = get_api_key(keys)
        client = OpenAIClient(api_key=api_key, model=cfg.OPENAI_MODEL_NAME)

    landing_intro()

    first_user_input = input('What do you want to do? ')

    stop = loading_animation()

    try:
        # Invoke (1) Specifier Agent
        specifier_agent = TaskSpecifierAgent(client=client)
        specifier_agent_result = specifier_agent.specify_task(first_user_input)

        # Invoke (2) Divider Agent
        divider_agent = TaskDividerAgent(client=client)
        divider_agent_result = divider_agent.divide_tasks(specifier_agent_result)

        # Invoke (3) Evaluator Agent
        evaluator_agent = TaskEvaluatorAgent(client=client)
        subtasks_path = evaluator_agent.evaluate_tasks(divider_agent_result)


        # Get Each Subtask and Invoke (4) an Agent Orchestrator for each one
        subtasks = load_json(subtasks_path)

        task_id = subtasks["task_desc"]
        subtasks = subtasks["subtasks"]

        # ACORDARSE DE RESPETAR EL ORDEN DE SUBTASKS

        for subtask in subtasks:
            orchestrator = OrchestratorAgent(client=client, task_id=task_id)
            subtask_result = orchestrator.create_agents(subtask)

        









        print("\nAgents have finished their work! ENJOY THE RESULT 😎\n")
    
    except Exception as e:
        print(f"\nAgents were not too accurate this time 😔\nError: {e}")

    finally:
        stop()


if __name__ == "__main__":
    main()