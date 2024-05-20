# Blog Posts

Write nice blog post about user provided topic.

## Models

Compare GPT 3.5 and Llama 7b local.

Findings: GPT ran to completion finding,e.g;

```txt
Thought:
The Data Analyst has provided the current stock price, trading volume, and recent news for AAPL. Now, I need to delegate the task of using statistical modelling and machine learning to identify trends to the Trading Strategy Developer.
```

Note: in hierarchical crew the model is passed on crew instantiation rather then to individual agents.

## Learning Goals

Hierarchical models and manager llm's.

## Poetry Setup

Using latest versions as of 17/05/24.

CrewAI: 0.30.11

Setting up this environment;

```bash
poetry new tailor_job_applications
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
tailor_job_applications = "tailor_job_applications.main:run"
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
