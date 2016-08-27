#!/usr/bin/env bash

set -e

# Try to create a commit with two times it's parent with git-commit-tree
# Outcome on Git 2.7: commit fails. Will try again with raw object creation from Python later on.

. commit-meta.bashrc
. init.bashrc

# Directory parameters.
blob_content=''
blob_name='a'
blob_mode='100644'
dir_name='directory'

# Blob.
blob_sha="$(printf "$blob_content" | git hash-object --stdin -w)"

# Tree.
tree_sha="$(printf "\
$blob_mode blob $blob_sha\t$blob_name
" | git mktree)"

# Commit 1.
commit_sha="$( \
  git commit-tree -m 0 "$tree_sha")"
git branch master "$commit_sha"

# Commit 2 that has the duplicate parent.
commit_sha="$(git commit-tree -m 1 -p "$commit_sha" -p "$commit_sha" "$tree_sha")"
git update-ref master "$commit_sha"
