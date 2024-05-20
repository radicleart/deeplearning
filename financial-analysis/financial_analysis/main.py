import os
from textwrap import dedent
from dotenv import load_dotenv
load_dotenv()
from .crew import FinancialAnalysisCrew
from IPython.display import Markdown

def run():
  print("## Welcome to FinancialAnalysis Crew")
  print('-------------------------------')
  financial_trading_inputs = {
    'stock_selection': 'AAPL',
    'initial_capital': '100000',
    'risk_tolerance': 'Medium',
    'trading_strategy_preference': 'Day Trading',
    'news_impact_consideration': True
  }
  result = FinancialAnalysisCrew().crew().kickoff(inputs=financial_trading_inputs)
  Markdown(result)
  
if __name__ == "__main__":
    run()