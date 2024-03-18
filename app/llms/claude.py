import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
api_key = os.getenv('CLAUDE_API_KEY')
claude_client = anthropic.Anthropic(api_key=api_key)

base_prompt = "You are an SQL Expert. You are asked to write SQL queries based on the prompts given to you. Your response should be a valid SQL query."

def generate_claude_response(prompt: str, content_prompt: str='') -> str:
    if content_prompt:
        base_prompt = content_prompt
    print(f'claude content prompt: {content_prompt} | claude prompt: {prompt}')
    messages = [{"role": "user", "content": prompt}]
    response = claude_client.messages.create(model="claude-3-opus-20240229", max_tokens=300, system=base_prompt, messages=messages)
    return response.content[0].text
