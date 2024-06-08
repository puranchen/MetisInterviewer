import os
from langchain.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from archetypes import SymptomSigns

class ChatChain:
    def __init__(self, system_prompt, temperature=0, llm='gpt-3.5-turbo', structured_output=False, schema=SymptomSigns):
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.llm = llm
        self.structured_output = structured_output
        self.schema = schema
        self.prompt = self._create_prompt()
        self.model = self._create_model()
        self.output_parser = self._create_output_parser()
        self.api_key = self._load_api_key()

    def _create_prompt(self):
        return ChatPromptTemplate.from_messages(
            [
                ('system', self.system_prompt),
                MessagesPlaceholder(variable_name = 'chat_history')
            ]
        )
    
    def _create_model(self, llm='openai'):
        if llm == 'openai':
            OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
            return ChatOpenAI(model=self.llm, temperature=self.temperature, api_key=OPENAI_API_KEY)
        else:
            raise ValueError(f"{llm} api key is not available")

    def _create_output_parser(self):
        return StrOutputParser()
    
    def create(self):
        return (self.prompt | self.model.with_structured_output(schema=self.schema)) if self.structured_output else (self.prompt | self.model | self.output_parser)
    
__all__ = ['ChatChain']