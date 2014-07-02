#!/usr/bin/env bash

[ "$(cat a)" -gt "6" ] && echo "fail" && exit 1
exit 0
