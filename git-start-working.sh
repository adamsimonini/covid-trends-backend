#!/bin/bash

read -p "Please confirm you are on the main branch [y/n]? " main_branch_confirmation
if [[ $main_branch_confirmation =~ ^[Yy]$ ]]
then
    echo
    echo "pulling any changes from main..."
    git pull
    read -p "Would you like to start a new branch [y/n]? " new_branch_confirmation
    if [[ $new_branch_confirmation =~ ^[Yy]$ ]]
    then
        echo
        read -p "Provide new branch name: " new_branch_name
        git checkout -b "$new_branch_name"
    fi
fi