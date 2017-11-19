#!/usr/bin/env bash

# https://github.com/cirosantilli/test-submodule-mod
# https://github.com/cirosantilli/test-submodule-top
# https://github.com/cirosantilli/test-submodule-top-shallow
# https://github.com/cirosantilli/test-submodule-mod-branch
# https://github.com/cirosantilli/test-submodule-top-branch
# https://github.com/cirosantilli/test-submodule-top-branch-shallow

set -ex

rm -rf tmp
mkdir tmp
cd tmp
rm -rf *

export GIT_AUTHOR_NAME="Ciro Santilli"
export GIT_AUTHOR_EMAIL="ciro.santilli@gmail.com"
export GIT_AUTHOR_DATE='2000-01-01T00:00:00+0000'
export GIT_COMMITTER_NAME="$GIT_AUTHOR_NAME"
export GIT_COMMITTER_EMAIL="$GIT_AUTHOR_EMAIL"
export GIT_COMMITTER_DATE="$GIT_AUTHOR_DATE"

mkdir mod
cd mod
git init
touch base
git add base
git commit -m base
touch master-1
git add master-1
git commit -m master-1
touch master-2
git add master-2
git commit -m master-2
git tag tag-master
touch master-3
git add master-3
git commit -m master-3
git checkout -b mybranch HEAD~3
touch mybranch-1
git add mybranch-1
git commit -m mybranch-1
touch mybranch-2
git add mybranch-2
git commit -m mybranch-2
git tag tag-mybranch
touch mybranch-3
git add mybranch-3
git commit -m mybranch-3
git checkout master
cd ..

mkdir top
cd top
git init
touch a
git add a
git commit -m 1
touch b
git add b
git commit -m 2
git submodule add ../mod/ mod
git add .gitmodules
git commit -m '.gitmodules'
cd ..

cp -rv top top-shallow
cd top-shallow
printf '\tshallow = true\n' >> .gitmodules
git add .gitmodules
git commit -m 'shallow'
cd ..

mkdir top-branch
cd top-branch
git init
touch a
git add a
git commit -m 1
touch b
git add b
git commit -m 2
git submodule add -b mybranch ../mod/ mod
git add .gitmodules
git commit -m '.gitmodules'
cd ..

cp -rv top-branch top-branch-shallow
cd top-branch-shallow
printf '\tshallow = true\n' >> .gitmodules
git add .gitmodules
git commit -m 'shallow'
cd ..

mkdir top-tag
cd top-tag
git init
touch a
git add a
git commit -m 1
touch b
git add b
git commit -m 2
git submodule add ../mod/ mod
cd mod
git checkout tag-mybranch
cd ..
git add .
git commit -m '.gitmodules'
cd ..

mkdir top-sha
cd top-sha
git init
touch a
git add a
git commit -m 1
touch b
git add b
git commit -m 2
git submodule add ../mod/ mod
cd mod
git checkout tag-mybranch~
cd ..
git add .
git commit -m '.gitmodules'
cd ..

rm -f results

git clone --depth 1 "file://$(pwd)/mod" mod-clone
git --git-dir mod-clone/.git log --oneline | wc -l >>results
# 1

git clone --depth 1 "file://$(pwd)/mod" mod-branch-clone
git --git-dir mod-branch-clone/.git log --oneline | wc -l >>results
# 1

## gitmodule

echo 'gitmodule' >>results

git clone --recurse-submodules "file://$(pwd)/top" top-clone
git --git-dir top-clone/.git/modules/mod log --oneline | wc -l >>results
# many

git clone --recurse-submodules "file://$(pwd)/top-shallow" top-shallow-clone
git --git-dir top-shallow-clone/.git/modules/mod log --oneline | wc -l >>results
# 1

git clone --recurse-submodules "file://$(pwd)/top-branch" top-branch-clone
git --git-dir top-branch-clone/.git/modules/mod log --oneline | wc -l >>results
# many

git clone --recurse-submodules "file://$(pwd)/top-branch-shallow" top-branch-shallow-clone
git --git-dir top-branch-shallow-clone/.git/modules/mod log --oneline | wc -l >>results
# many

git clone --recurse-submodules "file://$(pwd)/top-tag" top-tag-clone
git --git-dir top-tag-clone/.git/modules/mod log --oneline | wc -l >>results
# many

git clone --recurse-submodules "file://$(pwd)/top-sha" top-sha-clone
git --git-dir top-sha-clone/.git/modules/mod log --oneline | wc -l >>results
# many

## SS

echo 'ss' >>results

git clone --recurse-submodules --shallow-submodules "file://$(pwd)/top" top-clone-ss
git --git-dir top-clone-ss/.git/modules/mod log --oneline | wc -l >>results
# 1

git clone --recurse-submodules --shallow-submodules "file://$(pwd)/top-shallow" top-shallow-clone-ss
git --git-dir top-shallow-clone-ss/.git/modules/mod log --oneline | wc -l >>results
# 1

git clone --recurse-submodules --shallow-submodules "file://$(pwd)/top-branch" top-branch-clone-ss
git --git-dir top-branch-clone-ss/.git/modules/mod log --oneline | wc -l >>results
# 1

git clone --recurse-submodules --shallow-submodules "file://$(pwd)/top-branch-shallow" top-branch-shallow-clone-ss
git --git-dir top-branch-shallow-clone-ss/.git/modules/mod log --oneline | wc -l >>results
# 1

git clone --recurse-submodules --shallow-submodules "file://$(pwd)/top-tag" top-tag-clone-ss
git --git-dir top-tag-clone-ss/.git/modules/mod log --oneline | wc -l >>results
# 1

#git clone --recurse-submodules --shallow-submodules "file://$(pwd)/top-sha" top-sha-clone-ss
# error: Server does not allow request for unadvertised object
#git --git-dir top-sha-clone-ss/.git/modules/mod log --oneline | wc -l >>results

cat results
