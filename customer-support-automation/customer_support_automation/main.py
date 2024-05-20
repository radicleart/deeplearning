from textwrap import dedent
from .crew import CustomerSupportAutomationCrew
from IPython.display import Markdown

def run():
  print("## Welcome to Customer Support Automation Crew")
  print('-------------------------------')
  inputs = {
      "customer": "Authogonal",
      "person": "Mike C.",
      "inquiry": "I need help with setting up a Crew "
                "and kicking it off, specifically "
                "how can I add memory to my crew? "
                "Can you provide guidance?"
  }
  result = CustomerSupportAutomationCrew().crew().kickoff(inputs=inputs)
  Markdown(result)
  
if __name__ == "__main__":
    run()