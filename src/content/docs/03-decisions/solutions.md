---
title: Unit 03 solutions
sidebar:
  label: Solutions
---
## Warm-ups

### 3.1 Predict the boolean

```python
10 > 5 # True
10 > 10 # False, strictly greater
10 >= 10 # True
"a" == "A" # False, case matters
"a" != "A" # True
3 * 2 == 6 # True, the multiplication happens first
not (5 > 3) # False, not True is False
5 > 3 and 2 > 4 # False, one side is False
5 > 3 or 2 > 4 # True, at least one side is True
```

The one to watch out for is `3 * 2 == 6`. Arithmetic happens before comparison, so it is `6
== 6`, which is true. Python has a precedence order (which operation goes first, see the
glossary) and here it matches what you would expect. Brackets remove all doubt, as
always.

### 3.2 Spot the bug

```python
if age >= 17 or age < 17:
```

This is always true, because every number is either greater than or equal to 17, or less
than 17. There is no gap. So it always prints "Can drive".

The fix is to keep only the first half:

```python
if age >= 17:
    print("Can drive")
else:
    print("Cannot drive")
```

The point: `or` with two conditions that cover everything is the same as no
condition at all. Put 15 in place of `age` in each half and see which one is true. The
second one is, so the whole condition is true.

### 3.3 Spot the second bug

```python
if number > 1 or number < 10:
```

`or` is wrong here, it should be `and`. With `or`, the condition is true whenever either
half is true, and 50 satisfies `number > 1`. So it passes.

The fix is:

```python
if number > 1 and number < 10:
```

Or, a shorter way:

```python
if 1 < number < 10:
```

The exercise says that 1 and 10 are not included. `number > 1` excludes 1 and
`number < 10` excludes 10, so this is correct. If 1 and 10 had to be included, you would
need `>=` and `<=`. In real work, "between 1 and 10" often does not say which one is
meant, so it is worth asking.

### 3.4 Branch order

```python
score = 95

if score > 60:
    print("C") # <- this matches first and everything stops
elif score > 90:
    print("A")
else:
    print("F")
```

The problem is the order. `95 > 60` is true, so the first branch runs and the `A` branch
is never reached. The conditions have to go from strictest to loosest.

```python
score = 95

if score > 90:
    print("A")
elif score > 60:
    print("C")
else:
    print("F")
```

There is a second problem with the original. A score of exactly 60 gets `F`, because the
condition is `> 60` rather than `>= 60`. Whether that is a bug depends on what was
meant, which is exactly why testing boundaries matters.

---

## Core

### 3.5 Even or odd

```python
number = int(input("Number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

This is the canonical use of `%`. If there is nothing left over when dividing by two,
the number is even.

Test 0 and -3. `0 % 2` is 0, so zero is even, which is correct in mathematics even if it
surprises some people. `-3 % 2` is 1, so -3 is detected as odd, and the check still
works for negative numbers.

### 3.6 Biggest of three

```python
a = int(input("First: "))
b = int(input("Second: "))
c = int(input("Third: "))

if a >= b and a >= c:
    biggest = a
elif b >= a and b >= c:
    biggest = b
else:
    biggest = c

print(f"The biggest is {biggest}")
```

The interesting part is `>=` rather than `>`. With `>`, the input 5, 5, 1 does not match
either of the first two conditions, so it falls into `else` and prints 1, which is wrong.
Using `>=` throughout means a tie still matches, so the first matching branch wins.

The failure mode to watch for is writing something like `if a > b and b > c`,
which only handles the case where the values are already in order. Test `3, 1, 2`
and watch it break.

Once you have it working, look at `max(a, b, c)`, which does it in one line. Then ask
yourself which version you would use in real code. The answer is `max()`. The point of
the exercise was the logic, not the result.

### 3.7 Cinema tickets

```python
age = int(input("Age: "))

if age < 5:
    price = 0
elif age < 18:
    price = 8
elif age < 65:
    price = 14
else:
    price = 9

print(f"Ticket price: {price} dollars")
```

Look at the conditions. Because the branches are checked in order, `age < 18` only gets
evaluated when `age >= 5` is already known, so there is no need to write `5 <= age <
18`. Writing the full range is also fine and may be clearer for a beginner. Both are correct.

The boundary tests are the real point:

- 4 gives 0
- 5 gives 8
- 17 gives 8
- 18 gives 14
- 64 gives 14
- 65 gives 9

If any of these are wrong, the problem is a comparison that is off by one step, for example `<` where `<=` was
needed. This is the most common bug with age brackets and price brackets.

### 3.8 Password check

```python
password = input("Password: ")
length = len(password)

if length >= 12:
    print("Strong")
elif length >= 8:
    print("Acceptable")
else:
    print("Weak")
```

Same order-dependent shape as the cinema prices. A 14 character password matches the
first branch and stops, so it is strong rather than merely acceptable.

The choice to think about here is `.strip()`. Should it be `input("Password: ").strip()`?
For a real password, no. A space is a legitimate character and stripping would change
what the user typed. For this exercise it does not matter. Still, it is a good question
to ask yourself, because it shows that "always strip input" is a habit and not a rule.

### 3.9 Login

```python
correct_user = "ada"
correct_pass = "secret123"

username = input("Username: ").strip().lower()
password = input("Password: ")

if username != correct_user:
    print("No such user")
elif password != correct_pass:
    print("Wrong password")
else:
    print("Welcome")
```

The order of the checks does not change the result here. "Welcome" needs both the
username and the password to match, so it cannot print for a wrong username in either
order. Only the choice between the two error messages depends on the order. If you check
the password first, a wrong username with a wrong password says "Wrong password" instead
of "No such user".

Real systems usually show one message for both cases, so that an attacker cannot learn
which part was wrong. Here you show two messages on purpose, because the exercise asks
for them.

You can also write this with an `if` inside another `if`. Both shapes work, and the
version with one `if` inside another may be easier to follow here:

```python
if username == correct_user:
    if password == correct_pass:
        print("Welcome")
    else:
        print("Wrong password")
else:
    print("No such user")
```

### 3.10 Triangle or not

```python
a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("That is a triangle")
else:
    print("That is not a triangle")
```

The three conditions all have to hold, so `and` throughout. The trap is writing `or`,
which would let almost everything through.

It helps to picture this before writing the code. Two short sides have to
be able to reach across the long one. If they cannot, the shape collapses. Try
to draw a triangle with sides 1, 2 and 10 and see for yourself.

Test 3, 4, 5, which works, and 1, 2, 3, which fails because the condition is strict (`>`
and not `>=`). With 1, 2, 3 the two short sides lie exactly along the long one and make
a flat line, so it is correctly rejected.

### 3.11 BMI category

```python
weight = float(input("Weight in kg: "))
height = float(input("Height in metres: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"

print(f"Your BMI is {bmi:.1f}, which is {category}")
```

Two things to check.

The formula needs `height ** 2`, which is height squared. Writing `weight / height ** 2`
is correct, because `**` binds tighter than `/`. If you wrote `(weight / height) ** 2`
you will get a wildly wrong number, so test with a known value. For 70 kg and
1.75 m, the answer is about 22.9.

Each condition only states the upper end of its range. This works because of the
order. When `bmi < 18.5` has failed, the BMI is at least 18.5, so `bmi < 25` is enough
for the normal range.

### 3.12 Yes or no, properly

```python
answer = input("Do you agree? ").strip().lower()

if answer in ["y", "yes"]:
    print("You agreed")
elif answer in ["n", "no"]:
    print("You disagreed")
else:
    print("I did not understand")
```

`.strip().lower()` handles all the capital letter and space variations. Then
`answer in ["y", "yes"]` checks the two spellings of each answer in one short line.

If you wrote `if answer == "y" or answer == "yes"` that is also correct. The list
version is shorter and is common in real code.

The `else` here is the point of the exercise. If only the yes and no cases are handled, a
typo like `ya` silently does the wrong thing. Writing the third case is a good habit.

---

## Stretch

### 3.13 Leap year

```python
year = int(input("Year: "))

if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

if is_leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

If you want a shorter way, the last four lines can be one line. It means "print the
first text if `is_leap` is true, otherwise print the second text":

```python
print(f"{year} is a leap year" if is_leap else f"{year} is not a leap year")
```

The interesting part is the logic. The rules can be written as one combined
condition:

```python
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
```

That is correct and it is harder to read than the chain of `elif` above. The `elif`
version works because the order encodes the priority of the rules. 2000 is divisible by
400, so the first branch takes it. 1900 is divisible by 100 but not 400, so the second
branch takes it. 2024 falls through both and hits the third.

Both versions are worth seeing, and that comparison is the point. Some
problems are easier to write as a chain of priorities than as one big condition.

Test cases that must all pass: 2024 yes, 2023 no, 1900 no, 2000 yes, 2100 no.

### 3.14 Income tax

```python
income = float(input("Annual income: "))

if income <= 10000:
    tax = 0
elif income <= 30000:
    tax = (income - 10000) * 0.20
else:
    tax = 20000 * 0.20 + (income - 30000) * 0.40

print(f"Tax on {income:.2f} is {tax:.2f}")
```

Test values:

- 5000 pays 0
- 10000 pays 0
- 30000 pays 4000, which is 20 percent of 20000
- 50000 pays 12000, being 4000 plus 40 percent of 20000

The shape here is important and it comes up often in real programming. The tax on
income above a bracket is the full tax from all the brackets below, plus the partial
amount in the current one. The `20000 * 0.20` in the last branch is that "full tax from
below" term, written as a number.

If you write `(income - 30000) * 0.40` alone you get 8000 for an income of 50000,
forgetting the 4000 from the middle bracket. That is the mistake this exercise is
designed to produce. Testing with 50000 shows it, because only an income above 30000
reaches the last branch.

For a cleaner version, give the fixed amount a name:

```python
tax_from_lower_brackets = 4000
```

This is easier to read and makes the structure clear.

### 3.15 Rock paper scissors

This is a short version that handles the draw first and then checks one direction.

```python
p1 = input("Player 1: ").strip().lower()
p2 = input("Player 2: ").strip().lower()

if p1 == p2:
    print("Draw")
elif (p1 == "rock" and p2 == "scissors") or \
     (p1 == "scissors" and p2 == "paper") or \
     (p1 == "paper" and p2 == "rock"):
    print("Player 1 wins")
else:
    print("Player 2 wins")
```

The backslash at the end of a line means "this statement continues on the next line".
Another way is to wrap the whole condition in brackets, which lets it continue on the
next line without a backslash:

```python
elif ((p1 == "rock" and p2 == "scissors")
      or (p1 == "scissors" and p2 == "paper")
      or (p1 == "paper" and p2 == "rock")):
```

Both work. Most people prefer the bracket version because it does not depend on an
invisible character at the end of a line.

Here is the answer to the question in the exercise. The solution has one `if`, one
`elif` and one `else`, so 3 branches, instead of 9 separate cases (3 x 3), and it
handles all nine combinations correctly. The idea has two parts. Handle the draw first
with a single equality, and then only test the three combinations where player one wins,
leaving everything else to the `else`. This pattern, "test the specific cases and let the
rest fall through", is worth remembering because you will see it often.

This last version is optional and you can skip it. It uses a list and `.index()`, which
you will meet in unit 05, and it also handles a move that is not rock, paper or scissors.
Some people find this arithmetic idea on their own.

```python
moves = ["rock", "paper", "scissors"]
if p1 not in moves or p2 not in moves:
    print("Invalid move")
elif p1 == p2:
    print("Draw")
elif (moves.index(p1) - moves.index(p2)) % 3 == 1:
    print("Player 1 wins")
else:
    print("Player 2 wins")
```
