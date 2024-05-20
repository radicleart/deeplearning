#!/bin/bash

# Variables
model_name="llama3"
custom_model_name="crewai-llama3"

# Get base model
ollama pull $model_name

# Create the model file
ollama create $custom_model_name -f ./Llama3Modelfile
