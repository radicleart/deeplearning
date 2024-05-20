import os
from textwrap import dedent
from dotenv import load_dotenv
load_dotenv()
from .crew import TailorJobApplicationsCrew
from IPython.display import Markdown, display

def run():
  print("## Welcome to tailor_job_applications Crew")
  print('-------------------------------')
  display(Markdown("./fake_resume.md"))
  job_application_inputs = {
    'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund',
    'github_url': 'https://github.com/joaomdmoura',
    'personal_writeup': """Noah is an accomplished Software
    Engineering Leader with 18 years of experience, specializing in
    managing remote and in-office teams, and expert in multiple
    programming languages and frameworks. He holds an MBA and a strong
    background in AI and data science. Noah has successfully led
    major tech initiatives and startups, proving his ability to drive
    innovation and growth in the tech industry. Ideal for leadership
    roles that require a strategic and innovative approach."""
  }
  result = TailorJobApplicationsCrew().crew().kickoff(inputs=job_application_inputs)
  Markdown(result)

if __name__ == "__main__":
    run()