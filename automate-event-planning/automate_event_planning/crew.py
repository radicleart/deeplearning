from crewai import Agent, Task, Process, Crew
from crewai.project import CrewBase, agent,crew, task
from langchain_openai import ChatOpenAI
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
import os
from .models.venue_details import VenueDetails

# Initialize the tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

@CrewBase
class AutomateEventPlanningCrew():
    """AutomateEventPlanning crew """
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
                        model_name=os.environ.get("MODEL_NAME", "gpt-4")) #3.5-turbo

    @agent
    def venue_coordinator(self) -> Agent:
        print(self.agents_config['venue_coordinator'])
        return Agent(
            config = self.agents_config['venue_coordinator'],
            tools=[search_tool, scrape_tool],
            verbose=True,
            llm = self.model
        )

    @agent
    def logistics_manager(self) -> Agent:
        print(self.agents_config['logistics_manager'])
        return Agent(
            config = self.agents_config['logistics_manager'],
            tools=[search_tool, scrape_tool],
            verbose=True,
            llm = self.model
        )

    #@agent
    def marketing_communications_agent(self) -> Agent:
        print(self.agents_config['marketing_communications_agent'])
        return Agent(
            config = self.agents_config['marketing_communications_agent'],
            tools=[search_tool, scrape_tool],
            verbose=True,
            llm = self.model
        )

    @task
    def venue_task(self) -> Task:
        return Task(
            config = self.tasks_config['venue_task'],
            agent=self.venue_coordinator(),
            human_input=True,
            output_json=VenueDetails,
            output_file="venue_details.json",  
            # Outputs the venue details as a JSON file
        )
        
    @task
    def logistics_task(self) -> Task:
        return Task(
            config = self.tasks_config['logistics_task'],
            human_input=True,
            async_execution=False,
            agent=self.logistics_manager()
        )
        
    #@task
    def marketing_task(self) -> Task:
        return Task(
            config = self.tasks_config['marketing_task'],
            async_execution=False,
            output_file="marketing_report.md",
            agent=self.marketing_communications_agent()
        )
        
    @crew
    def crew(self) -> Crew:
        """Creates the new AutomateEventPlanningCrew"""
        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.sequential,
            verbose = 2,
            memory = True,
            #max_rpm = 2
        )