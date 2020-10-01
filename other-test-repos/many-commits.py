#!/usr/bin/env python3

"""
Packing is important, or else deleting and pushing the generated repository could take a **huge** ammount of time.

This method gets slower as it goes. 1M are fast to generate, but 10M require running for 24h nonstop.

For extra safety, use a tmpfs or ramfs:

```
ulimit -Sv 500000
mkdir -p tmp
sudo umount tmp
sudo mount -t tmpfs -o size=3g tmpfs tmp
sudo chown $USER:$USER tmp
cd tmp
../many-commits.py
```

The tags can be used to push by parts to GitHub, which does not accept 1M at once:

```
remote='git@github.com:cirosantilli/test-many-commits-1m.git'
for i in `seq 10 10 100`; do
    git --git-dir=tmp/repo.tmp/.git push -f "$remote" "$i:master"
done
# TODO for some reason I needed this afterwards.
git --git-dir=tmp/repo.tmp/.git push "$remote" 'master'
```
"""

import datetime
import subprocess
import time
import sys

import util

email = b''
name = b''

util.init()

# https://stackoverflow.com/questions/9905257/git-push-fatal-unable-to-create-thread-resource-temporarily-unavailable
subprocess.run(['git', 'config', '--local', 'pack.windowMemory', '50m'])
subprocess.run(['git', 'config', '--local', 'pack.packSizeLimit', '50m'])
subprocess.run(['git', 'config', '--local', 'pack.threads', '1'])

tree = util.create_tree_with_one_file()
commit = None
if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 1000
for i in range(n):
    now = int(time.time())
    commit, _, _ = util.save_commit_object(
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
    if i % 100000 == 0:
        print(i)
        print(datetime.datetime.now())
        # Lose objects are too large and blow up the tmpfs.
        # Does clean packets, but the calculation takes more and more memory,
        # and slows down and blows up at the end. TODO which subcommand blows up exactly?.
        #subprocess.check_output(['git', 'gc'])
        subprocess.check_output(['git', 'repack'])
        subprocess.check_output(['git', 'prune-packed'])
        subprocess.check_output(['git', 'tag', str(i), commit])
util.create_master(commit)
