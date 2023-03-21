#!/bin/bash
echo "Old Repo:" $1
echo "New Repo:" $2

git clone --mirror $1 repo.git
cd repo.git
git remote set-url origin $2
git push --mirror origin
cd ..
rm -rf repo.git

echo "Repo Migrated."

