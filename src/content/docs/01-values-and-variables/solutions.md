---
title: Unit 01 solutions
sidebar:
  label: Solutions
---
## Warm-ups

### 1.1 Predict the output

```python
a = 5
b = 2
print(a + b) # 7
print(a - b) # 3
print(a * b) # 10
print(a / b) # 2.5 <- float, always
print(a // b) # 2 <- whole times 2 fits into 5
print(a % b) # 1 <- what is left over
print(a ** b) # 25 <- 5 to the power 2
```

Two of these are the ones worth checking. `a / b` gives `2.5` rather than `2`, because
`/` always produces a float. And `a // b`, `a % b` come as a pair. `2` times 2 is 4, and
1 is left over, which is exactly `5 = 2 * 2 + 1`.

### 1.2 Predict the output

It prints `25`.

Line by line. `x` gets 10. Then `x` gets 20, replacing the 10 entirely, because a
variable holds one value at a time. Then `x = x + 5` reads the current 20, works out 25,
and stores it back. So the final value is 25.

The common wrong answer is 35. If you got 35, you added all three values together.
Assignment replaces, it does not accumulate. If you got
15, you worked down from 10 and ignored the middle line, which is a different and
equally instructive mistake about reading order.

### 1.3 What is the type?

| Value | Type | Why |
| --- | --- | --- |
| `42` | `int` | whole number, no decimal point |
| `42.0` | `float` | has a decimal point, even though the value is whole |
| `"42"` | `str` | quoted, so it is text, not a number |
| `"hello"` | `str` | quoted |
| `True` | `bool` | capitalised, and it is a keyword |
| `7 / 2` | `float` | division always gives float, even when it divides evenly |

The middle row and the last row are the interesting ones. `42.0` being a float surprises
people, since it is a whole number. But type is about how the value is written, not
about its mathematical value.

And `7 / 2` giving `3.5` is expected, but `4 / 2` giving `2.0` is worth checking too,
since students often assume exact division stays an int.

---

## Core

### 1.4 Age in 2100

```python
birth_year = 1990
current_year = 2026
age_now = current_year - birth_year
age_in_2100 = 2100 - birth_year

print(f"In 2100 I will be {age_in_2100} years old.")
```

The only thing to check here is that you used an f-string rather than gluing with `+`.
If you wrote `print("In 2100 I will be " + age_in_2100 + " years old.")` that is a
`TypeError`, since you cannot add a number to a string. Hit it and fix it with
`str`, then use the f-string version as the better way.

### 1.5 Temperature conversion

```python
celsius = 37
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}C is {fahrenheit:.1f}F")
```

Output for 37 is `37C is 98.6F`.

This one is a precedence trap. `celsius * 9 / 5 + 32` is evaluated left to right for the
multiplication and division, then the addition, giving the right answer. But a student
who writes `celsius * 9 / (5 + 32)` gets something wildly wrong. That is the point of
the exercise. Explain why the brackets change everything.

### 1.6 Split a bill

```python
bill = 187.50
tip_rate = 12

tip = bill * tip_rate / 100
total = bill + tip
each = total / 3

print(f"Bill: {bill:.2f}")
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
print(f"Each: {each:.2f}")
```

Output.

```
Bill: 187.50
Tip: 22.50
Total: 210.00
Each: 70.00
```

On precedence. `bill * tip_rate / 100` multiplies first then divides, which is correct.
Writing `bill * (tip_rate / 100)` gives the same answer. Writing `bill * tip_rate / 100`
is fine. The one that breaks is if you try `bill + tip_rate / 100` by mistake, which
adds 0.12 to the bill.

If you wrote `tip_rate = 0.12` instead and forgot the `/ 100`, that also works, and it
is arguably cleaner. Both are acceptable. What matters is that you can say which you
did and why.

### 1.7 Seconds into hours and minutes

```python
total_seconds = 7385

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
```

Output is `2 hours, 3 minutes, 5 seconds`.

The reasoning, which is worth working through since it is the pattern for a lot of later
exercises.

1. An hour is 3600 seconds. `7385 // 3600` gives 2, the number of whole hours.
2. What is left over is `7385 % 3600`, which is 185 seconds.
3. A minute is 60 seconds. `185 // 60` gives 3 whole minutes.
4. What is left is `185 % 60`, which is 5 seconds.

Note the shape of step 2 and 3 together. `(total_seconds % 3600) // 60` takes the
leftover after removing hours and then counts minutes in it. Students often write
`total_seconds // 60 % 60` instead, which gives the same answer for this input. Both are
correct. Use whichever you can explain.

The `seconds` line can just be `total_seconds % 60`, because after removing whole hours
and whole minutes, the leftover seconds are already what is left. Worth noticing
that the answer came out of the structure of the problem rather than from a formula you
had to memorise.

### 1.8 Swap two variables

The version with a third variable, which is the one to work out first.

```python
a = "first"
b = "second"

temp = a
a = b
b = temp

print(a) # second
print(b) # first
```

The reasoning matters more than the code. If you do `a = b` first, you have overwritten
`a` and lost the value you needed. So you hold one value in a spare variable before
overwriting anything. Try the broken order first

```python
a = b
b = a
```

and see that both end up holding `"second"`. That failure is the lesson.

The Python trick.

```python
a = "first"
b = "second"

a, b = b, a

print(a) # second
print(b) # first
```

This works because Python evaluates the whole right side before assigning anything, so
both values are read before either is overwritten. Think of it as "Python holds the old
value for you". Do not use this in exercises until you understand the three
line version, since the three line version is the one that transfers to other languages.

### 1.9 Broken code

Here is the broken version again.

```python
Item price = 12.50
quantity = 4
total = item_price * Quantity
print(f"Total: {total)
```

The three mistakes.

**One. `Item price` has a space in it.** Variable names cannot contain spaces. This is a
`SyntaxError`, so nothing runs at all. The fix is an underscore, giving `item_price`.

This mistake is why the next line fails too. `item_price` on line 3 is a `NameError`,
not because line 3 is wrong in itself, but because the variable was never successfully
created. A good illustration of how one error can produce a second, misleading error
further down.

**Two. `Quantity` has a capital Q.** The variable was defined as `quantity`. Python is
case sensitive, so `Quantity` is a different name that does not exist. This is another
`NameError`.

**Three. The f-string is not closed properly.** `f"Total: {total)` has a `)` where there
should be a `}` and then a closing `"`. This is a `SyntaxError`. It should read
`f"Total: {total}"`.

The fixed version.

```python
item_price = 12.50
quantity = 4
total = item_price * quantity
print(f"Total: {total:.2f}")
```

Output is `Total: 50.00`.

Worth noting the ordering of the fixes. Since mistakes one and three are syntax errors,
the program refuses to run at all until both are fixed, and the `NameError` for
`Quantity` only becomes visible after that. This is a good lesson in the fact that you
often cannot see all the problems at once. Fix, rerun, look again.

---

## Stretch

### 1.10 Pizza maths

```python
small_radius = 10
large_radius = 15
price = 12

small_area = 3.14159 * small_radius ** 2
large_area = 3.14159 * large_radius ** 2

print(f"Small: {small_area:.2f} square units, {small_area / price:.2f} per dollar")
print(f"Large: {large_area:.2f} square units, {large_area / price:.2f} per dollar")
print("The large is better value per square unit.")
```

Output.

```
Small: 314.16 square units, 26.18 per dollar
Large: 706.86 square units, 58.90 per dollar
```

The answer is the large, by a lot, because area grows with the square of the radius.
Doubling the radius quadruples the area. At one and a half times the radius, the large
has about 2.25 times the area for the same price.

The interesting part of this exercise is `small_radius ** 2` versus `(3.14159 *
small_radius) ** 2`. The second is a common mistake and gives a totally different
answer, so it is worth trying both and comparing. Precedence again.

### 1.11 Days, hours, minutes and seconds

```python
total = 1000000

days = total // 86400
hours = (total % 86400) // 3600
minutes = (total % 3600) // 60
seconds = total % 60

print(f"{total} seconds is {days} days, {hours} hours, {minutes} minutes and {seconds} seconds")
```

Output.

```
1000000 seconds is 11 days, 13 hours, 46 minutes and 40 seconds
```

The reasoning, same shape as 1.7 applied four times.

1. A day is 86400 seconds. `1000000 // 86400` is 11, so 11 days.
2. Left over is `1000000 % 86400`, which is 49600 seconds.
3. An hour is 3600. `49600 // 3600` is 13 hours.
4. Left over is `49600 % 3600`, which is 2800 seconds.
5. A minute is 60. `2800 // 60` is 46 minutes.
6. Left over is `2800 % 60`, which is 40 seconds.

Notice that the minutes line uses `total % 3600` rather than `total % 86400`. Both work,
since the extra days removed by the larger modulo divide evenly into hours anyway. This
is exactly the kind of thing where you should pick one form and be able to
justify it, rather than worry about which is "right".

A sanity check worth doing. If the leftover values came out negative or larger than
they should be, something is wrong. Hours should be under 24, minutes under 60, seconds
under 60. Saying that out loud before checking is a good habit.

### 1.12 The silent bug

```python
print(f"Each person pays each:.2f")
```

This prints literally

```
Each person pays each:.2f
```

No error at all. The braces were removed, so `each` is just a word in the text and `.2f`
is just characters. Python has no way to know that you meant a variable there, because
as far as it is concerned the string is entirely literal text.

Why this is more dangerous than an error message. When code crashes, you know
immediately, you get a line number, and the fix is usually close by. When code silently
does the wrong thing, you might not notice for a long time, and if you do notice, the
output gives you no clue about where to look. It could be this line, or a wrong
calculation ten lines earlier.

The habit to build in response. When output is wrong but there is no error, do not stare
at the output. Go to the print statement and read it character by character, checking
that every value you expect to be interpolated is actually inside braces. This is why
`f"Forgot the braces: name is name"` from [`fstrings.py`](/code/01-values-and-variables/fstrings.py) is in the lesson file.

The wider lesson, worth remembering. Errors that crash are your friends. Errors that do
not are the ones to be careful about.
