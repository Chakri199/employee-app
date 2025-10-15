#!/bin/bash

# Navigate to project directory
cd ~/employee-app || exit

# Add all changes
git add .

# Commit with timestamp
commit_message="Auto update on $(date '+%Y-%m-%d %H:%M:%S')"
git commit -m "$commit_message"

# Push changes to GitHub
git push origin master

echo "✅ Changes pushed to GitHub successfully at $(date)"
