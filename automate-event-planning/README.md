# Blog Posts

automate_event_planning.

## Learning Goal

- converting output to json
- running tasks asynchronously
- human input

## Models

Comparing GPT 3.5, GPT 4 and Llama3:8b (Llama3:70b fails to run on local mac book).

GPT 4 performs best as expected. Various things can go wrong with 3.5 and Llama 3 locally fails to complete.

Saw this error from GPT models but can't see an easy way to avoid this in the [crewai framework, see](https://github.com/joaomdmoura/crewAI/issues/140);

```bash
Error code: 400 - {'error': {'message': "This model's maximum context length is 8192 tokens. However, your messages resulted in 9085 tokens. Please reduce the length of the messages.", 'type': 'invalid_request_error', 'param': 'messages', 'code': 'context_length_exceeded'}}
```

## Poetry Setup

Using latest versions as of 17/05/24.

CrewAI: 0.30.11

Setting up this environment;

```bash
poetry new automate_event_planning
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
automate_event_planning = "automate_event_planning.main:run"
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
