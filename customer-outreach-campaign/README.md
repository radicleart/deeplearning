# Blog Posts

customer_outreach_campaign.

## Learning Goal

How to use custom tools

## Models

Compares GPT 3.5 and Llama3:8b.

Latter is run locally, see `setup` directory for ollama create scripts.

```bash
ollama run crewai-llama3
```

### Notes

The llama3:8b is unable to finish the task and gets stuck in loops.

## Poetry Setup

Using latest versions as of 17/05/24.

CrewAI: 0.30.11

Setting up this environment;

```bash
poetry new customer_outreach_campaign
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
customer_outreach_campaign = "customer_outreach_campaign.main:run"
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
