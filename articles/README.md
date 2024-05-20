# Blog Posts

Write nice blog post about user provided topic.

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
poetry new articles
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
articles = "articles.main:run"
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
