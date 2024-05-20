# Stacks Automation Experiment1

Goals here are a minimal integration between CrewAI and Stacks that extends the other
use cases in this repo by wrapping CrewAI in a REST API. I.e. we want our Stacks Crew to be powered by an
http get/post request and to return data in json format to the client (in this case
a nodejs express application).

The objective is the integration with an external service and so the crew needs to be able to
run on a small llm, for local testing.

Kickoff the crew;

```bash
curl -X POST http://127.0.0.1:5000/kickoff -H "Content-Type: application/json" -d '{      "customer": "Zest Protocol","person": "Mike C.","inquiry": "I need help with applying for a Stacks Critical Bounty. Can you please provide me with 3 examples of past bounties? Can you provide your answer in json format including the title of the bounty and a link to the full critical bounty application?"}'

curl -X POST http://127.0.0.1:5000/kickoff -H "Content-Type: application/json" -d '{"customer": "Uasu Industries","person": "Mike C.","inquiry": "Please provide any information you cann about the residency program offered by the Stacks Foundation"}'

```

## Models

Llama:8b - running on mac book pro.

## Poetry Setup

Using latest versions as of 17/05/24.

CrewAI: 0.30.11

Setting up this environment;

```bash
poetry new stacks_automation_experiment1
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
poetry add flask
poetry show
```

Run project;

```bash
poetry run python src/crewai_project/main.py
```

Or add script to pyproject.toml

```bash
[tool.poetry.scripts]
stacks_automation_experiment1 = "stacks_automation_experiment1.main:run"
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
