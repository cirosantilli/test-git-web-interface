# Test

Tests to see how Git web interfaces like GitHub and GitLab work exactly detect bugs.

## Mirrors

This repository is mirrored at:

- <http://repo.or.cz/w/cirosantilli-test.git>. Runs on [Girocco](http://repo.or.cz/w/girocco.git). TODO get working.
- <https://bitbucket.org/cirosantilli/test>
- <https://github.com/cirosantilli/test>
- <https://gitlab.com/cirosantilli/test>
- <https://hub.jazz.net/git/cirosantilli/test>
- <https://sourceforge.net/projects/cirosantilli-test>
- <https://www.assembla.com/code/cirosantilli-test/git/nodes>

Mirrors without public view:

- <https://cirosantilli.kilnhg.com/Code/Repositories/Group/test/Files>
- <https://cirosantilli.visualstudio.com/DefaultCollection/_git/test> <http://webapps.stackexchange.com/questions/52512/tfs-visual-studio-online-make-a-query-publicly-visible>

Mirrors without repository browsing:

- <http://codeplane.com>

Mirrors for which I can't create projects:

- <https://kenai.com>

Discontinued:

- <https://code.google.com/p/cirosantilli-test> (to be closed)
- <https://gitorious.org/cirosantilli-test/cirosantilli-test>, bough by GitLab. Will remain read only.

Web interfaces without public hosting service that I know of. Huge list: <https://git.wiki.kernel.org/index.php/Interfaces,_frontends,_and_tools#Web_Interfaces> Some interesting ones:

- Gitweb. Distributed with Git. The Perl one.
- cgit. Official self-host: <http://git.zx2c4.com/cgit>, GitHub mirror: <https://github.com/zx2c4/cgit>. Used by GNU Savannah. Written in C.
- Gerrit. The Java one. <http://en.wikipedia.org/wiki/Gerrit_%28software%29>, 
- GitList. The PHP one. <https://github.com/klaussilveira/gitlist>
- WebGitNet. The .Net one. <https://github.com/otac0n/WebGitNet>

The SSH of those repos can be found at: [remotes.sh](remotes.sh), including other repos which don't have public view like Atlas.

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
- <https://github.com/cirosantilli/test-submodule-contributing>
- <https://github.com/cirosantilli/test-symlink-contributing>
- <https://github.com/cirosantilli/test-symlink-middle-null>
- <https://github.com/cirosantilli/test-symlink-self>
- <https://github.com/cirosantilli/test-symlink-start-null>
- <https://gitlab.com/cirosantilli/test-GIT/tree/master> (fails on GitHub)
- <https://github.com/cirosantilli/test-streak>, <https://github.com/cirosantilli/test-streak-1000>

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

-   [\\](\\)

-   [-](-)

-   [--](--)

-   [-start-with-slash](-start-with-slash)

-   [\.md](\.md)

-   whitespace filename edge cases:

    - [single whitespace filename](%20)
    - [double whitespace directory name](%20%20/) and [its README](%20%20/README.md)
    - [a b](a b)

-   Case insensitive filename conflict attempt: [CASE](CASE), [case](case) and [CASE-DIR](CASE-DIR), [case-dir](case-dir). Interestingly, however, `.GIT` fails: <https://gitlab.com/cirosantilli/test-GIT/tree/master>

Magic Git files:

-   Git directory inside Git directory: [_git](_git).

    For further mischief, the files in that directory were copied to the top-level of the repository.

-   [.gitattributes](.gitattributes): TODO empty

    Does not seems to lead to arbitrary code execution, as available diff and merge drivers must be set on the config.

    GitHub seems to ignore it: <http://stackoverflow.com/a/24382933/895245>

Other interesting things to do are the uppercase `.Git` and the `.git` file, which did not fit well in this repository.

XSS attempts:

- [<script>](<script>)
- `<script src="data:text;utf8,alert('xss')">`
- [svg.svg](svg.svg), with an XSS attempt
- [sym-xss](sym-xss). It's path is an XSS attempt.

## Refs

Interesting branches and tags:

-   [`hasslash/a`](../hasslash/a): branch inside sub-directory

-   [`-r`](../-r): branch with forbidden name, and in particular one that may be used for shell injection. 

    Create manually with `cp master -- -r` and push with `git push --all`.

-   `<script>alert('xss')</script>` and `<b>a</b>`: XSS attempts

-   `tag-empty-blob`: a tag that points to a blob

-   [`a;{echo,INJECTION};{echo,RULZ};`](a;{echo,INJECTION};{echo,RULZ};): GitHub proposes a shell injection to users on a pull request under "You can also merge branches on the command line". <https://github.com/cirosantilli/test/pull/17>

-   [1970](1970): earliest possible commit with `git commit --date '@0 +0000'`

-   [future](future): commit in the far far future, on some date that does not show as 1970 on `git log`? See also: <http://stackoverflow.com/questions/19742345/what-is-the-format-for-date-parameter-of-git-commit/29289807>

-   [future-max](future-max): commit at the latest possible pushable date of `2^63 - 1`. Larger dates up to `2^64 - 2` can be committed, but not pushed.

    As of 2015-04-02, that commits will show as the fist one on the UI commit list no matter its order on the commit tree, making it a good way to drive other people mad and then later make them scold you when they understand.
