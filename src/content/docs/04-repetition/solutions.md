---
title: Unit 04 solutions
sidebar:
  label: Solutions
---
## Warm-ups

### 4.1 What does range give?

```python
list(range(3)) # [0, 1, 2]
list(range(1, 4)) # [1, 2, 3]
list(range(0, 10, 3)) # [0, 3, 6, 9]
list(range(5, 0, -1)) # [5, 4, 3, 2, 1]
list(range(2, 2)) # [] empty
```

The last one is empty, and that is not an error. `range(2, 2)` means "start at 2, stop
before 2", and there is nothing in between. It is empty rather than invalid. This is
worth knowing because it means a loop over an empty range simply does not run, with no
complaint, which can hide a bug.

### 4.2 Trace this loop

```python
total = 0
for i in range(1, 4):
    total = total + i * 2
```

`range(1, 4)` gives 1, 2, 3. Three passes.

```
i = 1: total = 0 + 1 * 2 = 2
i = 2: total = 2 + 2 * 2 = 6
i = 3: total = 6 + 3 * 2 = 12
```

It prints `12`.

The mistake to watch out for is getting 14, from doing `(total + i) * 2`. The precedence is
multiplication first, so `i * 2` happens before the addition. If you got 14, add
brackets and see which version you were imagining.

### 4.3 Find the infinite loop

```python
count = 5

while count >= 1:
    print(count)
    count = count + 1
```

Two problems, and both need fixing.

**The counter goes the wrong way.** `count = count + 1` moves away from the condition
rather than towards it. Since `count` keeps growing, `count >= 1` stays true forever.

**There is no way out at all.** Even if the direction were fixed, there is nothing that
ends the loop when it reaches 1.

The fix.

```python
count = 5

while count >= 1:
    print(count)
    count = count - 1
```

Or a `for` loop, which is better here since the number of passes is known.

```python
for count in range(5, 0, -1):
    print(count)
```

Worth asking yourself which you prefer and why. "The `for` version, because I cannot get
the direction wrong" is an excellent answer and a good habit to build.

### 4.4 Predict break and continue

It prints `1`, `2`, `4`, `5`.

Trace.

```
i = 1 -> not 3, not 6 -> print 1
i = 2 -> not 3, not 6 -> print 2
i = 3 -> CONTINUE, skip the rest of this pass
i = 4 -> not 3, not 6 -> print 4
i = 5 -> not 3, not 6 -> print 5
i = 6 -> BREAK, leave the loop entirely
i = 7 -> never reached
```

The `if i == 3` check comes first, so when `i` is 3 the `continue` fires and the `i ==
6` check is never even looked at. That is a good illustration of why order matters
inside a loop body too.

### 4.5 How many times?

```python
for i in range(10): # 10 times, 0 to 9
for i in range(1, 10): # 9 times, 1 to 9
for i in range(0, 10, 2): # 5 times, 0, 2, 4, 6, 8
for i in range(5, 0, -1): # 5 times, 5, 4, 3, 2, 1
```

If you said 10 for the second one, you are still thinking of the end value as
inclusive. The count of a range is `stop - start` when the step is 1, after adjusting
for the step. Just work out the values and count them rather than
memorising a formula.

---

## Core

### 4.6 Countdown

```python
number = int(input("Start from: "))

for i in range(number, 0, -1):
    print(i)

print("Lift off!")
```

For an input of 5, this prints 5, 4, 3, 2, 1, then "Lift off!".

`range(number, 0, -1)` starts at `number` and stops before 0, so it reaches 1 and not 0.
That is exactly what is wanted here. If you wrote `range(number, -1, -1)` you get 0 as
well, which is a fine answer too. Ask yourself which you intended.

A `while` version is equally acceptable and is a good way to check you can write both.

```python
number = int(input("Start from: "))
while number > 0:
    print(number)
    number -= 1
print("Lift off!")
```

### 4.7 Times table

```python
number = int(input("Number: "))

for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")
```

`range(1, 13)` gives 1 to 12, which is the off-by-one rule doing its job. `range(1, 12)`
would stop at 11 and give eleven lines, which is the mistake to watch out for.

### 4.8 Sum and average

```python
how_many = int(input("How many numbers? "))

total = 0
for i in range(how_many):
    number = float(input(f"Number {i + 1}: "))
    total += number

if how_many > 0:
    average = total / how_many
    print(f"Total: {total:.2f}")
    print(f"Average: {average:.2f}")
```

The guard `if how_many > 0` is the interesting part. Without it, entering 0 gives a
`ZeroDivisionError` on the average line. That is a really good error to hit,
because "what if the user enters zero" is exactly the kind of question you should be
asking yourself by now.

The other check is `float` rather than `int`, since you may want to enter decimals.

A version that also tracks the biggest, for extra practice.

```python
total = 0
biggest = None
```

Careful with `biggest = None` here. It works, because `None` compares as smaller than
any number, but `None` is unit 08 material. Not needed for this exercise.

### 4.9 Count the vowels

```python
sentence = input("Sentence: ").strip.lower

count = 0
for letter in sentence:
    if letter in "aeiou":
        count += 1

print(f"There are {count} vowels")
```

The `.lower` on the input handles the case problem in one move, which is neater than
checking both cases in the condition.

If you wrote `if letter in "aeiouAEIOU"` that is also correct and avoids the `.lower`.
Either is fine. What matters is that you thought about the case problem at all.

Note that `letter in "aeiou"` reuses the `in` operator
 from unit 03, which works on a string
because a string is a sequence of characters. That connection is worth noticing.

### 4.10 FizzBuzz

```python
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
```

The `and` case has to come first. If `number % 3 == 0` came first, then 15 would print
`Fizz` and the `FizzBuzz` branch would never be reached. Exactly the same ordering
problem as the grade calculator in unit 03, and worth noticing that it is the same
lesson in a different form.

The first few lines should be.

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
```

If 15 shows up as `Fizz`, the order is wrong.

### 4.11 Letter pyramid

The plain version.

```python
rows = int(input("Rows: "))

for row in range(1, rows + 1):
    print("*" * row)
```

The centred version.

```python
rows = int(input("Rows: "))

for row in range(1, rows + 1):
    spaces = " " * (rows - row)
    stars = "*" * row
    print(spaces + stars)
```

For five rows, the first row has four spaces and one star, and the last row has zero
spaces and five stars. The pattern is that the spaces count down while the stars count
up.

The reasoning to work out. Row 1 needs `rows - 1` spaces. Row `rows` needs 0. So the
number of spaces is `rows - row`. Working that out from the first and last row, rather
than being told, is the exercise.

### 4.12 Multiplication table grid

```python
size = 5

for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(f"{row * column:3}", end="")
    print()
```

Output.

```
  1 2 3 4 5
  2 4 6 8 10
  3 6 9 12 15
  4 8 12 16 20
  5 10 15 20 25
```

Two new things here.

`f"{row * column:3}"` pads the value to three characters wide, which is what makes the
columns line up. Without it, the single digit numbers take less space than the double
digit ones and everything goes ragged. This is the same formatting idea as `.2f` from
unit 01, using `:3` to mean "width three" rather than "three decimal places".

The inner loop finishes before the outer loop moves on. That is the whole idea of
nesting. Trace the first two rows by hand.

The `print()` with nothing in it at the end of the outer loop is what starts a new line
for each row. Without it, everything would come out as one long line.

### 4.13 Guess the number

```python
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    text = input("Guess a number between 1 and 100: ").strip

    if not text.isdigit:
        print("That is not a number, try again")
        continue

    guess = int(text)
    attempts += 1

    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print(f"Correct! You took {attempts} attempts")
        break
```

The interesting part is the `continue`. A bad input skips the rest of the pass, so it
does not count as an attempt and the loop just asks again. That is exactly what
`continue` is for, and it is a much better use of it than the contrived `if number == 5:
continue` examples.

`.isdigit` gives back `True` for `"42"` and `False` for `"hello"`, `"-5"` and `"4.5"`.
Note the last two. It is stricter than `int` in one direction, since `int("-5")` works
but `.isdigit` says no, and looser in others. Worth testing both. Handling
negative numbers properly would need unit 08 material.

### 4.14 Sum of digits

The string way, which is easier.

```python
text = input("Number: ").strip

total = 0
for digit in text:
    total += int(digit)

print(total)
```

The arithmetic way.

```python
number = int(input("Number: ").strip)

total = 0
while number > 0:
    total += number % 10
    number //= 10

print(total)
```

The arithmetic way deserves a trace, because it is a really nice bit of reasoning.

For 472.

```
number = 472 -> 472 % 10 = 2, add 2, total = 2
                  472 // 10 = 47
number = 47 -> 47 % 10 = 7, add 7, total = 9
                  47 // 10 = 4
number = 4 -> 4 % 10 = 4, add 4, total = 13
                  4 // 10 = 0
number = 0 -> loop ends
```

`% 10` peels off the last digit. `// 10` throws it away. Doing both repeatedly walks
through the number from right to left.

Note that this version does not work for negative numbers, since the `while number
> 0` condition fails immediately. That is fine, but noticing it is worth
a moment.

---

## Stretch

### 4.15 Prime check

The straightforward version.

```python
number = int(input("Number: "))

if number < 2:
    is_prime = False
else:
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
```

The `number < 2` check handles 0 and 1, which are not prime. That is a case people
forget, so testing 1 is worthwhile.

The `break` stops as soon as a divisor is found. Once you know a number is not prime,
there is no point looking for more divisors.

The faster version, which is the answer to the question in the exercise.

```python
for divisor in range(2, int(number ** 0.5) + 1):
```

Why this works, which is a really lovely argument. If a number has a factor bigger than
its square root, it must also have one smaller than its square root, because the two
factors multiply to give the number. So if you have found no factors up to the square
root, there are none at all.

For 97, the slow version checks 95 numbers and the fast one checks 8.

### 4.16 Factorial

```python
number = int(input("Number: "))

result = 1

for i in range(1, number + 1):
    result *= i

print(f"{number}! = {result}")
```

The accumulator starts at 1 rather than 0, because it is a multiplication. Starting at 0
would make everything zero, which is a mistake worth making once.

The guard for 0 is worth thinking about. `range(1, 1)` is empty, so the loop does not
run and the answer is 1. That happens to be correct, since 0 factorial is defined as 1.
Ask yourself whether that was on purpose or luck.

For 20, the answer is 2432902008176640000, which is about 2.4 quintillion. Compare with
`2 ** 100` from unit 01, which is about 1.27 nonillion, so much bigger still. Python
handles arbitrary precision integers, which most languages do not, and this shows it
well.

### 4.17 Fibonacci

The three variable version, which is what the exercise is steering towards.

```python
a = 1
b = 1

for i in range(20):
    print(a)
    next_value = a + b
    a = b
    b = next_value
```

Output starts `1 1 2 3 5 8 13 21 34 55...`

The order matters. If you do `a = b` before computing the next value, you have destroyed
the old `a` and lost it. So the next value has to be worked out first, before anything
is overwritten. That is exactly the same reasoning as the swap exercise in unit 01, and
it is worth noticing the connection.

The Python trick version, which is shorter and harder to read.

```python
a = 1
b = 1

for i in range(20):
    print(a)
    a, b = b, a + b
```

This works because Python works out the whole right side before assigning anything. Same
trick as `a, b = b, a` from unit 01.

Do not use this until you can explain why it works. The three line version
transfers to every language. This one only works in Python.

Note that this prints the first 20 numbers starting `1 1 2 3 5...`, which matches the
exercise. Starting from `a = 0, b = 1` gives `0 1 1 2 3...` instead. Both are common and
the exercise asked for the first, so check which you produced.

### 4.18 Collatz

```python
number = int(input("Start: "))

steps = 0
print(number)

while number!= 1:
    if number % 2 == 0:
        number //= 2
    else:
        number = number * 3 + 1

    print(number)
    steps += 1

print(f"Took {steps} steps")
```

For 6, the sequence is 6, 3, 10, 5, 16, 8, 4, 2, 1, which is 8 steps. Note the printed
sequence has 9 numbers and 8 arrows between them, so the step count is one less than the
number of lines printed. That is worth checking, since students often get 9.

This is the exercise that justifies `while`. You really cannot know in advance how many
steps it will take, so a `for` loop with a range is not an option. Say that
out loud. "I cannot count the passes, so I need a `while`" is exactly the reasoning this
unit is trying to build.

If you want to test the conjecture yourself, you can wrap the whole thing in another
loop that runs every starting number from 1 to 1000 and checks that each one reaches 1.
That is a nice nested loop exercise and it runs fast enough.

Worth knowing that the Collatz conjecture is unsolved. No one has proved it always
reaches 1, and no one has found a number that fails. It is a real open problem in
mathematics, and it fits in ten lines of beginner code. That is a really motivating
thing for a new programmer to hear.
