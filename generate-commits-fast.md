## Generate many commits fast

It is sometimes interesting to generate a ton of commits to test some edge case, but it is not trivial to go way above 1000 commits in a reasonable amount of time.

1000 operations take on a my computer:

- echo to file, add and commit: 43s
- empty commit with `--allow-empt`: 23s
- `openssl dgst -sha1`: 22s
- `git hash-object --stdin -w`: 21s
- `git hash-object --stdin`: 20s
- `sha1sum` Coreutils: 1.4s. TODO: why so much faster than `hash-object`? This is minimum bottleneck per CPU. We can reuse identical blobs. 
- touch: 0.9s (same on ramfs). This is the minimum IO bottleneck. Since the CPU bottleneck is not much above, parallelization is not the trouble.
