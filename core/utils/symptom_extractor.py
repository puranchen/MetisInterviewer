from langchain.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from archetypes import SymptomSigns

class NoteTaker:
    def __init__(self, system_prompt, llm='gpt-3.5-turbo', temperature=0):
        self.system_prompt = system_prompt
        self.llm = llm
        self.prompt = self._create_prompt()
        self.model = self._create_model()

    def _create_prompt(self):
        return ChatPromptTemplate.from_messages(
            [
                (
                    'system',
                    self.system_prompt
                ),
                MessagesPlaceholder(variable_name = 'chat_history')
            ]
        )
    
    def _create_model(self):
        return ChatOpenAI(
            model=self.llm,
            temperature=0
        )
    
    def create(self):
        return self.prompt | self.model.with_structured_output(schema=SymptomSigns)
    
__all__ = ['NoteTaker']