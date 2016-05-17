#!/usr/bin/env python3

"""
Create objects very manually to try and be faster than Git to generate large repos.
"""

import util

util.init()

# Directory parameters.
blob_content = b'a'
blob_basename = b'a'
blob_mode = b'100644'

# Commit parameters.
name = b'a'
email = b'a@a.com'
# 2000-01-01T00:00:00+0000
date = b'946684800 +0000'
author_date = date
author_email = email
author_name = name
committer_date = date
committer_email = email
committer_name = name
message = b'a'
# ASCII hex of parents.
parents = ()

# Blob.
blob_sha_ascii, blob_sha = util.save_object(b'blob', blob_content)
# Check sha matches Git.
blob_sha_git = util.get_git_hash_object(b'blob', blob_content)
assert blob_sha_ascii == blob_sha_git

# Tree.
tree_sha_ascii, tree_sha, tree_content = util.save_tree_object(blob_mode, blob_basename, blob_sha)
# Check sha matches Git.
tree_sha_git = util.get_git_hash_object(b'tree', tree_content)
assert tree_sha_ascii == tree_sha_git

# Commit.
commit_sha_ascii, commit_sha, commit_content = util.save_commit_object(
        tree_sha_ascii, parents,
        author_name, author_email, author_date,
        committer_name, committer_email, committer_date,
        message)
commit_sha_git = util.get_git_hash_object(b'commit', commit_content)
assert commit_sha_ascii == commit_sha_git

# Finish.
util.create_master(commit_sha_ascii)
util.clone()
