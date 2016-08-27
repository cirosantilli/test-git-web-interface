#!/usr/bin/env bash

set -e

# This was an attempt to calculate SHAs manually.
# It stopped halfway because Bash cannot store NUL characters in variables,
# so we had to move to Python.

. commit-meta.bashrc
. init.bashrc

# Directory parameters.
blob_content='blob content'
blob_name='file'
blob_mode='100644'
dir_name='directory'

strlen() {
  printf "$1" | wc -c
}

sha_calc() {
  type="$1"
  content="$2"
  printf "${type} $(strlen "$content")\0${content}" | sha1sum
}

# Blob.
blob_sha="$(printf "$blob_content" | git hash-object --stdin -w)"
echo "$blob_sha"
echo "$(sha_calc "blob"  "$blob_content")"
echo

# Tree 1.
sub_tree_sha="$(printf "\
$blob_mode blob $blob_sha\t$blob_name
" | git mktree)"
echo "$sub_tree_sha"
# TODO the problem here is the null character
# which is impossible for bash to put into a variable.
echo "$(sha_calc "tree" "${blob_mode} ${blob_name}\0${blob_sha}")"
echo

# Tree 2.
root_tree="$(printf "\
040000 tree $sub_tree_sha\t$dir_name
100644 blob $blob_sha\t$blob_name
" | git mktree)"

commit="$(git commit-tree -m 0 "$root_tree")"
git branch master "$commit"

# Modify the master branch
root_tree="$((
git ls-tree HEAD:./
printf "\
100644 blob $blob_sha\tb
") | git mktree)"

commit="$(git commit-tree -m 1 -p "$(git rev-parse HEAD)" "$root_tree")"
# Bare
git update-ref master "$commit"
