#!/usr/bin/env python3

"""
Git does not let a commit have twice the same parent, but GitHub does, and normally shows it.
But as of 2016-05-17 they didn't page this edge case, and it 502's the commit for large numbers of links.
"""

import itertools

import util

util.init()

tree = util.create_tree_with_one_file()
commit, _, _ = util.save_commit_object(tree, author_name=b'a')
commit, _, _ = util.save_commit_object(tree, itertools.repeat(commit, 1000000), author_name=b'b')

# Finish.
util.create_master(commit)
util.clone()
