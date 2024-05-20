#!/bin/bash

# Variables
model_name="mixtral-8x7b-32768"
custom_model_name="crewai-mixtral"

# Get base model
ollama pull $model_name

# Create the model file
ollama create $custom_model_name -f ./MixtralModelfile
