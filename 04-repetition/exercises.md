# Unit 04 exercises

For every loop in this set, trace it on paper before you run it. Write down the value of
the variable on each pass. That is not optional while you are learning this, and it is
faster than guessing and rerunning.

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

The last one is a valid question. What does a range from 2 to 2 give?

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

This is meant to print the numbers 5 down to 1. It never stops. Find both problems and
fix them.

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

Ask for a number and print a countdown from it down to 1, then print "Lift off".

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
them up as you go. At the end print the total and the average.

Average to two decimal places.

### 4.9 Count the vowels

Ask for a sentence and print how many vowels it contains.

Careful with case. `a` and `A` should both count.

### 4.10 FizzBuzz

The most famous exercise in beginner programming. Print the numbers 1 to 100, but.

- If the number is divisible by 3, print `Fizz` instead
- If it is divisible by 5, print `Buzz` instead
- If it is divisible by both, print `FizzBuzz`
- Otherwise print the number

The trap is the order of the checks. Think about which condition has to come first, and
why. Print the first 20 and check them against what you expect before printing all 100.

### 4.11 Letter pyramid

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

The centring needs the trick from unit 02, `" " * n`, and a bit of thinking about how
many spaces each row needs.

### 4.12 Multiplication table grid

Print a full 1 to 5 times table, showing every product from 1x1 to 5x5. This needs a
loop inside a loop.

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

Write the guessing game from the lesson yourself, without looking at it. Then add one
thing. If the user enters something that is not a number, ignore it and ask again
instead of crashing.

The second part is hard without what comes in unit 08, so here is a hint. You can check
whether a string is made of digits with `.isdigit`, which gives back `True` or `False`.
Use that before converting.

### 4.14 Sum of digits

Ask for a whole number, and add up its digits. So `472` gives `13`, because 4 plus 7
plus 2 is 13.

You can do this with `%` and `//` in a `while` loop, taking off one digit at a time, or
by treating the number as a string and looping over the characters. Try the string way
first, since it is easier, then try the arithmetic way.

---

## Stretch

### 4.15 Prime check

Ask for a number and print whether it is prime. A prime is only divisible by 1 and
itself.

The naive way is to check every number from 2 up to one less than the number. Once that
works, think about how much of that work is necessary. If you have checked up to the
square root, is there anything left to check?

### 4.16 Factorial

Ask for a number and print its factorial. The factorial of 5 is 5 times 4 times 3 times
2 times 1, which is 120.

Then try it with 20. Compare the answer with `2 ** 100` from unit 01 and see how big the
numbers get. Python handles it fine, which is not true of every language.

### 4.17 Fibonacci

Print the first 20 numbers of the Fibonacci sequence , where each number is the sum of
the two before it. It starts 1, 1, 2, 3, 5, 8, 13.

You will need two variables that you update on each pass. Think carefully about the
order of the updates, because doing it in the wrong order loses one of the values. If
you get stuck, the three-variable swap trick from exercise 1.8 is the answer.

### 4.18 Collatz

Start with any whole number. Repeat these rules until you reach 1.

- If it is even, halve it
- If it is odd, multiply by 3 and add 1

So starting at 6 you get 6, 3, 10, 5, 16, 8, 4, 2, 1. That is 8 steps.

Ask for a starting number and print every value in the sequence and how many steps it
took. No one has ever found a starting number that does not eventually reach 1, and no
one has proved that none exists. That is a real open problem in mathematics, which is a
fun thing to tell a beginner.

Careful, the loop needs `while number!= 1` rather than a `for`, because you do not know
in advance how many steps there will be. That is exactly the situation `while` is for.

---

## Before next session

Be able to do these without notes.

- Write a `for` loop with `range()` that prints 1 to 10.
- Explain why `range(1, 5)` stops at 4.
- Sum a series of numbers inside a loop.
- Write `while True` with a `break` for a loop that ends when the user says so.
- Say out loud what `break` does and what `continue` does.
