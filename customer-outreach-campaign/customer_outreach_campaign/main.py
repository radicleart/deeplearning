import os
from textwrap import dedent
from .crew import CustomerOutreachCampaignCrew
from IPython.display import Markdown

def run():
  print("## Welcome to Customer Support Automation Crew")
  print('-------------------------------')
  inputs = {
    "lead_name": "DeepLearningAI",
    "industry": "Online Learning Platform",
    "key_decision_maker": "Andrew Ng",
    "position": "CEO",
    "milestone": "product launch"
  }
  result = CustomerOutreachCampaignCrew().crew().kickoff(inputs=inputs)
  Markdown(result)
  
if __name__ == "__main__":
    run()