from crewai import Agent, Task, Process, Crew
from crewai.project import CrewBase, agent,crew, task
from langchain_openai import ChatOpenAI
from crewai_tools import (
  FileReadTool,
  ScrapeWebsiteTool,
  MDXSearchTool,
  SerperDevTool
)

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()
read_resume = FileReadTool(file_path='./fake_resume.md')
semantic_search_resume = MDXSearchTool(mdx='./fake_resume.md')

@CrewBase
class TailorJobApplicationsCrew():
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
    def researcher(self) -> Agent:
        print(self.agents_config['researcher'])
        return Agent(
            config = self.agents_config['researcher'],
            tools = [scrape_tool, search_tool],
            verbose=True,
        )
        
    @agent
    def profiler(self) -> Agent:
        print(self.agents_config['profiler'])
        return Agent(
            config = self.agents_config['profiler'],
            tools = [scrape_tool, search_tool,
                    read_resume, semantic_search_resume],
            verbose=True,
        )
        
    @agent
    def resume_strategist(self) -> Agent:
        return Agent(
            config = self.agents_config['resume_strategist'],
            tools = [scrape_tool, search_tool,
                    read_resume, semantic_search_resume],
            verbose=True,
        )
    
    @agent
    def interview_preparer(self) -> Agent:
        return Agent(
            config = self.agents_config['interview_preparer'],
        tools = [scrape_tool, search_tool,
                read_resume, semantic_search_resume],
        verbose=True,
        )
    
    @task
    def research_task(self) -> Task:
        return Task(
            config = self.tasks_config['research_task'],
            agent=self.researcher(),
            async_execution=True
        )
    
    @task
    def profile_task(self) -> Task:
        return Task(
            config = self.tasks_config['profile_task'],
            agent=self.profiler(),
            async_execution=True
        )
    
    @task
    def resume_strategy_task(self) -> Task:
        return Task(
            config = self.tasks_config['resume_strategy_task'],
            agent=self.resume_strategist(),
            output_file="tailored_resume.md",
            context=[self.research_task(), self.profile_task()],
        )
    
    @task
    def interview_preparation_task(self) -> Task:
        return Task(
            config = self.tasks_config['interview_preparation_task'],
            agent=self.interview_preparer(),
            output_file="interview_materials.md",
            context=[self.research_task(), self.profile_task(), self.resume_strategy_task()],
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the new TailorJobApplications"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            manager_llm=self.model,
            process=Process.hierarchical,
            verbose = 2
        )