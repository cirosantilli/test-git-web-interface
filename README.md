This repo is only for testing how GitHub works.

# markdown tests

# h1

## h2

### h3

#### h4

##### h5

## 012 UPPERCASE underline_hyphen-spaces  others%%%end

# h

[""]()

[#h](#h)

[/#h](/#h)

[README.md#h](README.md#h)

[d/README.md#h](d/README.md#h)

[`code` inside link](#)

# List

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


Code in list:

- a

        b

# Table

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

| Open source | Open source | Open source | Open source | Open source | Open source | Open source | Open source | Open source |
|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|-------------|
| Open source | Open source | Open source | Open source | Open source | Open source | Open source | Open source | Open source |

| asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer |
|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
| asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer | asdfqwerasdfqwerasdqwerasdfqwer |

# Link

Relative link: [a.md](a.md).

Relative link: [..](..).

Relative automatic link: <a.md>.

Automatic link: <http://example.com>.
