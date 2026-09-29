# Unit 01 exercises

Work through these in order. Warm-ups are meant to be quick and to be done together.
Core ones are yours to work out. Predict before you run, every time.

---

## Warm-ups

### 1.1 Predict the output

Do not run these. Write down what each one prints, then check.

```python
a = 5
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

### 1.2 Predict the output, part two

```python
x = 10
x = 20
x = x + 5
print(x)
```

### 1.3 What is the type?

Write down `int`, `float` or `str` for each one, then check with `type()`.

- `42`
- `42.0`
- `"42"`
- `"hello"`
- `True`
- `7 / 2`

---

## Core

### 1.4 Age in the year 2100

Make a variable `birth_year` set to your birth year, and a variable `current_year` set
to 2026. Work out how old you will be in 2100 and print a sentence about it using an
f-string.

Example output shape, yours will differ.

```
In 2100 I will be 104 years old.
```

### 1.5 Temperature conversion

Celsius to Fahrenheit uses this formula.

```
fahrenheit = celsius * 9 / 5 + 32
```

Store a celsius temperature in a variable, work out the fahrenheit, and print both,
rounded to one decimal place.

Then change the celsius value and run it again without touching anything else.

### 1.6 Split a bill

Three friends share a bill of 187.50 and want to leave a 12 percent tip. Work out the
tip, the total including the tip, and what each person pays. Print all three with two
decimal places.

Watch out for operator precedence, which means which operation happens first, in `total
* 12 / 100`. Work it out on paper first, then check.

### 1.7 Seconds into hours and minutes

Given `total_seconds = 7385`, print how many hours, minutes and seconds that is. You
will need `//` and `%`, and you will need to be careful about the order you do things
in.

Expected output.

```
2 hours, 3 minutes, 5 seconds
```

### 1.8 Swap two variables

Start with this.

```python
a = "first"
b = "second"
```

Make it so that `a` holds `"second"` and `b` holds `"first"`, then print both.

There are two ways to do this. One of them needs a third variable and is worth working
out because the reasoning is useful. The other is a special Python trick. Try to find
the one with a third variable first.

### 1.9 Broken code

The following is meant to print the price of 4 items at 12.50 each. It has three
mistakes. Find them all before running anything, then fix them one at a time.

```python
Item price = 12.50
quantity = 4
total = item_price * Quantity
print(f"Total: {total)
```

---

## Stretch

### 1.10 Pizza maths

A pizza place sells small pizzas of radius 10 and large pizzas of radius 15. Both cost
12 dollars. Work out the area of each with `3.14159 * radius ** 2` and print both areas
and which one is better value per square centimetre.

### 1.11 Days, hours, minutes, seconds

Take a large number of seconds, say `1000000`, and break it into days, hours, minutes
and seconds. Print the result.

```
1000000 seconds is 11 days, 13 hours, 46 minutes and 40 seconds
```

This is the hardest of the arithmetic exercises. Write down the steps in English before
writing any code. It is the same pattern as the hours and minutes one, applied four
times.

### 1.12 The silent bug

Take your answer to 1.6 and change this line

```python
print(f"Each person pays {each:.2f}")
```

into this

```python
print(f"Each person pays each:.2f")
```

Run it. There is no error. Explain out loud what happened and why this kind of bug is
more dangerous than the ones that produce an error message.

---

## Before next session

Be able to do these without notes.

- Make a variable, change it, and print the new value.
- Use `//` and `%` to split a number into parts.
- Print a sentence containing a variable and a calculation using an f-string.
- Say what `type()` returns for `5`, `5.0` and `"5"`, and why that matters.
