#!/usr/bin/env python

'''
This is a superior and simpler alternative to many-commits.py.

Usage:

rm -rf many-commits.tmp
mkdir -p many-commits.tmp
cd many-commits.tmp
git init
../many-commits-fast-import.py [ncommits=10] | git fast-import

Lenovo ThinkPad P51 SSD generation time for 2M commits: 33s. Disk usage: 270.2 MiB. Push size is smaller for some reason.
'''

import sys

print('''blob
mark :1
data 1
a
reset refs/heads/master
commit refs/heads/master
mark :2
author  <> 0 +0000
committer  <> 0 +0000
data 1

M 100644 :1 a
''')

if len(sys.argv) > 1:
    n = int(sys.argv[1])
else:
    n = 10
for i in range(2, n + 2):
    print('''commit refs/heads/master
mark :{}
author  <> {} +0000
committer  <> 0 +0000
data 1

from :2
'''.format(i + 1, i - 2))
print('''commit refs/heads/master
mark :{}
author  <> 0 +0000
committer  <> 0 +0000
data 1

from :3'''.format(n + 3)
)
for i in range(4, n + 3):
    print('merge :{}'.format(i))
