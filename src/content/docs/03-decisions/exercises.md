---
title: Unit 03 exercises
sidebar:
  label: Exercises
---
Predict before you run. Read your conditions to yourself as sentences. Say `==` as "is
equal to" and `=` as "gets". In an `if`, `elif`, `else` chain only the first matching
branch (the first condition that is true) runs.

---

## Before you start

Two facts explain the bug in exercise 3.12 and the last question of this page.

First, `or` joins two complete conditions. This does not do what it looks like:

```python
answer = "no"

if answer == "yes" or "y":
    print("Continuing")
```

Python reads it as `(answer == "yes") or ("y")`. The second part, `"y"`, is not a
question. It is just a value. Any text that is not empty counts as true, and so does any
number except 0. So `"y"` is always true, and the whole condition is always true. The
code above prints "Continuing" even though the answer is "no". Try it.

You can see how Python judges a value with `bool()`:

```python
print(bool("y"))   # True
print(bool(""))    # False
print(bool(5))     # True
print(bool(0))     # False
```

Second, to ask "is this value one of several choices", use `in` with a list (a group of
values in square brackets):

```python
answer = "y"

if answer in ["y", "yes"]:
    print("You agreed")
```

This means "is `answer` one of these". It is shorter than writing `answer == "y" or
answer == "yes"` and it avoids the trap above.

---

## Warm-ups

### 3.1 Predict the boolean

Write down `True` or `False` for each, then check them in the Python console.

```python
10 > 5
10 > 10
10 >= 10
"a" == "A"
"a" != "A"
3 * 2 == 6
not (5 > 3)
5 > 3 and 2 > 4
5 > 3 or 2 > 4
```

### 3.2 Spot the bug

This is meant to check whether someone is old enough to drive, in a country where the
age is 17. It prints "Can drive" for everyone, even a 15 year old.

```python
age = int(input("Age: "))

if age >= 17 or age < 17:
    print("Can drive")
```

Explain in your own words why it always prints "Can drive", and fix it.

### 3.3 Spot the second bug

This is meant to say whether a number is between 1 and 10. The numbers 1 and 10 are not
included. It says yes for the number 50.

```python
number = int(input("Number: "))

if number > 1 or number < 10:
    print("Between 1 and 10")
```

Why does it fail, and what is the fix?

### 3.4 Branch order

This is meant to grade a test. It gives a 95 a C. Fix it.

```python
score = 95

if score > 60:
    print("C")
elif score > 90:
    print("A")
else:
    print("F")
```

---

## Core

### 3.5 Even or odd

Ask for a whole number and print whether it is even or odd. You met `%` in unit 01 and
this is what it is for.

### 3.6 Biggest of three

Ask for three numbers and print the biggest one. Do not use `max()`, work it out with
comparisons.

Test it with all six orderings of the same three numbers, for example 1 2 3, 1 3 2, 2 1
3, and so on. All six must give the same answer. That is the real work of this exercise.

### 3.7 Cinema tickets

A cinema charges by age.

- Under 5, free
- 5 to 17, 8 dollars
- 18 to 64, 14 dollars
- 65 and over, 9 dollars

All ages are whole numbers.

Ask for an age and print the price. Test every boundary (a value where the answer changes), that is 4, 5, 17, 18, 64 and
65. Testing boundaries is a good habit to build now.

### 3.8 Password check

Ask for a password. Print whether it is strong, weak, or acceptable, using these rules.

- Strong, at least 12 characters
- Acceptable, at least 8 characters
- Weak, anything shorter

You will need `len()`.

### 3.9 Login

Store a username and password in variables at the top of the file. Ask the user for
both. Print "Welcome" if both match, "Wrong password" if only the username matches, and
"No such user" if the username does not match.

### 3.10 Triangle or not

Ask for three side lengths. Print whether they can form a triangle. The rule is that the
sum of any two sides must be greater than the third.

A triangle with sides 3, 4 and 5 works. Sides 1, 2 and 10 do not, and neither do 1, 2 and
3 (a flat line is not a triangle).

### 3.11 BMI category

Ask for a weight in kilograms and a height in metres. Work out the BMI, which is weight
divided by the square of the height. Then print the category.

- Under 18.5, underweight
- 18.5 up to, but not including, 25, normal
- 25 up to, but not including, 30, overweight
- 30 and over, obese

Print the BMI itself to one decimal place as well.

### 3.12 Yes or no, properly

Ask a yes or no question. Accept `y`, `yes`, `Y`, `YES`, ` yes ` and the same for no.
For anything else, print "I did not understand". You will learn to ask again in unit 04.

This is exercise 2.4 done properly, and it is where the `or` trap (see "Before you
start") shows up. Use `if answer in ["y", "yes"]`, which means "is `answer` one of
these".

---

## Stretch

### 3.13 Leap year

Ask for a year and print whether it is a leap year. The rules are:

- Divisible by 4, it is a leap year
- Unless it is also divisible by 100, then it is not
- Unless it is also divisible by 400, then it is

So 2024 is, 1900 is not, and 2000 is.

This one is worth doing slowly. Write the rule in English first, in three sentences,
then translate. Getting it wrong the first time and then testing 1900 and 2000 is where you
really learn.

### 3.14 Income tax

Ask for an annual income and work out the tax, using these brackets.

- The first 10000 is tax free
- The next 20000 is taxed at 20 percent
- Anything above 30000 is taxed at 40 percent

So an income of 50000 pays 0 on the first 10000, 20 percent of 20000 which is 4000, and
40 percent of 20000 which is 8000, for a total of 12000.

Test with 5000, 10000, 30000 and 50000 to make sure the boundaries behave.

This is the hardest exercise in the unit. It is not conceptually hard, but there are a
lot of numbers and it is easy to forget the tax from the lower brackets. Do the arithmetic on paper first.

### 3.15 Rock paper scissors

Ask two players for their choices, player one first then player two. Print who wins, or
that it is a draw.

You know the rules. Rock beats scissors, scissors beats paper, paper
beats rock.

Then think about this question. How many branches (`if`, `elif` and `else` parts) did
you need, and could you have used fewer by writing the conditions differently? There is
no single right answer, but a version that handles the draw first and then checks "does
player one win" is much shorter than one that lists all nine combinations (3 x 3).

---

## Check yourself

Try these without notes.

- Write an `if`, `elif`, `else` chain from a blank file.
- Say to yourself what `=` and `==` each mean.
- Explain why `if answer == "yes" or "y"` is always true.
- Test a range with a chained comparison like `0 <= x <= 10`.
