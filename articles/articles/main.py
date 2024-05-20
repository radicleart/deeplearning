import os
from textwrap import dedent
from dotenv import load_dotenv
load_dotenv()
from .crew import ArticlesCrew
from IPython.display import Markdown

def run():
  print("## Welcome to Articles Crew")
  print('-------------------------------')
  topic = "civilian submarines"
  #input(
  #  dedent("""
  #    What is the topic you wish to write about?
  #  """))
  result = ArticlesCrew().crew().kickoff(inputs={"topic": topic})
  Markdown(result)
  
if __name__ == "__main__":
    run()