# Deep Learning

Inspired by thy CrewAI / DeeplearningAI [course](https://learn.deeplearning.ai/courses/multi-ai-agent-systems-with-crewai/lesson/1/introduction) and the
Bitcoin AI X [working group](https://github.com/orgs/stacks-network/discussions/531).

This repo contains the example from the course with the following changes;

- examples updated to latest CrewAI release (0.30.11)
- uses poetry for python package and running
- uses yaml for agent and task configuration
- extends the original course material - stacks-automation-experiment1 contains simple crew running via http rest api.

## Contents

Repository contents are

### Setup

Setup directory contains scripts and model files for creating and running models locally using Ollama

### Research Directory

Contains ChatGPT related research, a quick reference.

### Other Directories

Contain example crews including the original set from the course - see individual readme docs for more info.

## Directory Structure

```txt
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
