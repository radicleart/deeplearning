from langchain.schema import BaseMessage, HumanMessage, AIMessage
from langchain.llms.base import LLM
import crewai

class CustomChatModel(LLM):
    def __init__(self, model_name: str, api_key: str = None):
        super().__init__()
        self.model_name = model_name
        self.api_key = api_key
        self.client = crewai.Client(api_key=api_key)

    def _call(self, prompt: str, stop=None):
        response = self.client.generate(
            model_name=self.model_name,
            prompt=prompt,
            stop=stop
        )
        return response['text']  # Adjust this line based on the actual response format from CrewAI

    async def _acall(self, prompt: str, stop=None):
        response = await self.client.agenerate(
            model_name=self.model_name,
            prompt=prompt,
            stop=stop
        )
        return response['text']  # Adjust this line based on the actual response format from CrewAI

    def call_model(self, messages: list):
        combined_prompt = "\n".join([msg.content for msg in messages])
        response_text = self._call(combined_prompt)
        return AIMessage(content=response_text)

    async def acall_model(self, messages: list):
        combined_prompt = "\n".join([msg.content for msg in messages])
        response_text = await self._acall(combined_prompt)
        return AIMessage(content=response_text)
    
    @property
    def _llm_type(self) -> str:
        return "custom_chat_model"
