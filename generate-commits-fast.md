## Generate many commits fast

It is sometimes interesting to generate a ton of commits to test some edge case, but it is not trivial to go way above 1000 commits in a reasonable amount of time.

Bottom line: don't use `git`. The manual Python code under [other-test-repos](other-test-repos/) presents a huge speedup. TODO: try gitlib2.

1000 operations take on a my computer:

- echo to file, add and commit: 43s
- empty commit with `--allow-empt`: 23s
- `openssl dgst -sha1`: 22s
- `git hash-object --stdin -w`: 21s
- `git hash-object --stdin`: 20s
- `sha1sum` Coreutils: 1.4s.
- touch: 0.9s (same on ramfs).
- `time python3 <(printf 'import hashlib; import sys;\nfor i in range(1000): print(hashlib.sha1(str(i).encode("ascii")).hexdigest())')`: 0.14s TODO: why so much faster than `hash-object`? This is minimum bottleneck per CPU.
