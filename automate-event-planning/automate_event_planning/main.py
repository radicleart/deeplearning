import os
from textwrap import dedent
from dotenv import load_dotenv
load_dotenv()
from .crew import AutomateEventPlanningCrew
from IPython.display import Markdown
import json
from pprint import pprint

def run():
  print("## Welcome to Automate Event Planning Crew")
  print('-------------------------------')
  event_details = {
    'event_topic': "Tech Innovation Conference",
    'event_description': "A gathering of tech innovators "
                        "and industry leaders "
                        "to explore future technologies.",
    'event_city': "London",
    'tentative_date': "2024-09-15",
    'expected_participants': 50,
    'budget': 20000,
    'venue_type': "Conference Hall",
    'max_tokens': 500,
    'client_id': 'request_1234'
  }
  result = AutomateEventPlanningCrew().crew().kickoff(inputs=event_details)
  
  with open('venue_details.json') as f:
    data = json.load(f)

  pprint(data)
  
  Markdown(result)
  
if __name__ == "__main__":
    run()