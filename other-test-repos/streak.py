#!/usr/bin/env python3

import datetime
import os

repo = 'repo'
os.mkdir(repo)
os.cwd(repo)

date0 = datetime.date(2000, 1, 1)
datef = datetime.date(2100, 1, 1)
date = date0
while date < datef:
    s = date.strftime('%Y-%m-%dT01:00:00')
    cmd = 'GIT_COMMITTER_DATE="{0}" git commit --allow-empty --allow-empty-message -m "" --date="{0}"'.format(s)
    print(cmd)
    os.system(cmd)
    date += datetime.timedelta(days=1)
