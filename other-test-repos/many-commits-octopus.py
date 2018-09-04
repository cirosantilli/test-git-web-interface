#!/usr/bin/env python3

import datetime
import subprocess
import time
import sys

import util

email = b'a@a.com'
name = b''

util.init()

tree = util.create_tree_with_one_file()
commit = None
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 1000
base_commit, _, _ = util.save_commit_object(
    tree,
    (commit,),
    author_date_s=0,
    author_email=email,
    author_name=name,
    committer_date_s=0,
    committer_email=email,
    committer_name=name,
    message=b'',
)
parents = []
for i in range(n):
    now = int(time.time())
    commit, _, _ = util.save_commit_object(
        tree,
        (base_commit,),
        author_date_s=i,
        author_email=email,
        author_name=name,
        committer_date_s=0,
        committer_email=email,
        committer_name=name,
        message=b'',
    )
    parents.append(commit)
    if i % 100000 == 0:
        print(i)
        print(datetime.datetime.now())
        subprocess.check_output(['git', 'repack'])
        subprocess.check_output(['git', 'prune-packed'])
        subprocess.check_output(['git', 'tag', str(i), commit])
final_commit, _, _ = util.save_commit_object(
    tree,
    parents,
    author_date_s=0,
    author_email=email,
    author_name=name,
    committer_date_s=0,
    committer_email=email,
    committer_name=name,
    message=b'',
)
util.create_master(final_commit)
