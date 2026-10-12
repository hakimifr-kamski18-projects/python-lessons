---
title: Unit 04 exercises
sidebar:
  label: Exercises
---
For every loop in this set, trace it on paper before you run it. To trace a loop means
to follow it step by step and write down the value of the variable on each pass. Do this
while you are learning, because it is faster than guessing and rerunning.

---

## Before you start

A loop runs the same lines of code again and again. Each run of the lines is one pass.

A `while` loop checks its condition before every pass. If the condition is `True`, the
lines inside run once. Then Python checks again. When the condition is `False`, the loop
ends.

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1
```

Trace it: `count` is 1, so print 1 and `count` becomes 2. Then 2, so print 2 and `count`
becomes 3. Then 3, so print 3 and `count` becomes 4. Now `4 <= 3` is `False` and the loop
ends. A `while` loop needs a line inside that changes what the condition looks at. If
nothing changes it, the loop never ends. This is called an infinite loop. To stop a
runaway program, press the Stop button next to Run, or press Ctrl and C in the terminal.

A `for` loop walks through a series of values, one per pass. `range()` makes a series of
numbers. It starts at the first number and stops before the last one.

```python
for i in range(1, 4):
    print(i)
```

This prints 1, 2, 3 and not 4. `range(5)` means 0 to 4. `range(2, 11, 2)` counts in steps
of 2. A negative step counts down, and `range(5, 0, -1)` gives 5, 4, 3, 2, 1. To see the
numbers of a range, use `list(range(3))`, which turns the range into a list you can
print. A `for` loop can also walk through the letters of a string, as in
`for letter in "hi":`.

Two keywords change a pass. `break` leaves the loop at once. `continue` skips the rest of
the current pass and goes on to the next one.

---

## Warm-ups

### 4.1 What does range give?

Write down what each of these produces, then check with `list()`.

```python
range(3)
range(1, 4)
range(0, 10, 3)
range(5, 0, -1)
range(2, 2)
```

The last one is not a trick question. What does a range from 2 to 2 give?

### 4.2 Trace this loop

Do not run it. Write down the value of `total` after every pass, then say what it
prints.

```python
total = 0
for i in range(1, 4):
    total = total + i * 2
print(total)
```

### 4.3 Find the infinite loop

This is meant to print the numbers 5 down to 1. It never stops. Find the bug and
fix it.

```python
count = 5

while count >= 1:
    print(count)
    count = count + 1
```

### 4.4 Predict break and continue

```python
for i in range(1, 8):
    if i == 3:
        continue
    if i == 6:
        break
    print(i)
```

### 4.5 How many times?

Without running anything, say how many times the body of each loop runs.

```python
for i in range(10):
    print(i)
```

```python
for i in range(1, 10):
    print(i)
```

```python
for i in range(0, 10, 2):
    print(i)
```

```python
for i in range(5, 0, -1):
    print(i)
```

---

## Core

### 4.6 Countdown

Ask for a number and print a countdown from it down to 1, then print "Lift off!".

You will need `range()` with a negative step, or a `while` loop.

### 4.7 Times table

Ask for a number and print its times table from 1 to 12.

```
7 x 1 = 7
7 x 2 = 14
...
7 x 12 = 84
```

### 4.8 Sum and average

Ask how many numbers the user wants to enter, then ask for that many numbers, adding
them up as you go. At the end print the total and the average, each to two decimal
places. If the user asks for 0 numbers, print a message instead of crashing.

### 4.9 Count the vowels

Ask for a sentence and print how many vowels it contains.

Careful with case. `a` and `A` should both count. Remember that a `for` loop can walk
through the letters of a string.

### 4.10 FizzBuzz

The most famous exercise in beginner programming. Print the numbers 1 to 100, with these rules:

- If the number is divisible by 3, print `Fizz` instead
- If it is divisible by 5, print `Buzz` instead
- If it is divisible by both, print `FizzBuzz`
- Otherwise print the number

The trap is the order of the checks. Think about which condition has to come first, and
why. Print the first 20 and check them against what you expect before printing all 100.

### 4.11 Star triangle and pyramid

Ask for a number and print a pyramid of stars with that many rows.

```
*
**
***
****
*****
```

Then, as a second version, centre it so it looks like a proper pyramid.

```
    *
   **
  ***
 ****
*****
```

The centring needs a string times a number, which repeats the string, as in `"ab" * 3`
from unit 00. Use `" " * n` for the spaces. You also need to work out how many spaces
each row needs.

### 4.12 Multiplication table grid

Print a full 1 to 5 times table, showing every product from 1x1 to 5x5. This needs a
loop inside a loop. The inner loop runs completely for every pass of the outer loop.

```python
for row in range(1, 3):
    for column in range(1, 4):
        print(row, column)
```

This prints `1 1`, `1 2`, `1 3`, `2 1`, `2 2`, `2 3`. To keep several values on one
line, use `print(value, end="")`, which stops `print` from starting a new line. A plain
`print()` then starts the new line.

Expected shape, roughly.

```
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25
```

Getting the columns to line up is the annoying part. Do not worry too much about it, but
if you want to try, look up how to pad a number inside an f-string.

### 4.13 Guess the number

Write a number guessing game. It must do this:

- The program picks a secret whole number from 1 to 100.
- It asks the user for a guess, again and again.
- If the guess is too low, print `Too low`. If it is too high, print `Too high`.
- It counts the guesses.
- When the guess is right, print how many guesses it took, and stop.

To pick the secret number, put `import random` at the top of the file. Then
`random.randint(1, 100)` gives a whole number from 1 to 100, and both 1 and 100 can
come up.

When that works, add one thing. If the user enters something that is not a number,
ignore it and ask again instead of crashing. A wrong entry should not count as a guess.

The second part is hard without what comes in unit 08, so here is a hint. You can check
whether a string is made of digits with `.isdigit()`, which gives back `True` or `False`.
Use that before converting.

### 4.14 Sum of digits

Ask for a whole number, and add up its digits. So `472` gives `13`, because 4 plus 7
plus 2 is 13.

You can do this with `%` and `//` in a `while` loop, taking off one digit at a time, or
by treating the number as a string and looping over the characters (a `for` loop can
walk through a string). Try the string way
first, since it is easier, then try the arithmetic way.

---

## Stretch

### 4.15 Prime check

Ask for a number and print whether it is prime. A prime is only divisible by 1 and
itself.

The naive way is to check every number from 2 up to one less than the number. Once that
works, think about how much of that work is necessary. If you have checked up to the
square root, is there anything left to check? In Python, `number ** 0.5` is the square
root. `range()` needs a whole number, so wrap it in `int()`.

### 4.16 Factorial

Ask for a number and print its factorial. The factorial of 5 is 5 times 4 times 3 times
2 times 1, which is 120.

Then try it with 20. Compare the answer with `2 ** 100`, which you can type in the console, and see how big
the numbers get. Python handles it fine, which is not true of every language.

### 4.17 Fibonacci

Print the first 20 numbers of the Fibonacci sequence, where each number is the sum of
the two before it. It starts 1, 1, 2, 3, 5, 8, 13.

You will need two variables that you update on each pass. Think carefully about the
order of the updates, because doing it in the wrong order loses one of the values. If
you get stuck, the three-variable swap trick from exercise 1.8 is the answer.

### 4.18 Collatz

Start with any whole number above 0. Repeat these rules until you reach 1.

- If it is even, halve it
- If it is odd, multiply by 3 and add 1

So starting at 6 you get 6, 3, 10, 5, 16, 8, 4, 2, 1. That is 8 steps.

Ask for a starting number and print every value in the sequence and how many steps it
took. No one has ever found a starting number that does not eventually reach 1, and no
one has proved that none exists. That is a real open problem in mathematics.

Careful, the loop needs `while number != 1` rather than a `for`, because you do not know
in advance how many steps there will be. That is exactly the situation `while` is for.

---

## Check yourself

Try to do these without notes.

- Write a `for` loop with `range()` that prints 1 to 10.
- Explain why `range(1, 5)` stops at 4.
- Sum a series of numbers inside a loop.
- Write `while True` with a `break` for a loop that ends when the user says so.
- Say to yourself what `break` does and what `continue` does.
