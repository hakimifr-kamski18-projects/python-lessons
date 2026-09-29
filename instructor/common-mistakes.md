# Common beginner mistakes

Recognise these on sight. When you see one, do not fix it. Ask the question in the right
column and let them find it.

## Syntax level

These produce `SyntaxError` or `IndentationError`, which is the friendlier category,
because Python refuses to run at all and points at a line.

| What you will see | Why it happens | Question to ask |
| --- | --- | --- |
| `print("hello"` | Missing closing bracket | "Count the brackets on that line. Do they match?" |
| `if x > 5` then `print(x)` with no colon | Forgot the `:` | "What did the previous `if` line end with?" |
| `if x > 5:` but the body is not indented | Indentation is the syntax here | "Which line is supposed to be inside the if?" |
| `IndentationError: unexpected indent` | Extra space at the start of a line | "Is that line meant to be inside something?" |
| `TabError` | Tabs and spaces mixed in one file | "Let us look at the whitespace. Set your editor to three or four spaces and re-indent that block." |
| `print "hello"` | Syntax from Python 2 or from another language | "`print` is a function here, so it needs brackets." |
| `x = 5` written as `x == 5` | Confusing assignment with comparison | "You asked whether it equals, not to make it equal." |
| A curly quote `"hello"` | Typed in a chat app or word processor first | "That quote is not the straight one. Retype it in the editor." |

Curly quotes deserve a special mention. A student who writes their code in Telegram,
WhatsApp, or Google Docs and then pastes it will hit `SyntaxError: invalid character '"'
(U+201C)` and be completely baffled, because the character looks fine on screen. If
their code contains a suspicious `SyntaxError` with a `U+` code in it, this is almost
certainly why. Tell them to type code in the editor, always, and this stops happening.

## Runtime level

These are errors Python only notices once it is running. The code looks fine, which
makes them harder and more interesting.

| Error | What it really means | Question to ask |
| --- | --- | --- |
| `NameError: name 'x' is not defined` | Typo, wrong capitalisation, or the variable is never assigned | "Find every place you wrote that name. Do they match exactly, capitals included?" |
| `TypeError: can only concatenate str (not "int") to str` | Gluing a number onto text with `+` | "What type is each side of the `+`? Use `type()` and see." |
| `TypeError: unsupported operand type(s) for +: 'int' and 'str'` | The reverse order of the above | Same question. |
| `ValueError: invalid literal for int() with base 10: 'five'` | Converting something that is not a number | "What exactly did the user type? Print it before converting." |
| `IndexError: list index out of range` | Asking for position 5 of a four item list | "How long is the list? Remember positions start at zero." |
| `KeyError: 'name'` | Asking a dictionary for a key it does not have | "How could you check whether the key is there before asking for it?" |
| `ZeroDivisionError` | Dividing by something that turned out to be zero | "Print the divisor right before the division." |
| `AttributeError: 'str' object has no attribute 'append'` | Calling a list method on a string, or a typo in a method name | "What type is that thing, and does that type have that method?" |
| `TypeError: 'int' object is not iterable` | Forgetting `range()` in a `for` loop, writing `for i in 5` | "What do you want to loop over? `5` is one number, not a sequence." |

## Conceptual level

These are the ones that matter most, because the code runs and the output is wrong, or
the student's mental model is quietly broken.

### `=` versus `==`

```
=   put this value in that box        x = 5
==  ask whether these are equal       x == 5
```

Ask them to read each one out loud as a sentence. "X gets five" versus "is x equal to
five". The out-loud reading fixes this surprisingly fast.

### `input()` always gives back a string

The single most common beginner bug in the whole curriculum. No matter what the user
types, `input()` returns text. So this fails.

```python
age = input("How old are you? ")
print(age + 1)
```

And this works.

```python
age = int(input("How old are you? "))
print(age + 1)
```

Do not just tell them. Make them hit the `TypeError`, ask them to check with
`type(age)`, and then reason their way to `int()`.

Also worth showing, because it trips people even after they know better.

```python
print("5" + "5")     # 55, not 10
print(5 + 5)         # 10
```

### Off by one in `range()`

`range(5)` gives 0, 1, 2, 3, 4. Not 1 to 5. This is correct and deliberate, and
beginners find it maddening.

Teach them to check rather than memorise.

```python
print(list(range(5)))
```

Then let them decide. Also show that `range(1, 6)` gives 1 through 5, so the end is
always exclusive.

### Positions start at zero

```python
letters = ["a", "b", "c"]
letters[0]   # "a"
letters[2]   # "c"
letters[3]   # IndexError
```

Say the sentence "the first item is at position zero" many times, and make them count
index positions on their fingers once. It sticks better than a rule.

### `print` versus `return`

The classic. Teaching `print` in unit 01 and `return` in unit 06 means this will appear,
and it is worth a whole ten minutes.

```python
def double(n):
    print(n * 2)

result = double(5)
print(result)     # 10, then None
```

Ask them what `result` holds. The answer `None` is surprising and instructive. A
function that prints shows you something. A function that returns hands something back
to the code that called it. You cannot do maths with printed output.

### Mutating a list while looping over it

```python
numbers = [1, 2, 3, 4, 5, 6]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
```

This skips items, for reasons that are genuinely subtle. Do not teach the mechanism.
Teach the rule, loop over a copy (`for n in numbers[:]`) or build a new list. This is a
"later" topic, so just plant the flag.

### Variable names that shadow builtins

```python
list = [1, 2, 3]
sum = 0
str = "hello"
```

It runs. Then later `list("abc")` fails mysteriously, or `sum(numbers)` breaks, because
the name now refers to their variable. Ask them to run `print(sum)` after assigning `sum
= 0`. The confusing part is that Python allows it.

Teach the habit of naming things `total`, `items`, `text` instead.

### Forgetting `return`

```python
def add(a, b):
    result = a + b
```

This computes the answer and throws it away. The function returns `None`. Ask "where
does `result` go when the function finishes?" and then have them call `add(2, 3)` in the
shell and look at the result.

### Comparing floats for equality

```python
print(0.1 + 0.2 == 0.3)    # False
```

Worth showing once, as a "computers are not magic" moment. Do not go into binary
floating point representation. Just say numbers with decimals are stored approximately,
and comparing them directly is unreliable, so compare with a small tolerance if it ever
comes up.

### Copying a list by assignment

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)      # [1, 2, 3, 4]
```

Both names point at the same list. Ask them to predict the second print before running
it. The fix is `b = a[:]` or `b = list(a)`, but the fix matters less than the surprise.

### Strings are not lists

```python
name = "ada"
name[0] = "A"     # TypeError
```

You cannot change a string in place. You make a new one.

```python
name = "A" + name[1:]
```

Also worth knowing.

```python
name.upper()        # returns "ADA", does not change name
name = name.upper() # this does change it
```

A lot of string methods return a new string and leave the original alone. If the code
"does nothing", this is usually why.

### `and` and `or` are not English

```python
if answer == "yes" or "y":
```

This is always true, because `"y"` is a non-empty string, which counts as true. Students
write it because it reads right in English. Ask them to say the whole condition out loud
"or why" and the bug usually reveals itself.

Correct form.

```python
if answer == "yes" or answer == "y":
```

Or the cleaner Python way, once they know about lists.

```python
if answer in ["yes", "y"]:
```

## How to use this file

Do not pre-emptively teach this list. It is a lookup table for you, so that when a
student hits one of these you recognise it in two seconds, ask the right question, and
let them do the finding.

The exceptions worth teaching ahead of time, because they are so common that bumping
into them repeatedly wastes time.

- `=` versus `==`, before unit 03.
- `input()` gives a string, inside unit 02.
- Off by one in `range()`, inside unit 04.
- `print` versus `return`, inside unit 06.
