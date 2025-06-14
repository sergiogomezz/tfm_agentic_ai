import os
from config.loader import load_root_path

# General Info
PROJECT_NAME = "TFM_Agentic_AI"

# Model Settings
USE_LOCAL_MODEL = True

# For ollama client
LOCAL_MODEL_NAME = "llama3"
LOCAL_MAX_TOKENS = 512
LOCAL_TEMPERATURE = 0.7

# For OpenAI
OPENAI_MODEL_NAME = "gpt-4o-mini"
OPENAI_MAX_TOKENS = 1024
OPENAI_TEMPERATURE = 0.5

# Agents settings
ENABLE_DYNAMIC_AGENT_GENERATOR = True
MAX_AGENTS = 10

# Paths
ROOT_DIR = load_root_path()
AGENTS_DIR = os.path.join(ROOT_DIR, "agents")
PROMPTS_DIR = os.path.join(ROOT_DIR, "prompts")