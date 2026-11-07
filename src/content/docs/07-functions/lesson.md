---
title: Unit 06 — Functions
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
**Files for this unit.** [`broken_functions.py`](/code/06-functions/broken_functions.py), [`first_function.py`](/code/06-functions/first_function.py), [`return_values.py`](/code/06-functions/return_values.py), [`scope.py`](/code/06-functions/scope.py)

These live in `public/code/06-functions/` in the repository, and the links above
open them as plain text. Every snippet the student needs is already inline in the
exercises, so the files are for the session itself, when you are both at the
keyboard.

**Goal for the session.** They can take a piece of work, give it a name, and use it from
several places. And they understand the difference between printing a result and
returning it, which means handing the value back. That distinction is the hardest idea
in the unit.

**Time.** Two sessions. The `print` versus `return` distinction needs its own attention
and will come back.

**Prerequisites.** Unit 05. Lists, loops, building results in a loop.


---

## 0. Warm-up

Have them write code that asks for five numbers and prints the average. Pure retrieval
from units 04 and 05.

Then have them modify it to also print the biggest and the smallest. Then ask them to
write a second program that does the same thing for ten numbers. The copy and paste is
the motivation for today, and it is worth making them feel it before you name the fix.

## 1. Naming a piece of work

Open [`first_function.py`](/code/06-functions/first_function.py).

```python
def greet():
    print("Hello!")
    print("Welcome to Python.")

greet()
greet()
greet()
```

The shape. `def`, a name, brackets, a colon, an indented body. Then you call it by name
with brackets.

Three things to point out.

**Defining is not running.** The body does not execute when Python reads the `def`. It
only runs when you call the function. Have them delete the three `greet()` calls and run
the file, and nothing happens. That is worth seeing.

**The brackets are required even with nothing inside.** `greet` without brackets is the
function itself, `greet()` is calling it. If they forget the brackets they will get no
output rather than an error, which is confusing. Worth showing.

**The body must be indented,** same rule as `if` and `for`.

### Why this exists

Go back to the warm-up and show the same logic written twice. Then rewrite it as a
function.

The reasons, in order of how much beginners care.

1. You write it once instead of many times.
2. If you fix a bug in it, you fix it in one place.
3. Most importantly, you can stop thinking about how it works inside. You just call
   it.

That third one is the real reason and it is worth saying twice. A function is a way of
making a complicated thing simple by giving it a name. `print()` is a function. They
have been using functions since unit 00.

## 2. Parameters (the name in the definition that receives the value)

A function that does the same thing every time is not very useful. Parameters let you
hand it data.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ada")
greet("Grace")
```

The terminology, briefly. The name in the definition is a parameter. The value you pass
when calling is an argument. Beginners mix these up constantly and nobody actually
cares, so introduce both words once and do not insist on them.

The important details.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ada")
```

When `greet("Ada")` runs, `name` becomes `"Ada"` inside the function. It is a variable
that starts out holding whatever you passed.

Have them call it with a number instead, `greet(42)`, and see that it works anyway,
because f-strings convert anything to text. Then have them write a function that does
arithmetic with the parameter, and see what happens if they pass a string.

```python
def double(number):
    print(number * 2)

double(5)       # 10
double("ab")    # abab
double("5")     # 55
```

That last one is worth a minute. It is the `input()` type problem from unit 02 appearing
in a new place. The function did exactly what it was told, and the problem was the type
of what it was given.

### More than one parameter

```python
def describe(name, age):
    print(f"{name} is {age} years old")

describe("Ada", 36)
```

Commas separate them, and the order matters. `describe(36, "Ada")` gives a silly result
rather than an error, which shows that Python does not check whether your argument order
makes sense.

### Default values (the value used when the caller does not give one)

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Ada")                  # Hello, Ada!
greet("Ada", "Good morning")  # Good morning, Ada!
greet("Ada", greeting="Hi")   # Hi, Ada!   using the name
```

Parameters with defaults must come after parameters without them. Have them try it the
other way round and read the `SyntaxError`.

The third call spells out the parameter name, which is called a keyword argument
(passing a value by naming the parameter). It is useful when there are several optional
parameters and you only want to set one. Mention it, do not drill it.

## 3. Returning values

Open [`return_values.py`](/code/06-functions/return_values.py). This is the most important part of the unit.

```python
def double(number):
    return number * 2

result = double(5)
print(result)          # 10
print(double(5) + 1)   # 11
```

`return` hands a value back to whoever called the function. That is the difference from
`print`, and it is a big one.

### Print shows a human, return gives a value to the program

The comparison to spend time on.

```python
def double_print(number):
    print(number * 2)

def double_return(number):
    return number * 2

x = double_print(5)     # prints 10, and x is None
y = double_return(5)    # prints nothing, and y is 10
```

Have them run this and print `x` and `y`. The `x` being `None` is the moment.

The restaurant version, if it helps. `print` is shouting the answer across the room.
`return` is handing the answer to the person who asked. If you plan to do anything else
with the answer, arithmetic or comparison or storing it, you need it handed to you.

The practical difference.

```python
print(double_print(5) + 1)     # TypeError, None + 1
print(double_return(5) + 1)    # 11
```

Have them run that and read the error. `None + 1` is the symptom of a missing `return`,
and it is one they will see a lot in their own code over the next few weeks. Naming it
now saves time later.

### What a function returns if you do not say

```python
def add(a, b):
    total = a + b

print(add(2, 3))     # None
```

No `return` means the function returns `None`. It computes the answer and throws it away
when the function finishes. Have them predict before running.

### `return` also ends the function

```python
def check(number):
    if number < 0:
        return "negative"
    return "not negative"
```

The moment a `return` runs, the function stops. The second `return` never runs for a
negative number. This is called an early return, and it is a very common pattern for
handling the special cases first.

```python
def check(number):
    if number < 0:
        return "negative"
    if number == 0:
        return "zero"
    return "positive"
```

That reads better than nesting (put inside another one) everything in `else` branches.
Point out that it is a style choice, and that both work.

### Returning more than one value

Mention it briefly, it comes up with dictionaries (a collection you look things up in by
name) later.

```python
def min_and_max(numbers):
    return min(numbers), max(numbers)

low, high = min_and_max([3, 1, 4, 1, 5])
print(low, high)     # 1 5
```

The comma makes a tuple (like a list that cannot be changed), which is unit 07. For now,
just note that you can do it.

## 4. Scope (which parts can see a variable)

Open [`scope.py`](/code/06-functions/scope.py).

```python
def double(number):
    result = number * 2
    return result

double(5)
print(result)      # NameError
```

`result` only exists inside the function. When the function finishes, it is gone.
Beginners find this really surprising and it is worth making them see the `NameError`.

The mental model to give. A function is its own little world. It can see the variables
you pass in as parameters, and the variables it creates, and the global ones (they exist
for the whole program) if it must. But the variables it creates do not leak out.

In reverse.

```python
message = "hello"

def show():
    print(message)      # works, it can read the global

show()                  # hello
```

```python
message = "hello"

def change():
    message = "goodbye"     # this makes a NEW local variable
    print(message)

change()                # goodbye
print(message)          # hello, unchanged
```

This surprises people, and it is worth tracing carefully. `message = "goodbye"` inside
the function creates a local variable that shadows the global one. The global is
untouched.

The rule to give them, and it is a good one. Functions should take what they need as
parameters and hand back what they produce with `return`. Do not have functions that
quietly modify things outside themselves. It makes programs hard to reason about.

Do not teach `global`. If a student finds it, tell them it exists and that using it is
usually a sign that the function should be returning a value instead.

## 5. Functions calling functions

A short but important section.

```python
def area_of_rectangle(width, height):
    return width * height

def cost_of_floor(width, height, price_per_square_metre):
    return area_of_rectangle(width, height) * price_per_square_metre

print(cost_of_floor(3, 4, 25))
```

`cost_of_floor` uses `area_of_rectangle` without knowing or caring how it works inside.
That is the point of functions, arriving in full. Build things out of things you have
already built.

Note that the definitions have to appear before the calls, but the order of definitions
among themselves does not matter as long as everything is defined before it is called.

## 6. Putting it together

Refactor (change the code without changing what it does) an earlier exercise into
functions. This is the best exercise in the unit.

Take the guessing game from unit 04, and pull it apart.

```python
import random

def get_guess():
    while True:
        text = input("Guess a number between 1 and 100: ").strip()
        if text.isdigit():
            return int(text)
        print("That is not a number, try again")

def play():
    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess = get_guess()
        attempts += 1

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"Correct! You took {attempts} attempts")
            return attempts

play()
```

Ask them to look at `play()` now. It reads almost like the description of the game. That
is the goal of functions, and it is worth saying out loud.

Then have them do the same to one of their own older exercises. Take the grade
calculator or the shopping list, and pull out a function or two. The exercise is the
refactoring, not the code.

---

## Teaching notes for this unit

**`print` versus `return` is the whole unit.** Everything else is details. Budget at
least ten minutes for the side by side comparison in section 3, and expect the `None`
from a missing `return` to appear repeatedly for the next two units. When it does, do
not explain it again. Ask "what does that function give back?" and let them check.

**The "defining does not run it" point needs to be shown.** Delete the calls, run the
file, see nothing happen. It is the difference between a recipe and cooking the meal,
and it is really not clear.

**Forgetting the brackets when calling is common and silent.** `greet` rather than
`greet()` produces no output and no error. Show it once now so they recognise it.

**Scope should be shown, not explained.** The `NameError` from `print(result)` outside
the function is the lesson. The local shadowing case in section 4 is the second lesson.

**Do not teach `global`.** It is a bad habit for beginners and the correct answer is
almost always a `return` value.

**The refactoring exercise is more valuable than any new function they could write.**
Taking working code and pulling a function out of it is a different skill from writing
new code, and it is the one that makes their programs get better rather than just
longer.

**Default arguments are lower priority.** Cover them if the session is going well, skip
them if not. Keyword arguments can wait entirely.

**A function name should be a verb or describe what it gives back.** `calculate_tax` or
`is_prime` rather than `tax` or `prime`. Naming things well is a real skill and
beginners respond well to being told the usual way.

**Preview of next unit.** They can name pieces of work. Next session they meet
dictionaries, which are the thing that makes data meaningful rather than just ordered,
and which finally make the report card exercise from unit 05 pleasant.
