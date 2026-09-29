---
title: Unit 06 exercises
sidebar:
  label: Exercises
---
For each function, ask yourself the question first. Does this need to give something
back, or does it just need to show something? Most of these need to return.

---

## Warm-ups

### 6.1 Predict the output

```python
def add(a, b):
    print(a + b)

result = add(2, 3)
print(result)
```

### 6.2 Predict the output

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

Compare 6.1 and 6.2 and say the difference out loud in one sentence.

### 6.3 Predict the output

```python
def mystery(x):
    if x > 10:
        return "big"
    return "small"

print(mystery(20))
print(mystery(5))
print(mystery(10))
```

### 6.4 Find the bug

This is meant to work out the area of a rectangle. Calling it gives `None`.

```python
def area(width, height):
    result = width * height

print(area(3, 4))
```

### 6.5 Find the bug, part two

This is meant to print the total price including tax. It crashes.

```python
def with_tax(price):
    print(price * 1.15)

total = with_tax(20) + 5
print(total)
```

### 6.6 Scope

```python
def make_name:
    name = "Ada"

make_name
print(name)
```

What happens, and why?

---

## Core

### 6.7 Celsius to Fahrenheit

Write a function `to_fahrenheit(celsius)` that returns the fahrenheit value. Then call
it three times with different values and print the results.

Notice that the function does not print anything. That is on purpose. Printing is the
caller's job.

### 6.8 Even or odd, as a function

Write `is_even(number)` that returns `True` or `False`, not a string. Then use it in a
loop to print only the even numbers from 1 to 20.

A function that answers a yes or no question and returns a real boolean (a value that is
True or False) is one of the most useful shapes a function can have.

### 6.9 Biggest of three, as a function

Write `biggest(a, b, c)` that returns the largest. Do not use `max()`. Then use it to find
the biggest of three numbers the user enters.

This is exercise 3.6 wrapped in a function. The logic is the same, and now it can be
called whenever you like.

### 6.10 Greeting with a default

Write `greet(name, greeting="Hello")` that returns a greeting string, not prints it.
Call it once with one argument and once with two.

Then call it with `greeting` as a keyword argument (passing a value by naming the
parameter) and see that it works.

### 6.11 BMI

Write `bmi(weight, height)` that returns the BMI value.

Then write `bmi_category(value)` that takes a BMI and returns the category string from
exercise 3.11.

Then write a short program that asks for weight and height, works out the BMI, and
prints the category, using both functions.

Notice how the main program is now three lines instead of fifteen.

### 6.12 Count vowels, as a function

Write `count_vowels(text)` that returns the number of vowels in the text. Then ask the
user for a sentence and print the count using the function.

Then write `count_letters(text, letter)` that counts any letter. Then rewrite
`count_vowels` so that it uses `count_letters`. That is a function using a function.

### 6.13 Statistics

Write `statistics(numbers)` that takes a list and returns three things, the smallest,
the largest, and the average.

Remember that a function can return several values at once by separating them with
commas. Then unpack them on the other side.

Test it with an empty list and see what happens. Decide what you think it should do,
then make it do that.

### 6.14 Squares list

Write `squares_up_to(n)` that returns a list of the squares from 1 to n. So
`squares_up_to(4)` returns `[1, 4, 9, 16]`.

This is the accumulator pattern from unit 05, inside a function. Notice that the
function must create the list itself, and that the list has to be returned or it
disappears when the function ends.

### 6.15 Is it a prime, as a function

Write `is_prime(number)` that returns `True` or `False`. Do not print anything inside
it.

Then use it to print all the primes below 50.

This is exercise 4.15 wrapped in a function, and it is much more useful this way because
now you can call it inside a loop.

### 6.16 Menu

Write a program with four functions, one for each option, and a menu that asks the user
which one they want. Run it in a `while True` loop until they choose to quit.

Options, pick your own.

```
1. Celsius to Fahrenheit
2. Biggest of three
3. Count vowels
4. Quit
```

Keep the main part of the program short. It should mostly be calling functions, not
doing work itself.

---

## Stretch

### 6.17 Refactor the grade calculator

Take your solution to exercise 3.11 or the grade calculator from unit 03 and pull out
functions. A good target is a `letter_grade(score)` function and a `print_report(name,
score)` function.

The final program should read like a description of what it does, with almost no logic
in the main part.

Do the same for the shopping list from exercise 5.6. That one is harder, and the
functions may need to take a list as a parameter (the name in the definition that
receives the value) and return a new list.

### 6.18 Debugging by cutting down

Here is a function with a bug. It is meant to return the number of words in the sentence
that are longer than three characters.

```python
def count_long_words(sentence):
    words = sentence.split
    count = 0
    for word in words:
        if len(word) > 3:
            return count
        count += 1
    return count
```

Find the bug by reducing it to a tiny case. Call it with `"a bb ccc dddd"` and work out
what it should return, then trace what it actually does.

Then fix it, and explain what the `return` was doing in the wrong place.

### 6.19 Recursion, a first look

You have not been taught this, and it is not required. A function can call itself.

```python
def countdown(n):
    if n <= 0:
        print("Liftoff")
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

Trace this by hand and convince yourself that it stops. The key question is what stops
it, and why the function does not run forever.

Then rewrite it as a loop. Both versions are correct, and the loop version is usually
easier to read.

### 6.20 Functions that take functions

This is well beyond what you need, and it is here because it is a real thing you will
see. Python lets you pass a function as an argument.

```python
def apply_twice(func, value):
    return func(func(value))

def double(n):
    return n * 2

print(apply_twice(double, 5)) # 20
```

Work out what `apply_twice(double, 5)` does step by step. Then try it with an `add_one`
function of your own.

You met this idea already in exercise 5.14 with `sorted(words, key=len)`. `len()` was
being passed around as a value, exactly like `double` here.

---

## Before next session

Be able to do these without notes.

- Define a function with parameters and call it.
- Explain the difference between printing and returning.
- Say what a function returns when you forget the `return`.
- Explain why a variable created inside a function does not exist outside it.
- Write a program that is mostly a set of small functions being called in order.
