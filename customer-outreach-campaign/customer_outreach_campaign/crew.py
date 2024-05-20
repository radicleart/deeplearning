from crewai import Agent, Task, Process, Crew
from crewai.project import CrewBase, agent,crew, task
from langchain_openai import ChatOpenAI
from crewai_tools import DirectoryReadTool, \
                         FileReadTool, \
                         SerperDevTool
from .tools.senitment_analysis_tool import SentimentAnalysisTool
import os

directory_read_tool = DirectoryReadTool(directory='./instructions')
file_read_tool = FileReadTool()
search_tool = SerperDevTool()
sentiment_analysis_tool = SentimentAnalysisTool()

@CrewBase
class CustomerOutreachCampaignCrew():
    """CustomerSupportAutomation crew """
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self) -> None:
        self.llm = ChatOpenAI(
            temperature=0,
            model_name="crewai-llama3",
            base_url="http://localhost:11434/v1",
            api_key="NA"
        )
        #self.llm = CustomChatModel(model_name="crewai-llama3", api_key="NA")

        #self.llm = ChatOpenAI(openai_api_base=os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1"),
        #                openai_api_key=os.environ.get("OPENAI_API_KEY"),
        #                temperature=0.1,                        
        #                model_name=os.environ.get("MODEL_NAME", "gpt-3.5-turbo"))

    @agent
    def sales_rep_agent(self) -> Agent:
        print(f"sales_rep_agent")
        print(self.agents_config['sales_rep_agent'])
        return Agent(
            config = self.agents_config['sales_rep_agent'],
            allow_delegation=False,
	        verbose=True,
            llm = self.llm
        )
        
    @agent
    def lead_sales_rep_agent(self) -> Agent:
        print(f"lead_sales_rep_agent")
        print(self.agents_config['lead_sales_rep_agent'])
        return Agent(
            config = self.agents_config['lead_sales_rep_agent'],
            allow_delegation=True,
	        verbose=True,
            llm = self.llm
        )
    
    @task
    def lead_profiling_task(self) -> Task:
        print(f"lead_profiling_task")
        print(self.tasks_config['lead_profiling_task'])
        return Task(
            config = self.tasks_config['lead_profiling_task'],
            tools=[directory_read_tool, file_read_tool, search_tool],
            agent = self.sales_rep_agent(),
        )
    
    @task
    def personalized_outreach_task(self) -> Task:
        print(f"personalized_outreach_task")
        print(self.tasks_config['personalized_outreach_task'])
        return Task(
            config = self.tasks_config['personalized_outreach_task'],
            tools=[sentiment_analysis_tool, search_tool],
            agent=self.lead_sales_rep_agent(),
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the new CustomerOutreachCampaignCrew"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2,
            memory = True,
            #max_rpm = 2
        )