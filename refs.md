# Refs

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
