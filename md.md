# Markdown tests

# h1

## h2

### h3

#### h4

##### h5

## 012 UPPERCASE underline_hyphen-spaces  others%%%end

## h

Tests of automatic header ID generation.

[""]()

[#h](#h)

[/#h](/#h)

[README.md#h](README.md#h)

[d/README.md#h](d/README.md#h)

[`code` inside link](#)

## List

No newlines:

- a
- b
- c

Newlines:

- a

- b

- c

Some newlines:

- first

- after newline
- not after newline

Ordered:

1. 1
2. 2
3. 3

Only 1:

1. 1
1. 1
1. 1

Start 2:

2. 2
3. 3
4. 4

Inner list:

1.  1
2.  2
    - list
3.  3

Inner list:

1.  1
1.  1
    - list
1.  1

Inner list 1:

1.  1

1.  1

    - list
    - list

1.  1

Inner par list:

1.  1

2.  1

    - list
    - list

3.  1

Inner par ordered list:

1.  1

2.  1

    1. list
    2. list

3.  1

Inner par:

1.  1
1.  1

    par

1.  1


Nested:

- par
    - nopar
    - nopar
    - nopar

        - par

        - par

        - par

- par

- par


Code in list with one indent:

- a

        b

## Table

Very picky about table format. There must be the right amount of pipes, 3 consecutive hyphens per column of the separator line:

| a | b |
|---|---|
| c | d |

No outer pipes:

 a | b
---|---
 c | d

4 hyphens:

| a | b |
|----|---|
| c | d |

Space 3 hyphens:

| a | b |
| ---|---|
| c | d |

3 hyphens space:

| a | b |
|--- |---|
| c | d |

hyphen space 2 hyphens:

| a | b |
|- --|---|
| c | d |

2 hyphens:

| a | b |
|--|---|
| c | d |

no pipes:

| a | b |
|-------|
| c | d |

## Link

Automatic: <http://example.com>

Weird characters: with and without angle brackets:

`'` <http://example.com/ab'cd> http://example.com/ab'cd

`"` <http://example.com/ab"cd> http://example.com/ab"cd

`!` <http://example.com/ab!cd> http://example.com/ab!cd

`$` <http://example.com/ab$cd> http://example.com/ab$cd

`&` <http://example.com/ab&cd> http://example.com/ab&cd

`(` <http://example.com/ab(cd> http://example.com/ab(cd

`)` <http://example.com/ab)cd> http://example.com/ab)cd

`*` <http://example.com/ab*cd> http://example.com/ab*cd

`+` <http://example.com/ab+cd> http://example.com/ab+cd

`,` <http://example.com/ab,cd> http://example.com/ab,cd

`-` <http://example.com/ab-cd> http://example.com/ab-cd

`.` <http://example.com/ab.cd> http://example.com/ab.cd

`/` <http://example.com/ab/cd> http://example.com/ab/cd

`:` <http://example.com/ab:cd> http://example.com/ab:cd

`;` <http://example.com/ab;cd> http://example.com/ab;cd

`=` <http://example.com/ab=cd> http://example.com/ab=cd

`?` <http://example.com/ab?cd> http://example.com/ab?cd

`@` <http://example.com/ab@cd> http://example.com/ab@cd

`_` <http://example.com/ab_cd> http://example.com/ab_cd

`~` <http://example.com/ab~cd> http://example.com/ab~cd

### Relative links

[a.md](a.md).

[./a.md](./a.md).

[d/](d/). 14-11: GitHub renders links to `blob`, even if pointing to tree, and redirects `blob` to `tree`. GitLab also redirects, but renders trees as `tree` links directly.

[..](..).

[/../test-empty-commit](/../test-empty-commit).

Automatic relative link: <a.md>. Fails because would conflict with HTML tags.

## Image

- png.png ![](png.png)

- ./png.png ![](./png.png)

- d/png.png ![](d/png.png)

- ./d/png.png ![](./d/png.png)

### Video

https://user-images.githubusercontent.com/1429315/103039458-deb12a00-4568-11eb-9281-7cb8550666ca.mp4 uploaded at https://github.com/cirosantilli/china-dictatorship/issues/169

### Markup inside link

- [`d`](d)
- [*d*](d)
- [![](png.png)](d)

## GitHub extensions

User: @cirosantilli

Commit: cirosantilli/test-github@master

## Wide stuff

mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm

|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## Raw HTML

### HTML tags

`script`:

<script>alert('xss')</script>

`<div>a</div>`:

<div>a</div>

`</div>`:

</div>

### Entities

`&#35;`: &#35;

`&#1234;`: &#1234;

`&#992;`: &#992;

`&#98765432;`: &#98765432;

## XSS

<img onerror="alert('xss img onerror');" src="not-image" alt="err" />

For compilers that treat `h1` magically (e.g. add to a TOC):

# <script>alert('xss')</script>
