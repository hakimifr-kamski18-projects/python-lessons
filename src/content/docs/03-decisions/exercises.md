---
title: Unit 03 exercises
sidebar:
  label: Exercises
---
Predict before you run. Read your conditions out loud as sentences.

---

## Warm-ups

### 3.1 Predict the boolean

Write down `True` or `False` for each, then check them in the Python console.

```python
10 > 5
10 > 10
10 >= 10
"a" == "A"
"a"!= "A"
3 * 2 == 6
not (5 > 3)
5 > 3 and 2 > 4
5 > 3 or 2 > 4
```

### 3.2 Spot the bug

This is meant to check whether someone is old enough to drive, in a country where the
age is 17. It prints the wrong thing for a 15 year old.

```python
age = int(input("Age: "))

if age >= 17 or age < 17:
    print("Can drive")
```

Explain in your own words why it is always wrong, and fix it.

### 3.3 Spot the second bug

This is meant to say whether a number is between 1 and 10. It says yes for the number
50.

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

Ask for an age and print the price. Test every boundary, that is 4, 5, 17, 18, 64 and
65. Boundary testing is a habit worth building now.

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

A triangle with sides 3, 4 and 5 works. Sides 1, 2 and 10 do not.

### 3.11 BMI category

Ask for a weight in kilograms and a height in metres. Work out the BMI, which is weight
divided by the square of the height. Then print the category.

- Under 18.5, underweight
- 18.5 to 24.9, normal
- 25 to 29.9, overweight
- 30 and over, obese

Print the BMI itself to one decimal place as well.

### 3.12 Yes or no, properly

Ask a yes or no question. Accept `y`, `yes`, `Y`, `YES`, ` yes ` and the same for no.
Anything else, ask them again... actually you cannot loop yet, so instead print "I did
not understand".

This is exercise 2.4 done properly, and it is where the `or` trap from the lesson shows
up. Use the list form.

---

## Stretch

### 3.13 Leap year

Ask for a year and print whether it is a leap year. The rules are.

- Divisible by 4, it is a leap year
- Unless it is also divisible by 100, then it is not
- Unless it is also divisible by 400, then it is

So 2024 is, 1900 is not, and 2000 is.

This one is worth doing slowly. Write the rule in English first, in three sentences,
then translate. Getting it wrong the first time and testing 1900 and 2000 is the actual
lesson.

### 3.14 Income tax

Ask for an annual income and work out the tax, using these brackets.

- The first 10000 is tax free
- The next 20000 is taxed at 20 percent
- Anything above 30000 is taxed at 40 percent

So an income of 50000 pays 0 on the first 10000, 20 percent of 20000 which is 4000, and
40 percent of 20000 which is 8000, for a total of 12000.

Test with 5000, 10000, 30000 and 50000 to make sure the boundaries behave.

This is the hardest exercise in the unit. It is not conceptually hard, but there are a
lot of numbers and it is easy to be off by one. Do the arithmetic on paper first.

### 3.15 Rock paper scissors

Ask two players for their choices, player one first then player two. Print who wins, or
that it is a draw.

The rules are the ones you remember. Rock beats scissors, scissors beats paper, paper
beats rock.

Then think about this question. How many `if` statements did you need, and could you
have done it with fewer by writing the conditions differently? There is no single right
answer, but a version that checks "does player one beat player two" once and handles the
draw first is much shorter than one that enumerates all nine combinations.

---

## Before next session

Be able to do these without notes.

- Write an `if`, `elif`, `else` chain from a blank file.
- Say out loud what `=` and `==` each mean.
- Explain why `if x == 1 or 2` is always true.
- Test a range with a chained comparison like `0 <= x <= 10`.
