#!/usr/bin/env bash

while read repo; do
    git clone $repo
done < repo_list.txt