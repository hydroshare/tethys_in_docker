#!/usr/bin/env bash

if [  $# -eq 0 ]
then
    echo "No repo list given, reading default list (repo_list.txt)..."
    while read repo; do
        git clone $repo
    done < repo_list.txt
else
    while read repo; do
        git clone $repo
    done < $1
fi