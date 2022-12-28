---
jupytext:
  formats: md:myst
  text_representation:
    extension: .myst
    format_name: myst
    format_version: 1.1
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Regular expressions

We often need to extract information from text by 
matching patterns.  Regular expressions are a powerful 
tool for defining patterns.

## Motivating Example

![https://xkcd.com/208/](https://imgs.xkcd.com/comics/regular_expressions.png)

## A More Realistic Example

California bill 1793, passed in 2018, 
provides for resentencing of people
convicted of low-level marijuana crimes 
before decriminalization.  Only a tiny 
fraction of those eligible for expungement 
could afford the time and attorney fees to 
go through the process.  San Francisco 
[teamed with Code for America](https://www.codeforamerica.org/programs/clear-my-record)
to automatically 
search legal records to identify tens of 
thousands eligible people from criminal records. 

Source code for identifying and summarizing 
convictions to be expunged is at 
[https://github.com/codeforamerica/autoclearance](https://github.com/codeforamerica/autoclearance).
Several uses of regular expressions 
can be found in 
[https://github.com/codeforamerica/autoclearance/blob/master/app/helpers/rap_sheet_deidentifier.rb](https://github.com/codeforamerica/autoclearance/blob/master/app/helpers/rap_sheet_deidentifier.rb). 
This code is in the Ruby language, but the 
regular expression code is fairly similar to 
regular expressions in Python, e.g., 

```ruby
def strip_addresses(text)
    address_regex = /COM:\s*ADR-[\d]{6,8}\s*\([^)]*\)/m
    text.gsub(address_regex, 'COM: [ADDRESS REDACTED]')
end
```

## But that's so unreadable!

Regular expressions are notoriously difficult 
to read.  If I encountered the regular expression 
above (`/COM:\s*ADR-[\d]{6,8}\s*\([^)]*\)/m`)
in code without other contextual cues, I could 
not easily guess that it is a pattern that 
matches street addresses in criminal records. 
Python makes it possible to write _somewhat_
more readable patterns.  

In this chapter and in our project, I do not
expect that you will become expert in reading
and writing complex regular expressions.  My goals for 
this introduction and pattern are: 

* I want you to be able to read very 
  basic regular expressions for text that 
  has a restricted, very predictable format. 
  
* I want you to be familiar enough with 
  regular expressions that sometime in the 
  future, when you encounter a problem for 
  which more complex regular expressions are
  the right tool, you will be ready to 
  open up one of the many, many tutorials or 
  reference guides available online and learn 
  what you need to solve your immediate problem. 
  
## Patterns are Like Programs

Regular expressions are like a little 
programming language designed just for 
matching patterns in text.  In Python we 
write these little pattern programs as 
quoted strings which are interpreted by the 
`re` module. 

The most basic regular expression is a 
string to be matched.  For example, if we 
wanted to find the word `cat` in string `s`, 
we can write 

```python
cat_pat = "cat"
s = "My cat's name is Nora"
m = re.search(cat_pat, s)
```

`re.search` will either return a _match object_ 
or `None`.  Since "cat" does appear in 
string `s`, 

```python
if m:
    print(f"Matched {m.start()}..{m.end()}")
else:
    print("*** No Match ***")
```

will print `Matched 3..6`.  

While `re.search` looks for any occurrence of
the pattern, `re.match` checks whether the 
whole string matches the pattern.  Thus 

```python
m = re.match(cat_pat, s)
if m:
    print(f"Matched {m.start()}..{m.end()}")
else:
    print("*** No Match ***")
```

prints `*** No Match ***`. 

### White space and comments in regular expressions

By default, a space in a regular expression 
matches a space in a string. 
```python
pat = " is "
s = "My cat's name is Nora"
m = re.search(pat, s)
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{s[start:end]}'")
else:
    print("*** No Match ***")
```

prints 

``` 
Matched 13..17
Matched substring is ' is '
```

Imagine if the only spaces permitted in a Python
program were those required by Python syntax, 
and there was no way to include comments. 
Our Python programs would be nearly as 
unreadable as many regular expressions. 
The Python `re` module, however, gives us 
the option of adding white space, comments, 
and newlines.  Adding the `re.X` flag 
argument to `re.search` or `re.match` enables
these readability aids: 

```python
pat = r"""
c    # C is for cat
a    # an a in the middle
t    # This pattern really didn't need comments, but others do
"""
s = "My cat's name is Nora"
m = re.search(pat, s, re.X)     ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{s[start:end]}'")
else:
    print("*** No Match ***")
```

## Composing Patterns 

Regular expressions wouldn't be very 
powerful if we could only search for 
fixed strings.   Fortunately we can build up 
complex patterns with operators.  This why 
they are called "expressions"; we combine simple 
patterns into more complex expressions just as 
we combine simple arithmetic expressions into 
more complex expressions with arithmetic operators 
like `+` and `-`. 

### Or (`|`)

Suppose _e1_ and _e2_ are regular expressions, 
and that they match _m1_ and _m2_, respectively.  
We can write a pattern _e1_ \| _e2_ to match 
either what _e1_ matches or what _e2_ matches, 
with parentheses to avoid ambiguity. 

```python
pat = "(cat)|(dog)|(ferret)"
s = "My cat's name is Nora"
m = re.search(pat, s, re.X)     ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{s[start:end]}'")
else:
    print("*** No Match ***")
```

### Repetition (`*` and `+`)

We can write _e1_\* to match any number of 
repetitions of what _e1_ matches, including 
zero, or we can write _e1_+ to match 
one or more repetitions.  

```python
pat = "(ch-)*(changes)"
bowie = "Ch-ch-ch-ch-changes  # Turn and face the strange"
m = re.search(pat, bowie, re.X)     ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
```

Prints: 

``` 
Matched 3..19
Matched substring is 'ch-ch-ch-changes'
```

### Concatenation 

The examples above are actually using another "operator"
for regular expressions.  The pattern `"cat"` is actually 
three patterns (`c`, `a`, and `t`) that are concatenated 
to form one longer pattern to match the concatenation of 
what each of the individual letter patterns matches.  
A more interesting application of concatenation appears 
in `"(ch-)*(changes)"`.  Here `ch-` pattern may be 
repeated, but it must be followed by something that 
matches `changes`.  We have used parentheses to be 
clear that the whole string "ch-" must be repeated, and 
not just the hyphen.

### Character sets (`[]`)

Notice that `"(ch-)*(changes)"` did not match the 
beginning "Ch" of "Ch-ch-ch-ch-changes".  We could 
use `|` allow the "c" to be matched in lower case or 
capitalized: 

```python
pat = "((c|C)h-)*(changes)"
bowie = "Ch-ch-ch-ch-changes  # Turn and face the strange"
m = re.search(pat, bowie, re.X)     ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
```

Often it is simpler to give a set or range of characters. 
`[axe]` matches any of "a", "x", or "e".  `[c-f]` matches 
any of "c", "d", "e", or "f".  

```python
pat = "([Cc]h-)*([a-z]+)  # Turn and face the strange"
bowie = "Ch-ch-ch-ch-changes "
m = re.search(pat, bowie, re.X)     ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
```

Prints 

``` 
Matched 0..19
Matched substring is 'Ch-ch-ch-ch-changes'
```

## Wild card (`.`)

The symbol `.` (pronounced "dot") is a wild card that matches 
any single character.  We can use `.*` to match a substring 
of any length (including length zero), containing 
anything.  The wild card is particularly useful for matching
text between delimiters, but we must be careful because it is 
"greedy" and will prefer the longest possible match.  For example: 

```python
m = re.search(pat, bowie, re.X)     ## re.X allows commented patterns
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
```

Prints: 

``` 
Matched 2..12
Matched substring is '-ch-ch-ch-'
```

## Search, Match, and Fullmatch

In the examples above, we have used the `search` function from 
`re` to find a substring matching the pattern anywhere in the 
string.   That is often the right choice if we are searching 
in unstructured text, most of which we skip over.  When we process 
structured text (like a spreadsheet, or assembly language source code) 
or semi-structured text (like html or markdown documents), 
we may not want skip over everything that doesn't match 
the pattern.  If we want the matched substring to start at the 
beginning of the string, we can use `match` instead of `search`. 
If the whole string should match, we can use `fullmatch`. 

| `re` function  |  matches              |
|----------------|-----------------------|
| `re.search`    | pattern anywhere in string (ignore the rest) |
| `re.match`     | pattern must match beginning of string |
| `re.fullmatch` | pattern must match the whole string    |

For example, if the string is "Ch-ch-ch-ch-changes", 
then we get the following results: 

| pattern       | `re.search`    | `re.match` | `re.fullmatch` |
|---------------|----------------|------------|----------------|
|`changes`      | `"changes"`    | (no match) | (no match)     |
|`([Cc]h-)*`    |`"Ch-ch-ch-ch-"`| `"Ch-ch-ch-ch-"` | (no match) |
|`([Cc]h-)*([a-z]+)`|`"Ch-ch-ch-ch-changes"`|`"Ch-ch-ch-ch-changes"`|`"Ch-ch-ch-ch-changes"`|


## Capturing

Often it is not enough to know the position of the whole match.  
Particularly when we are using `re.fullmatch`, we typically want 
to know which parts of the pattern matched which parts of the string. 
These are called "captures".  Each parenthesized part of the 
pattern creates a "capture group", which can be extracted from 
the match object: 

```python
pat = "((c|C)h-)*(changes)  # Turn and face the strange"
bowie = "Ch-ch-ch-ch-changes"
m = re.search(pat, bowie, re.X)    
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
    print(f"Groups {m.groups()}")
```

Prints: 

```
Matched 0..19
Matched substring is 'Ch-ch-ch-ch-changes'
Groups ('ch-', 'c', 'changes')
```

We can improve on this by giving the capture group names. 
We assign a name to a group by enclosing it in parentheses 
and prepending `?P<name>`. We can then obtain the named 
groups in the form of a Python dict
using the `groupdict` method: 

```python
pat = "(?P<prefix> ((c|C)h-)*) (?P<suffix> changes)"
bowie = "Ch-ch-ch-ch-changes"
m = re.search(pat, bowie, re.X)
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
    print(f"Groups {m.groupdict()}")
``` 

Prints: 

``` 
Matched 0..19
Matched substring is 'Ch-ch-ch-ch-changes'
Groups {'prefix': 'Ch-ch-ch-ch-', 'suffix': 'changes'}
```

In the example above, we have made the "prefix" 
group contain all repetitions of "Ch-" or "ch-".  
We can also make a group that captures just the 
last repetition, and groups can be nested: 

```python
pat = "(?P<prefix>(?P<lastch> (c|C)h-)*) (?P<suffix> changes)"
bowie = "Ch-ch-ch-ch-changes"
m = re.search(pat, bowie, re.X)
if m:
    start, end = m.start(), m.end()
    print(f"Matched {start}..{end}")
    print(f"Matched substring is '{bowie[start:end]}'")
    print(f"Groups {m.groupdict()}")
```

This prints: 

``` 
Matched 0..19
Matched substring is 'Ch-ch-ch-ch-changes'
Groups {'prefix': 'Ch-ch-ch-ch-', 'lastch': 'ch-', 'suffix': 'changes'}
```

## Perspective

One could write 
[a whole book](http://shop.oreilly.com/product/9780596528126.do)
on regular expressions. 
Or [another](http://shop.oreilly.com/product/0636920023630.do). 
Or many others.   At some time it may be worthwhile to
extensively study regular expressions, but this is probably 
not that time.  The selection of examples above is designed to
be _just enough_ to get through the project.  
My goals in this chapter, and in the 
accompanying project, are two: 

* You should be able to read a fairly simple regular expression
  and make sense of it. 
  
* You should understand _why_ we use regular expressions well 
  enough that in the future, when you are faced with a task 
  for which regular expressions are the best tool, you will be 
  prepared to learn what you need from books and online 
  tutorials and references. 
  
### Sample code 

[Sample code for this chapter](../sample_code/08_re.py)
