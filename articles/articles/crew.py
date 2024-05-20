from crewai import Agent, Task, Process, Crew
from crewai.project import CrewBase, agent,crew, task
from langchain_openai import ChatOpenAI

@CrewBase
class ArticlesCrew():
    """Article crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    
    def __init__(self) -> None:

        self.groq_llm = ChatOpenAI(
            temperature=0,
            model_name="crewai-llama3",
            base_url="http://localhost:11434/v1",
            api_key="NA"
        )
    
    @agent
    def planner(self) -> Agent:
        print(self.agents_config['planner'])
        return Agent(
            config = self.agents_config['planner'],
            allow_delegation=False,
	        verbose=True,
            llm = self.groq_llm
        )
        
    @agent
    def writer(self) -> Agent:
        print(self.agents_config['writer'])
        return Agent(
            config = self.agents_config['writer'],
            allow_delegation=False,
	        verbose=True,
            llm = self.groq_llm
        )
        
    @agent
    def editor(self) -> Agent:
        return Agent(
            config = self.agents_config['editor'],
            allow_delegation=False,
	        verbose=True,
            llm = self.groq_llm
        )
    
    @task
    def plan(self) -> Task:
        return Task(
            config = self.tasks_config['plan'],
            agent = self.planner()
        )
    
    @task
    def write(self) -> Task:
        return Task(
            config = self.tasks_config['write'],
            agent = self.writer(),
        )
    
    @task
    def edit(self) -> Task:
        return Task(
            config = self.tasks_config['edit'],
            agent = self.editor(),
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the new StacksCrew"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2
        )