#!/usr/bin/env bash

if [ $# -gt 0 ]; then
  REPO="$1"
  shift
else
  REPO=test
fi

git remote add at      git@atlas-tmp:tmp/${REPO}.git
git remote add as      git@git.assembla.com:cirosantilli-${REPO}.git
git remote add bb      git@bitbucket.org:cirosantilli/${REPO}.git
git remote add bs      https://cirosantilli.git.beanstalkapp.com/test.git
git remote add cp      git@codeplane.com:cirosantilli/${REPO}.git
git remote add cx      https://git01.codeplex.com/cirosantillitest
git remote add gc      https://code.google.com/p/cirosantilli-${REPO}
git remote add go      git@gitorious.org:cirosantilli-${REPO}/cirosantilli-${REPO}.git
#git remote add gr      ssh://repo.or.cz/cirosantilli-${REPO}.git
git remote add gh      git@github.com:cirosantilli/${REPO}.git
git remote add gl      git@gitlab.com:cirosantilli/${REPO}.git
# GitLab Local
git remote add gll     http://root:5iveL!fe@localhost:3000/gitlab-org/gitlab-${REPO}.git
git remote add ja      https://hub.jazz.net/git/cirosantilli/test
git remote add ki      ssh://cirosantilli@cirosantilli.kilnhg.com/Repositories/Group/test
git remote add lp      git+ssh://git.launchpad.net/cirosantilli-test-git
git remote add nb      https://notabug.org/cirosantilli/test-git-web-interface.git
git remote add origin  git@github.com:cirosantilli/${REPO}.git
git remote add pf      git@www.penflip.com:cirosantilli/${REPO}.git
git remote add sf      ssh://cirosantilli@git.code.sf.net/p/cirosantilli-${REPO}/code
# username: email
git remote add vs      https://cirosantilli.visualstudio.com/DefaultCollection/_git/test
