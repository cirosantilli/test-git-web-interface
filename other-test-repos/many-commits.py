#!/usr/bin/env python3

"""
Packing is important, or else deleting and pushing the generated repository could take a **huge** ammount of time.

This method gets slower as it goes. 1M are fast to generate, but 10M require running for 24h nonstop.

For extra safety, use a tmpfs or ramfs:

    ulimit -Sv 500000
    sudo umount tmp && \
        sudo mount -t tmpfs -o size=1g tmpfs tmp && \
        sudo chown $USER:$USER tmp &&
        ./imagine-all-the-people.py

The tags can be used to push by parts to GitHub, which does not accept 1M at once:

    remote='git@github.com:cirosantilli/test-many-commits-1m.git'
    for i in `seq 10 10 100`; do
        git --git-dir=tmp/repo.tmp/.git push -f "$remote" "$i:master"
    done
    # TODO for some reason I needed this afterwards.
    git --git-dir=tmp/repo.tmp/.git push "$remote" 'master'
"""

import datetime
import subprocess
import time

import util

email = b'ciro.santili@gmail.com'
name = b'Ciro Santilli'

util.init()

tree = util.create_tree_with_one_file()
commit = None
n = 1000000
percent = (n / 100)
p = 0
for i in range(n):
    now = int(time.time())
    commit, _, _ = util.save_commit_object(
        tree,
        (commit,),
        author_date_s=now,
        author_email=email,
        author_name=name,
        committer_date_s=now,
        committer_email=email,
        committer_name=name,
        message=(str(i).encode('ascii')),
    )
    if i % percent == 0:
        print(p)
        print(datetime.datetime.now())
        p += 1

        # Lose objects are too large and blow up the tmpfs.

        # Does clean packets, but the calculation takes more and more memory,
        # and slows down and blows up at the end. TODO which subcommand blows up eactly?.
        #subprocess.check_output(['git', 'gc'])

        subprocess.check_output(['git', 'repack'])
        subprocess.check_output(['git', 'prune-packed'])

        subprocess.check_output(['git', 'tag', str(p), commit])
util.create_master(commit)
