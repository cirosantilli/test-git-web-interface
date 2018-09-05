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
commit, _, _ = util.save_commit_object(
    tree,
    (None,),
    author_date_s=0,
    author_email=email,
    author_name=name,
    committer_date_s=0,
    committer_email=email,
    committer_name=name,
    message=b'',
)
tag_sha, _, _ = util.save_tag_object(
    commit,
    b'mytag',
    object_type=b'commit',
    user_name=name,
    user_email=email,
    date_s=0,
    message=b'abc'
)
util.create_master(commit)
