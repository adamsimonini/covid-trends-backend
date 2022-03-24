#!/bin/bash

read -p "Enter the commit description:" commit_description

git add .
sleep 0
git commit -m "$commit_description"
sleep 0
git push