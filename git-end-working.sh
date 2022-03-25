#!/bin/bash

read -p "Please confirm you are done your work for now [y/n]? " work_complete_confirmation
if [[ $work_complete_confirmation =~ ^[Yy]$ ]]
then
    echo
    echo "Showing you the 'git status' below ..."
    echo
    git status
    read -p "Would you like to add these changes to the commit [y/n]? " add_changes_confirmation
    if [[ $add_changes_confirmation =~ ^[Yy]$ ]]
    then
        echo
        echo "adding changes ..."
        echo
        git add .
        read -p "Would you like to commit these changes now [y/n]? " commit_confirmation
        if [[ $commit_confirmation =~ ^[Yy]$ ]]
        then
            echo
            read -p "Please provide a comment for this commit now: " commit_description
            echo "commiting changes now ..."
            echo
            git commit -m "$commit_description"
            read -p "Would you like to push these changes now [y/n]? " push_confirmation
            if [[ $push_confirmation =~ ^[Yy]$ ]]
            then
                echo
                echo "Creating upstream branch if not created and pushing ..."
                branch_name="$(git branch | sed -n -e 's/^\* \(.*\)/\1/p')"
                echo "Pushing changes now ..."
                echo
                git push --set-upstream origin "$branch_name"
                echo "Changes pushed successfully!"
                echo "Checking out main branch now ..."
                git checkout main
            fi
        fi
    fi
fi