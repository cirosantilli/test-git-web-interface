#!/usr/bin/env python3

"""
Create objects very manually. Goals:

- learn the object file
- be faster than Git to generate large repos
"""

import datetime
import subprocess
import hashlib
import zlib
import os

import util

util.init()
git_dir = b'.git'
objects_dir = os.path.join(git_dir, b'objects')

# Directory parameters.
blob_content = b'a'
blob_basename = b'a'
blob_mode = b'100644'

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

def get_object_and_sha(obj_type, content):
    obj = b'%s %s\0%s' % (obj_type, str(len(content)).encode('ascii'), content)
    hash = hashlib.sha1(obj)
    return (obj, hash.hexdigest().encode('ascii'), hash.digest())

def save_object(obj_type, content):
    obj, sha_ascii, sha = get_object_and_sha(obj_type, content)
    obj_dir = os.path.join(objects_dir, sha_ascii[:2])
    obj_path = os.path.join(obj_dir, sha_ascii[2:])
    os.makedirs(obj_dir, exist_ok=True)
    with open(obj_path, 'wb') as f:
        f.write(zlib.compress(obj))

def get_git_hash_object(obj_type, input):
    cmd = [b'git', b'hash-object', b'--stdin', b'-t', obj_type]
    return subprocess.check_output(cmd, input=input).rstrip()

# Blob.
save_object(b'blob', blob_content)
obj, blob_sha_ascii, blob_sha = get_object_and_sha(b'blob', blob_content)
# Check sha matches Git.
blob_sha_git = get_git_hash_object(b'blob', blob_content)
assert blob_sha_ascii == blob_sha_git

# Tree.
tree_content = b'%s %s\0%s' % (blob_mode, blob_basename, blob_sha)
save_object(b'tree', tree_content)
# Check sha matches Git.
obj, tree_sha_ascii, tree_sha = get_object_and_sha(b'tree', tree_content)
tree_sha_git = get_git_hash_object(b'tree', tree_content)
assert tree_sha_ascii == tree_sha_git

# Commit.
commit_content = b'tree %s\nauthor %s <%s> %s\ncommitter %s <%s> %s\n\n%s\n' % (
        tree_sha_ascii,
        author_name, author_email, author_date,
        committer_name, committer_email, committer_date,
        message)
save_object(b'commit', commit_content)
# Check sha matches Git.
obj, commit_sha_ascii, commit_sha = get_object_and_sha(b'commit', commit_content)
commit_sha_git = get_git_hash_object(b'commit', commit_content)
assert commit_sha_ascii == commit_sha_git

# Create master branch.
subprocess.check_output(['git', 'branch', 'master', commit_sha_ascii])
subprocess.check_output(['git', 'clone', '.', '../clone.tmp'])
