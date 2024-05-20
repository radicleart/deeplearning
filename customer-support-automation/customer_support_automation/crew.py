from crewai import Agent, Task, Process, Crew
from crewai.project import CrewBase, agent,crew, task
from langchain_openai import ChatOpenAI
from crewai_tools import ScrapeWebsiteTool
import os
#from .custom_model import CustomChatModel

#from utils import get_openai_api_key

#openai_api_key = get_openai_api_key()
#os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'            
docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
)
                         
@CrewBase
class CustomerSupportAutomationCrew():
    """CustomerSupportAutomation crew """
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self) -> None:
        #self.model = ChatOpenAI(
        #    temperature=0,
        #    model_name="crewai-llama3",
        #    base_url="http://localhost:11434/v1",
        #    api_key="NA"
        #)
        #self.model = CustomChatModel(model_name="crewai-llama3", api_key="NA")

        self.model = ChatOpenAI(openai_api_base=os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1"),
                        openai_api_key=os.environ.get("OPENAI_API_KEY"),
                        temperature=0.1,                        
                        model_name=os.environ.get("MODEL_NAME", "gpt-3.5-turbo"),
                        top_p=0.3)

    @agent
    def support_agent(self) -> Agent:
        print(self.agents_config['support_agent'])
        return Agent(
            config = self.agents_config['support_agent'],
            allow_delegation=False,
	        verbose=True,
            #tools=[ScrapeWebsiteTool()],
            llm = self.model
        )
        
    @agent
    def support_quality_assurance_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['support_quality_assurance_agent'],
            allow_delegation=True,
	        verbose=True,
            llm = self.model
        )
    
    @task
    def inquiry_resolution(self) -> Task:
        return Task(
            config = self.tasks_config['inquiry_resolution'],
            agent = self.support_agent(),
            tools=[docs_scrape_tool],
        )
    
    @task
    def quality_assurance_review(self) -> Task:
        return Task(
            config = self.tasks_config['quality_assurance_review'],
            agent = self.support_quality_assurance_agent(),
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the new CustomerSupportAutomationCrew"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2,
            memory = True,
            #max_rpm = 2
        )