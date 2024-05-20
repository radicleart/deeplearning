# Blog Posts

customer support automation.

## Findings

See [issue](https://github.com/aibtcdev/ai-agent-crew/issues/9).

This use case works with OpenAI and GPT 3.5 but fails trying to
run the model locally (macbook pro 32Gram and 6cpu) with Llama3 model

## Model

Using Ollama and Llama3 - see setup directory for ollama create scripts.

```bash
ollama run crewai-llama3
```

## Poetry Setup

Using latest versions as of 17/05/24.

CrewAI: 0.30.11

Setting up this environment;

```bash
poetry new customer_support_automation
poetry env info
poetry env use python3.12
vi pyproject.toml
  - python = ">=3.12,<=3.13"

# check latest versions and attempt to solve dependency errors
poetry search crewai
poetry search crewai[tools]

poetry add crewai crewai[tools]
poetry add langchain
poetry install
poetry shell
poetry show
```

Adding more dependencies;

```bash
```

Run project;

```bash
poetry run python src/crewai_project/main.py
```

Or add script to pyproject.toml

```bash
[tool.poetry.scripts]
customer_support_automation = "customer_support_automation.main:run"
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
