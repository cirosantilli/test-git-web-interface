#!/usr/bin/env python3

"""
TODO: remove invalid emails, at the very least those that contain newlines or <>,
which make fsck fail. Those must have been pushed on a previous version of GitHub.

A repository with one commit per commit email:
https://github.com/cirosantilli/all-github-commit-emails

As of 2015-12-31 , the generated repo is just under 1Gb,
so under GitHub's soft max repo size limit.

    remote='git@github.com:cirosantilli/imagine-all-the-people.git'
    for i in `seq 10 10 100`; do
        git --git-dir=repo.tmp/.git push -f "$remote" "$i:master"
    done
    # TODO for some reason I needed this afterwards.
    git --git-dir=tmp/repo.tmp/.git push "$remote" 'master'
"""

import datetime
import subprocess
import time
import os

import util

# data_dir_path = '/path/to/all-github-commit-emails/emails'
data_dir_path = '/home/ciro/bak/git/all-github-commit-emails/emails'

name = b'a'

util.init()

tree = util.create_tree_with_one_file()
commit = None
n = 1000000
percent = (n / 100)
p = 0
i = 0

data_paths = sorted(os.listdir(data_dir_path))
for data_path in data_paths:
    data_path = os.path.join(data_dir_path, data_path)
    with open(data_path, 'rb') as f:
        for line in f:
            email = line.rstrip()[:255]
            commit, _, _ = util.save_commit_object(
                tree,
                (commit,),
                author_email=email,
                committer_email=email,
            )
            if i % percent == 0:
                print(p)
                print(email)
                print(datetime.datetime.now())
                p += 1

                # Lose objects are too large and blow up the tmpfs.

                # Does clean packets, but the calculation takes more and more memory,
                # and slows down and blows up at the end. TODO which subcommand blows up eactly?.
                #subprocess.check_output(['git', 'gc'])

                subprocess.check_output(['git', 'repack'])
                subprocess.check_output(['git', 'prune-packed'])

                subprocess.check_output(['git', 'tag', str(p), commit])
            i += 1
            if i == 100000:
                util.create_master(commit)
