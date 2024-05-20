from crewai import Agent, Task, Process, Crew
from crewai.project import CrewBase, agent,crew, task
from langchain_openai import ChatOpenAI
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
import os
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

@CrewBase
class FinancialAnalysisCrew():
    """FinancialAnalysis crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self) -> None:

        self.model = ChatOpenAI(
            temperature=0,
            model_name="crewai-llama3",
            base_url="http://localhost:11434/v1",
            api_key="NA"
        )
        #self.model = CustomChatModel(model_name="crewai-llama3", api_key="NA")

        #self.model = ChatOpenAI(openai_api_base=os.environ.get("OPENAI_API_BASE_URL", "https://api.openai.com/v1"),
        #                openai_api_key=os.environ.get("OPENAI_API_KEY"),
        #                temperature=0.1,
        #                model_name=os.environ.get("MODEL_NAME", "gpt-4")) #3.5-turbo
    
    @agent
    def data_analyst_agent(self) -> Agent:
        print(self.agents_config['data_analyst_agent'])
        return Agent(
            config = self.agents_config['data_analyst_agent'],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )
        
    @agent
    def trading_strategy_agent(self) -> Agent:
        print(self.agents_config['trading_strategy_agent'])
        return Agent(
            config = self.agents_config['trading_strategy_agent'],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )
        
    @agent
    def execution_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['execution_agent'],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )
    
    @agent
    def risk_management_agent(self) -> Agent:
        return Agent(
            config = self.agents_config['risk_management_agent'],
            verbose=True,
            allow_delegation=True,
            tools = [scrape_tool, search_tool]
        )
    
    @task
    def data_analysis_task(self) -> Task:
        return Task(
            config = self.tasks_config['data_analysis_task'],
            agent = self.data_analyst_agent()
        )
    
    @task
    def strategy_development_task(self) -> Task:
        return Task(
            config = self.tasks_config['strategy_development_task'],
            agent = self.trading_strategy_agent(),
        )
    
    @task
    def execution_planning_task(self) -> Task:
        return Task(
            config = self.tasks_config['execution_planning_task'],
            agent = self.execution_agent(),
        )
    
    @task
    def risk_assessment_task(self) -> Task:
        return Task(
            config = self.tasks_config['risk_assessment_task'],
            agent = self.risk_management_agent(),
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the new FinancialAnalysisCrew"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            manager_llm=self.model,
            process=Process.hierarchical,
            verbose = 2
        )