import os
import shutil
import subprocess

def init():
    repo = 'repo.tmp'
    for d in (repo, 'clone.tmp'):
        shutil.rmtree(d, ignore_errors=True)
    os.mkdir(repo)
    os.chdir(repo)
    subprocess.check_output(['git', 'init', '-q'])
