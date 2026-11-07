---
title: Common beginner mistakes
sidebar:
  hidden: true
pagefind: false
head:
  - tag: meta
    attrs:
      name: robots
      content: noindex
prev: false
next: false
---
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
| `TabError` | Tabs and spaces mixed in one file | "Let us look at the whitespace. Set your editor to four spaces and re-indent that block." |
| `print "hello"` | Syntax from Python 2 or from another language | "`print` is a function here, so it needs brackets." |
| `x = 5` written as `x == 5` | Confusing assignment with comparison | "You asked whether it equals, not to make it equal." |
| A curly quote, as in `print(“hello”)` | Typed in a chat app or word processor first | "That quote is not the straight one. Retype it in the editor." |

Curly quotes deserve a special mention. A student who writes their code in Telegram,
WhatsApp, or Google Docs and then pastes it will hit `SyntaxError: invalid character '“'
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
| `TypeError: Dog.bark() takes 0 positional arguments but 1 was given` | Forgetting `self` in a method's `def` line | "What does Python pass in when you write `rex.bark()`?" |
| `TypeError: Dog.__init__() missing 1 required positional argument: 'name'` | Creating an object without the values `__init__` asks for | "Read the `def __init__` line. What does it need after `self`?" |
| `AttributeError: 'Dog' object has no attribute 'name'` | A typo, or `name = name` in `__init__` without `self.` | "Where in `__init__` does the object get that attribute?" |

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

The classic. Teaching `print` in unit 01 and `return` in unit 07 means this will appear,
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
"later" topic, so just mention the rule and move on.

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

### A bare `except:`

```python
try:
    number = int(input("Number: "))
    print(numbr * 2)
except:
    print("That was not a number")
```

The typo `numbr` is a `NameError`, but the bare `except:` catches it and prints "That was
not a number" even when the input was fine. Ask "what does the program say when you type
`5`, and is that true?" Then have them write `except ValueError:` and run it again, so the
real error shows up.

### A giant `try` block

A student who has just learned `try` wraps the whole program in one. Every error then
lands in the same `except` with the same message, and a bug in their own code looks like
bad input. Ask "which line in here can actually raise a `ValueError`?" and have them
shrink the `try` to that line.

### Forgetting `break` in the validation loop

```python
while True:
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Not a whole number, try again")
```

Bad input gets the message, which is right, but good input does not end the loop either,
because nothing ever leaves it. It keeps asking forever. Ask "which line is supposed to
end the loop?" If they put the `break` after the whole `try` block, it runs after the bad
input too, so ask them to trace it with `hello`.

### Forgetting `self` in a method

```python
class Dog:
    def bark():
        print("Woof")

Dog().bark()   # TypeError: Dog.bark() takes 0 positional arguments but 1 was given
```

The message says one argument was given, and they can see an empty pair of brackets, so
it looks like Python is lying. Ask "what is in front of the dot, and where does it go?"
The object is passed in as the first argument, and `self` is the name that receives it.

### Forgetting `self.` inside the class

```python
class Dog:
    def __init__(self, name):
        name = name
```

This runs with no error. The error comes later, as `AttributeError: 'Dog' object has no
attribute 'name'` in some other method, or as a `NameError` when a method writes `name`
instead of `self.name`. Ask "after `__init__` finishes, where is the name kept?" A plain
`name` is a local variable, and it is gone when the method ends.

### Calling the class without brackets

```python
rex = Dog
```

This does not make a dog. It makes `rex` a second name for the class itself, and the
next method call fails with `missing 1 required positional argument: 'self'`. Ask "what
do you write to call a function?" and then "is `Dog` being called here?"

### Confusing the class and the object

Students say "the class" for both, and then write `Dog.name` or expect a change to one
object to change all of them. Ask them to say which one they mean every time. The class
is the plan, written once with `class`. Each object is one thing made from the plan, with
its own attributes. Making two objects and changing one of them shows it quickly.

## How to use this file

Do not pre-emptively teach this list. It is a lookup table for you, so that when a
student hits one of these you recognise it in two seconds, ask the right question, and
let them do the finding.

The exceptions worth teaching ahead of time, because they are so common that bumping
into them repeatedly wastes time.

- `=` versus `==`, before unit 03.
- `input()` gives a string, inside unit 02.
- Off by one in `range()`, inside unit 04.
- `print` versus `return`, inside unit 07.
- Forgetting `self`, inside unit 11.
