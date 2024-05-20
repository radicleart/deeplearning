# Blog Posts

Write nice blog post about user provided topic.

## Models

Compare GPT 3.5 and Llama 7b local.

Findings: GPT ran for >20 mins and found;

```txt
> Finished chain.
 [DEBUG]: [Crew Manager] Task output: Here is a comprehensive risk analysis report detailing potential risks and mitigation recommendations for AAPL:

1. Scalping:
   - Risks: High transaction costs due to frequent trading, leverage, spreads, fees, and slippage. Effective risk management, trading discipline, and adaptability to market conditions are crucial.
   - Mitigation Strategies: Employ protective measures like stop orders, set stop losses, position sizing, risk/reward ratio, and implement a money management strategy.

2. Day Trading:
   - Risks: Market volatility, quick and substantial financial losses if the market moves in the wrong direction, multiple commission costs due to frequent trades, and high stress levels. Day trading is also not suitable for someone with limited resources and trading experience.
   - Mitigation Strategies: Find the right broker, set stop-loss and take-profit points, ensure all trades are closed in the overnight session, and diversify portfolio.

3. Swing Trading:
   - Risks: Exposure to market volatility, potential for massive losses, temptation to hold onto positions for too long, and the risk of overtrading, which can lead to increased transaction costs. Swing trading also carries the risk of missing out on profit potential from exiting too early.
   - Mitigation Strategies: Diversify investments across different sectors and asset types, trade smaller positions, use stop-loss orders, and understand leverage.

4. Position Trading:
   - Risks: Potential for large losses, exposure to long-term market risks, and the risk of sudden changes or reversals in asset prices. Position traders are also exposed to the risk of their positions experiencing significant losses if the market moves against them.
   - Mitigation Strategies: Plan trades, set stop-loss and take-profit points, diversify across different asset classes, and hedge.

5. Trade Execution Algorithms:
   - Risks: Errant algorithms, huge investor losses, loss of confidence in market integrity, poor algorithm performance, technology failures, susceptibility to technical errors, and cybersecurity threats. Despite these risks, algorithmic trading can be less prone to emotional bias and human errors.
   - Mitigation Strategies: Conduct stress evaluations, use multiple sources of data, real-time monitoring by experienced traders, and implement proper risk management practices.

These strategies should be tailored according to the individual trader's needs, market conditions, and risk tolerance. It's also important to remember that all trading involves risk, and these strategies do not guarantee profit but can help manage potential losses.
```

Llama3 findings, e.g;

## Learning Goals

Hierarchical models and manager llm's.

Note: in hierarchical crew the model is passed on crew instantiation rather then to individual agents.

## Poetry Setup

Using latest versions as of 17/05/24.

CrewAI: 0.30.11

Setting up this environment;

```bash
poetry new financial_analysis
poetry env info
poetry env use python3.12
vi pyproject.toml
  - python = ">=3.12,<=3.13"

# check latest versions and attempt to solve dependency errors
poetry search crewai
poetry search crewai[tools]

poetry add crewai crewai[tools]

poetry update
```

Adding more dependencies;

```bash
poetry add langchain
poetry show
```

Run project;

```bash
poetry run python src/crewai_project/main.py
```

Or add script to pyproject.toml

```bash
[tool.poetry.scripts]
financial_analysis = "financial_analysis.main:run"
```

Setup directory structure;

```image
crewai-project/
├── README.md
├── pyproject.toml
├── tests
│   └── __init__.py
└── src
    ├── crewai_project
    │   ├── __init__.py
    │   ├── main.py
    │   ├── crew.py
    │   ├── config
    │   │   ├── agents.yaml
    │   │   └── tasks.yaml
    │   └── tools
    │       └── custom_tool.py
```
