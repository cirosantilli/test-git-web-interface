#!/usr/bin/env bash
set -eu

# Reproducibility.
export GIT_COMMITTER_NAME='a'
export GIT_COMMITTER_EMAIL='a'
export GIT_AUTHOR_NAME='a'
export GIT_AUTHOR_EMAIL='a'
export GIT_COMMITTER_DATE='2000-01-01T00:00:00+0000'
export GIT_AUTHOR_DATE='2000-01-01T00:00:00+0000'

# https://stackoverflow.com/questions/600079/how-do-i-clone-a-subdirectory-only-of-a-git-repository/52269934#52269934
rm -rf filter-repo.tmp
mkdir -p filter-repo.tmp
cd filter-repo.tmp
git init

# Create repo.
git init --quiet

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
root_commmit_sha="$(git log -1 --format="%H")"

# Second commit only on master.
git rm --quiet -r ./root
mkdir 'master'
printf 'master' > ./master/master
printf 'd1/a' > ./d1/a2
git add .
git commit -m 'master commit' --quiet

# Third commit only on master.
printf 'd1/b' > ./d1/b2
git add .
git commit -m 'master commit' --quiet

# Second commit only on mybranch.
git checkout -b mybranch --quiet "$root_commmit_sha"
git rm --quiet -r ./root
mkdir 'mybranch'
printf 'mybranch' > ./mybranch/mybranch
git add .
git commit -m 'mybranch commit' --quiet

# Restore master.
git checkout --quiet master

# To easily compare with the original repo.
git remote add origin https://github.com/cirosantilli/test-git-filter-repository
git fetch
