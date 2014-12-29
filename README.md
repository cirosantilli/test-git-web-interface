# Test

Tests to see how Git web interfaces like GitHub and GitLab work exactly detect bugs.

## Mirrors

This repository is mirrored at:

- <https://github.com/cirosantilli/test>
- <https://gitlab.com/cirosantilli/test>
- <https://bitbucket.org/cirosantilli/test>
- <https://code.google.com/p/cirosantilli-test>
- <https://sourceforge.net/projects/cirosantilli-test>
- <https://www.assembla.com/code/cirosantilli-test/git/nodes>

Mirrors without repository browsing:

- <http://codeplane.com>

The SSH of those repos can be found at: [remotes.sh](remotes.sh),
including other repos which don't have public view like Atlas.

## Related repositories

Tests that are very large will not be included here to keep this repository small:

- <https://github.com/cirosantilli/test-deep>
- <https://github.com/cirosantilli/test-diff-many-files>
- <https://github.com/cirosantilli/test-pr-many-commits>

There are also some tests that could not be included here conveniently:

- <https://github.com/cirosantilli/test-control-chars>
- <https://github.com/cirosantilli/test-empty-commit>
- <https://github.com/cirosantilli/test-empty-subdir>
- <https://github.com/cirosantilli/test-invalid-utf8>
- <https://github.com/cirosantilli/test-large-file>
- <https://github.com/cirosantilli/test-long-filename-1024>
- <https://github.com/cirosantilli/test-long-filename-256>
- <https://github.com/cirosantilli/test-min-sane>
- <https://github.com/cirosantilli/test-refs-api-tags-pulls-block>
- <https://github.com/cirosantilli/test-symlink-middle-null>
- <https://github.com/cirosantilli/test-symlink-self>
- <https://github.com/cirosantilli/test-symlink-start-null>
- <https://gitlab.com/cirosantilli/test-GIT/tree/master> (fails on GitHub)

Other similar repos from other people:

- <https://github.com/joernchen/evil_stuff>

Other useful things:

-   <https://github.com/holman/feedback/issues>. May contain some extra semi-internal information.

    - <https://github.com/showcases/projects-that-power-github>
    - <https://github.com/holman/feedback/issues/553> GitHub is hosted on Carpathia
    - <https://github.com/holman/feedback/issues/544> GitHub uses Mac?

## Files

The most interesting files on this repository are:

Markup tests:

- [md.md](markdown.md)
- [issue-md.md](issue-markdown.md): markdown on issues
- [adoc.adoc](adoc.adoc)
- [rdoc.rdoc](rdoc.rdoc)

Routing conflict attempts:

- [atom.atom](atom.atom)
- [diff](diff)
- [diff.diff](diff.diff)
- [patch.patch](patch.patch)

Weird stuff and attacks based on the filenames.

The only filenames which are not valid are:

- contain forward slash `/`
- `.git`
- `.` and `..`, but not `...`

Everything else goes:

-   [?a=b&c=d](?a=b&c=d)

-   ["](")

-   [#](#)

-   ['](')

-   [:](:)

-   [;](;)

-   [\](\)

-   [-](-)

-   [-start-with-slash](-start-with-slash)

-   [\.md](\.md)

-   whitespace filename edge cases:

    - [single whitespace filename](%20)
    - [double whitespace directory name](%20%20/) and [its README](%20%20/README.md)
    - [a b](a b)

-   Case insensitive filename conflict attempt: [CASE](CASE), [case](case) and [CASE-DIR](CASE-DIR), [case-dir](case-dir). Interestingly, however, `.GIT` fails: <https://gitlab.com/cirosantilli/test-GIT/tree/master>

Magic Git directories:

-   Git directory inside Git directory: [_git](_git).

    For further mischief, the files in that directory were copied to the top-level of the repository.

Other interesting things to do are the uppercase `.Git` and the `.git` file, which did not fit well in this repository.

XSS attempts:

- [<script>](<script>)
- `<script src="data:text;utf8,alert('xss')">`
- [svg.svg](svg.svg), with an XSS attempt

## Refs

Interesting branches and tags:

-   [`hasslash/a`](../hasslash/a): branch inside sub-directory

-   [`-r`](../-r): branch with forbidden name, and in particular one that may be used for shell injection. 

    Create manually with `cp master -- -r` and push with `git push --all`.

-   `<script>alert('xss')</script>` and `<b>a</b>`: XSS attempts

-   `tag-empty-blob`: a tag that points to a blob

-   [`a;{echo,INJECTION};{echo,RULZ};`](a;{echo,INJECTION};{echo,RULZ};): GitHub proposes a shell injection to users on a pull request under "You can also merge branches on the command line". <https://github.com/cirosantilli/test/pull/17>
