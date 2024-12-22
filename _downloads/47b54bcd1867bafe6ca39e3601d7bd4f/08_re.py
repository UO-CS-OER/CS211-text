"""Regular expression examples for week 8 chapter"""

import re

print("Example 1, strings match themselves")

cat_pat = "cat"
s = "My cat's name is Nora"
m = re.search(cat_pat, s)
if m:
    print(f"Matched {m.start()}..{m.end()}")
else:
    print("*** No Match ***")

print("Example 2, 'match' means 'match the whole string'")

m = re.match(cat_pat, s)
if m:
    print(f"Matched {m.start()}..{m.end()}")
else:
    print("*** No Match ***")

print("Example 3, spaces match spaces")
pat = " is "
s = "My cat's name is Nora"
m = re.search(pat, s)
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{s[start:end]}'")
else:
    print("*** No Match ***")

print("Example 4, adding whitespace and comments")
pat = r"""
c    # C is for cat
a    # an a in the middle
t    # This pattern really didn't need comments, but others do
"""
s = "My cat's name is Nora"
m = re.search(pat, s, re.X)  ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{s[start:end]}'")
else:
    print("*** No Match ***")

print("Example 5, OR")
pat = "(cat)|(dog)|(ferret)"
s = "My cat's name is Nora"
m = re.search(pat, s, re.X)  ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{s[start:end]}'")
else:
    print("*** No Match ***")

print("Example 6, *")
pat = "(ch-)*(changes)"
bowie = "Ch-ch-ch-ch-changes  # Turn and face the strange"
m = re.search(pat, bowie, re.X)  ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
else:
    print("*** No Match ***")

print("Example 6.5, OR for character sets")
pat = "((c|C)h-)*(changes)"
bowie = "Ch-ch-ch-ch-changes  # Turn and face the strange"
m = re.search(pat, bowie, re.X)  ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
else:
    print("*** No Match ***")

print("\nExample 7, [ ] for character sets")
pat = "([Cc]h-)*([a-z]+)  # Turn and face the strange"
bowie = "Ch-ch-ch-ch-changes "
m = re.search(pat, bowie, re.X)  ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
else:
    print("*** No Match ***")

print("\nExample 7.5, wild card")
bowie = "Ch-ch-ch-ch-changes"
pat = "-(.*)-   #Anything between - and -"
m = re.search(pat, bowie, re.X)  ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
else:
    print("*** No Match ***")

print("\n Example 8, match/fullmatch")
bowie = "Ch-ch-ch-ch-changes"
for pat in ["changes", "([Cc]h-)*", "([Cc]h-)*([a-z]+)"]:
    print(f"\nPattern is '{pat}'")
    print("Checking 'search'")
    m = re.search(pat, bowie)
    if m:
        start, end = m.start(), m.end()
        print(f"'{pat}' Matched {start}..{end}")
        print(f"Matched substring is '{bowie[start:end]}'")
    else:
        print("*** No Match ***")

    print("Checking 'match'")
    m = re.match(pat, bowie)
    if m:
        start, end = m.start(), m.end()
        print(f"'{pat}' Matched {start}..{end}")
        print(f"Matched substring is '{bowie[start:end]}'")
    else:
        print("*** No Match ***")

    print("Checking 'fullmatch'")
    m = re.fullmatch(pat, bowie)
    if m:
        start, end = m.start(), m.end()
        print(f"'{pat}' Matched {start}..{end}")
        print(f"Matched substring is '{bowie[start:end]}'")
    else:
        print("*** No Match ***")

print("\nExample 9, capture groups")
pat = "((c|C)h-)*(changes)  # Turn and face the strange"
bowie = "Ch-ch-ch-ch-changes"
m = re.search(pat, bowie, re.X)
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
    print(f"Groups {m.groups()}")
else:
    print("*** No Match ***")

print("\nExample 9a, named capture groups")
pat = "(?P<prefix> ((c|C)h-)*) (?P<suffix> changes)"
bowie = "Ch-ch-ch-ch-changes"
m = re.search(pat, bowie, re.X)
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
    print(f"Groups {m.groupdict()}")
else:
    print("*** No Match ***")

print("\nExample 9b, named capture groups with repetition")
pat = "(?P<prefix>(?P<lastch> (c|C)h-)*) (?P<suffix> changes)"
bowie = "Ch-ch-ch-ch-changes"
m = re.search(pat, bowie, re.X)
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
    print(f"Groups {m.groupdict()}")
else:
    print("*** No Match ***")
