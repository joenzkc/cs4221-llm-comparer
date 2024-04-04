import anthropic
from .BaseLLM import BaseLLM

base_prompt = "You are an SQL Expert. You are asked to write SQL queries based on the prompts given to you. Your response should be a valid SQL query."

class ClaudeClient(BaseLLM):
    def __init__(
            self, 
            key: str, 
            base_prompt: str='',
            model: str="claude-3-opus-20240229"
        ):
        super().__init__('Claude', key, base_prompt)
        self.model = model
        self.client = anthropic.Anthropic(api_key=key)
    
    def generate_response(self, prompt: str, content_prompt: str='', **kwargs) -> str:
        messages = [{"role": "user", "content": prompt}]
        response = self.client.messages.create(
            model=self.model, 
            max_tokens=300, 
            system=content_prompt if content_prompt else self.base_prompt, 
            messages=messages,
            **kwargs
        )
        return response.content[0].text
    
    def __repr__(self):
        return f'<Claude {self.model}>'
    
# def generate_claude_response(prompt: str, content_prompt: str='') -> str:
#     print(f'claude content prompt: {content_prompt} | claude prompt: {prompt}')
#     messages = [{"role": "user", "content": prompt}]
#     response = claude_client.messages.create(
#         model="claude-3-opus-20240229", 
#         max_tokens=300, 
#         system=content_prompt if content_prompt else base_prompt, 
#         messages=messages
#     )
#     return response.content[0].text
