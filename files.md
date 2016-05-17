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

-   Very tall or wide Unicode glyphs. [More details](https://www.quora.com/What-are-the-coolest-Unicode-characters/answer/Ciro-Santilli-%E5%85%AD%E5%9B%9B%E4%BA%8B%E4%BB%B6-%E6%B3%95%E8%BD%AE%E5%8A%9F-%E7%BA%B3%E7%B1%B3%E6%AF%94%E4%BA%9A-%E5%A8%81%E8%A7%86).

    -   Basmala ﷽

        <https://github.com/cirosantilli/test-git-web-interface/blob/fc0bf02b85e42e649127d964057e594361c4f305/%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD%EF%B7%BD>

    -   Unicode Thai combining characters ส็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็็

        <https://github.com/cirosantilli/test-git-web-interface/blob/de4a8e71fe6a1fe7f6e95b864c833b0e6965996b/%E0%B8%AA%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87%E0%B9%87>

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
