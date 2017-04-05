#!/bin/bash

git add .
echo "Enter a commit message: "
read commitMessage
#echo hello $commitMessage
git commit -m $commitMessage

git push origin master

