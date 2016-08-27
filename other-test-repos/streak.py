#!/usr/bin/env python3

import datetime
import os
import shutil
import subprocess

import util

util.init()

name = 'a'
email = 'a@a.com'
os.environ['GIT_AUTHOR_EMAIL'] = email
os.environ['GIT_AUTHOR_NAME'] = name
os.environ['GIT_COMMITTER_EMAIL'] = email
os.environ['GIT_COMMITTER_NAME'] = name

date0 = datetime.date(2000, 1, 1)
datef = datetime.date(2100, 1, 1)
date = date0
while date < datef:
    s = date.strftime('%Y-%m-%dT01:00:00')
    print(s)
    os.environ['GIT_AUTHOR_DATE'] = s
    os.environ['GIT_COMMITTER_DATE'] = s
    cmd = ['git', 'commit', '-q', '--allow-empty', '--allow-empty-message', '-m', '']
    subprocess.check_output(cmd)
    date += datetime.timedelta(days=1)
