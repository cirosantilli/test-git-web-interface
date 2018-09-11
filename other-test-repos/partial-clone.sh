#!/usr/bin/env bash

# https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository/52269934#52269934
rm -rf partial-clone.tmp
mkdir -p partial-clone.tmp
cd partial-clone.tmp

#!/usr/bin/env bash
set -eu

list-objects() (
  git rev-list --all --objects
  echo "master commit SHA: $(git log -1 --format="%H")"
  echo "mybranch commit SHA: $(git log -1 --format="%H")"
  git ls-tree master
  git ls-tree mybranch | grep mybranch
  git ls-tree master~ | grep root
)

# Reproducibility.
export GIT_COMMITTER_NAME='a'
export GIT_COMMITTER_EMAIL='a'
export GIT_AUTHOR_NAME='a'
export GIT_AUTHOR_EMAIL='a'
export GIT_COMMITTER_DATE='2000-01-01T00:00:00+0000'
export GIT_AUTHOR_DATE='2000-01-01T00:00:00+0000'

rm -rf server_repo local_repo
mkdir server_repo
cd server_repo

# Create repo.
git init --quiet
git config --local uploadpack.allowfilter 1
git config --local uploadpack.allowanysha1inwant 1

# First commit.
# Directories present in all branches.
mkdir d1 d2
printf 'd1/a' > ./d1/a
printf 'd1/b' > ./d1/b
printf 'd2/a' > ./d2/a
printf 'd2/b' > ./d2/b
# Present only in root.
mkdir 'root'
printf 'root' > ./root/root
git add .
git commit -m 'root' --quiet

# Second commit only on master.
git rm --quiet -r ./root
mkdir 'master'
printf 'master' > ./master/master
git add .
git commit -m 'master commit' --quiet

# Second commit only on mybranch.
git checkout -b mybranch --quiet master~
git rm --quiet -r ./root
mkdir 'mybranch'
printf 'mybranch' > ./mybranch/mybranch
git add .
git commit -m 'mybranch commit' --quiet

echo "# List and identify all objects"
list-objects
echo

# Restore master.
git checkout --quiet master
cd ..

# Clone. Don't checkout for now, only .git/ dir.
# file:// shenanigans:
# https://stackoverflow.com/questions/47307578/how-to-shallow-clone-a-local-git-repository-with-a-relative-path
git clone --depth 1 --quiet --no-checkout --filter=blob:none "file://$(pwd)/server_repo" local_repo
cd local_repo

# List missing objects from master.
echo "# Missing objects after --no-checkout"
git rev-list --all --quiet --objects --missing=print
echo

echo "# Git checkout fails without internet"
mv ../server_repo ../server_repo.off
! git checkout master
echo

echo "# Git checkout fetches the missing directory from internet"
mv ../server_repo.off ../server_repo
git checkout master -- d1/
echo

echo "# Missing objects after checking out d1"
git rev-list --all --quiet --objects --missing=print
