#!/bin/bash

# Variables
model_name="llama3-70b"
custom_model_name="crewai-llama3-70b"

# Get base model
ollama pull $model_name

# Create the model file
ollama create $custom_model_name -f ./Llama370bModelfile
