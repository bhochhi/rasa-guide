#!/bin/bash

# Train the Rasa model
rasa train nlu --nlu nlu.yml

# Extract the latest model
python3.8 extract_model.py

# Change to the directory where your Git repository is located
cd /path/to/your/git/repo

# Add the extracted model to Git
git add current_model

# Commit the changes
git commit -m "Update model with latest training results"


