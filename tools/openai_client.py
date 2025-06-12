import openai

# esto va a haber que cambiarlo porque es demasiado simple

class OpenAIClient:
    def __init__(self, api_key, default_model='gpt-4o-mini'):
        openai.api_key = api_key
        self.default_model = default_model

    def chat(self, prompt, model=None):
        used_model = model if model else self.default_model

        response = openai.ChatCompletion.create(
            model=used_model,
            messages=prompt
        )
        return response['choices'][0]['message']['content']
