from abc import ABC, abstractmethod

BASEPROMPT = ("You are an SQL Expert. "
              "You are asked to write SQL queries "
              "based on the prompts given to you. "
              "Your response should be a valid SQL query.")

class BaseLLM(ABC):
    def __init__(self, llm: str, key: str, base_prompt: str=''):
        self.llm = llm
        self.base_prompt = base_prompt if base_prompt else BASEPROMPT
        self.client = None
        self.__key = key
    
    @abstractmethod
    def generate_response(prompt: str, content_prompt: str='', **kwargs) -> str:
        pass
    
    def __repr__(self):
        return f'<{self.llm}>'
    
    