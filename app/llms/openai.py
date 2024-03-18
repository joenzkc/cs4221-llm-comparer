from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')  # Use getenv instead of environ.get

client = OpenAI(api_key=api_key)

# Setup base prompt
base_prompt = {
    "role": "system", 
    "content": ("You are an SQL Expert. You are asked to write SQL"
                "queries based on the prompts given to you. Your "
                "response should be a valid SQL query.")
}

def generate_ai_response(prompt: str, content_prompt: str='') -> str:
    """
    args:
        prompt (str): String to send to openai endpoint
        content_prompt (str, optional): Custom base prompt content
    returns:
        str: Response in markdown from AI
    """
    messages = [{
        'role': 'system',
        'content': content_prompt
    } if content_prompt else base_prompt]
    print(f'openai content prompt: {content_prompt} | openai prompt: {prompt}')
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)  # Use ChatCompletion.create
    return response.choices[0].message.content
