Git automatically treats certain directories as Git repositories when certain files are present.
<http://stackoverflow.com/questions/2044574/determine-if-directory-is-under-git-control>

In normal circumstances, this happens for test repos that are kept inside git related repositories,
e.g. <https://github.com/schacon/grack/tree/613acd237ab7f522a02953c310aad0d484873bd7/tests/example>

When there is a `.git` directory in the current directory,
it takes precedence over the current directory being a bare repo:
`git` commands without explicit `--git-dir` will use it.

If however git finds a directory that it recognizes to be a git bare repo and there is no `.git`,
it will be used. Try `git log` in this directory. If some system fails to check for that,
it is a great vector for arbitrary code execution.
