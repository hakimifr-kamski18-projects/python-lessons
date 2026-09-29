# Unit 03 solutions

## Warm-ups

### 3.1 Predict the boolean

```python
10 > 5 # True
10 > 10 # False, strictly greater
10 >= 10 # True
"a" == "A" # False, case matters
"a"!= "A" # True
3 * 2 == 6 # True, the multiplication happens first
not (5 > 3) # False, not True is False
5 > 3 and 2 > 4 # False, one side is False
5 > 3 or 2 > 4 # True, at least one side is True
```

The one to watch out for is `3 * 2 == 6`. Arithmetic happens before comparison, so it is `6
== 6`, which is true. Python has a precedence order here and it matches what you would
expect. Worth remembering that brackets remove all doubt, as always.

### 3.2 Spot the bug

```python
if age >= 17 or age < 17:
```

This is always true, because every number is either greater than or equal to 17, or less
than 17. There is no gap. So it always prints "Can drive".

The fix is just the first half.

```python
if age >= 17:
    print("Can drive")
else:
    print("Cannot drive")
```

The lesson here. `or` with two conditions that cover everything is the same as no
condition at all. Say the two conditions out loud for an age of 15 and hear
that the second one is true.

### 3.3 Spot the second bug

```python
if number > 1 or number < 10:
```

`or` is wrong here, it should be `and`. With `or`, the condition is true whenever either
half is true, and 50 satisfies `number > 1`. So it passes.

The fix.

```python
if number > 1 and number < 10:
```

Or, nicer.

```python
if 1 < number < 10:
```

Note that as written, `number > 1` excludes 1 and `number < 10` excludes 10, so the
range is strictly between. If the exercise means to include 1 and 10, it needs `>=` and
`<=`. Worth asking yourself which was intended, since the exercise says "between
1 and 10" and English is really unclear here. Noticing that lack of
clarity is valuable, because real specifications are full of it.

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

The issue is ordering. `95 > 60` is true, so the first branch runs and the `A` branch is
never reached. The conditions have to go from strictest to loosest.

```python
score = 95

if score > 90:
    print("A")
elif score > 60:
    print("C")
else:
    print("F")
```

There is a second problem with the original, worth noticing. A score of exactly 60 falls
through to `F`, because the condition is `> 60` rather than `>= 60`. Whether that is a
bug depends on intent, which is exactly why boundary testing matters.

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

Worth testing 0 and negative numbers. `0 % 2` is 0, so zero is even, which is
correct mathematically and occasionally surprises people. `-3 % 2` is 1 in Python, not
-1, which means the even and odd check still works for negatives. Python's `%` always
gives a result with the same sign as the divisor, which is different from some other
languages. You do not need to go into it deeply, just check that your even and odd test works for
negatives too.

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

The interesting part is the `>=` rather than `>`. With `>` the code still works for the
largest value, but ties get handled inconsistently. Using `>=` throughout makes the
first matching branch win and keeps the behaviour predictable.

The failure mode to watch for is writing something like `if a > b and b > c`,
which only handles the case where the values are already in order. Test `3, 1, 2`
and watch it break.

Once you have it working, look at `max(a, b, c)`, which does it in one line. Then ask
yourself which version you would use in real code. The answer is `max()`, and the point of the
exercise was the logic, not the result.

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

Note the conditions. Because the branches are checked in order, `age < 18` only gets
evaluated when `age >= 5` is already known, so there is no need to write `5 <= age <
18`. Writing the full range is also fine and arguably clearer for a beginner, so do not
avoid it. Both are correct.

The boundary tests, which are the actual point.

- 4 gives 0
- 5 gives 8
- 17 gives 8
- 18 gives 14
- 64 gives 14
- 65 gives 9

If any of these are wrong, the problem is an off-by-one in a comparison operator, which
is the single most common bug with age brackets and price brackets.

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

The judgement call here is `.strip`. Should it be `input("Password: ").strip`? For a
real password, no, a space is a legitimate character and stripping would change what the
user typed. For this exercise it does not matter. It is a nice question to ask yourself, because
it shows that "always strip input" is a habit rather than a law.

### 3.9 Login

```python
correct_user = "ada"
correct_pass = "secret123"

username = input("Username: ").strip.lower
password = input("Password: ")

if username!= correct_user:
    print("No such user")
elif password!= correct_pass:
    print("Wrong password")
else:
    print("Welcome")
```

The order matters and is worth thinking about. You check the username first so that a
wrong username never reveals whether the password was right. If you put the password
check first, a wrong username with a right password would say "Welcome", which is wrong.

That is a real thing in real systems. Security people call it not leaking information
about which part was wrong. It is a nice first taste of the idea that the order of
checks can have meaning beyond just correctness.

If you wrote it with nested `if` statements instead, that is completely fine. Both
shapes work and the nesting is arguably easier to follow here.

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

It is worth getting a feel for this before writing the code. Two short sides have to
be able to reach across the long one. If they cannot, the shape collapses. Try
to draw a triangle with sides 1, 2 and 10 and see for yourself.

Worth testing with 3, 4, 5, which works, and 1, 2, 3, which fails because the condition
is strict. That is a degenerate triangle, a flat line, and it correctly gets rejected.

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

The category comparisons use the boundary value on the end of each range, which works
because of the ordering. `bmi < 25` after `bmi < 18.5` failed means the BMI is at least
18.5.

### 3.12 Yes or no, properly

```python
answer = input("Do you agree? ").strip.lower

if answer in ["y", "yes"]:
    print("You agreed")
elif answer in ["n", "no"]:
    print("You disagreed")
else:
    print("I did not understand")
```

`.strip.lower` handles all the case and whitespace variations, and then the list form
handles the two spellings per answer cleanly.

If you wrote `if answer == "y" or answer == "yes"` that is also correct. The list
version is shorter and is what you will see in real code.

The `else` here is the point of the exercise. With only two options handled, a typo like
`ya` silently does the wrong thing. Spelling out the third case is a habit worth
building.

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

print(f"{year} is a leap year" if is_leap else f"{year} is not a leap year")
```

That final print uses a conditional expression, which is unit 09 material. If you have
not met it, use the ordinary version.

```python
if is_leap:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
```

The logic, and this is the interesting part. The rules can be written as one combined
condition.

```python
if (year % 4 == 0 and year % 100!= 0) or year % 400 == 0:
```

That is correct and it is harder to read than the chain of `elif` above. The `elif`
version works because the order encodes the priority of the rules. 2000 is divisible by
400, so the first branch takes it. 1900 is divisible by 100 but not 400, so the second
branch takes it. 2024 falls through both and hits the third.

Both versions are worth seeing, and the comparison between them is the lesson. Some
problems are easier to write as a chain of priorities than as one big condition.

Test cases that must all pass. 2024 yes, 2023 no, 1900 no, 2000 yes, 2100 no.

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

Test values.

- 5000 pays 0
- 10000 pays 0
- 30000 pays 4000, which is 20 percent of 20000
- 50000 pays 12000, being 4000 plus 40 percent of 20000

The shape here is important and it comes up constantly in real programming. The tax on
income above a bracket is the full tax from all the brackets below, plus the partial
amount in the current one. The `20000 * 0.20` in the last branch is that "full tax from
below" term, written as a number.

If you write `(income - 30000) * 0.40` alone you get 8000 for an income of 50000,
forgetting the 4000 from the middle bracket. That is the mistake the exercise is
designed to produce, and testing with 30000 first makes it clear.

If you want a cleaner version, the fixed amount can be a named variable.

```python
tax_from_lower_brackets = 4000
```

Which is more readable and makes the structure clear.

### 3.15 Rock paper scissors

A compact version that handles the draw first and then checks one direction.

```python
p1 = input("Player 1: ").strip.lower
p2 = input("Player 2: ").strip.lower

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
Worth knowing about, but the alternative is to wrap the whole
condition in brackets and let it span lines naturally.

```python
elif ((p1 == "rock" and p2 == "scissors")
      or (p1 == "scissors" and p2 == "paper")
      or (p1 == "paper" and p2 == "rock")):
```

Both work. The bracket version is generally preferred because it does not depend on an
invisible character at the end of a line.

Answering the question in the exercise. There are five statements here, not nine, and it
handles all nine combinations correctly. The trick is two-fold. Handle the draw first
with a single equality, and then only test the three combinations where player one wins,
leaving everything else to the `else`. That "test the specific cases, let the rest fall
through" pattern is worth remembering, because it turns up everywhere.

There is a neat arithmetic version using `%` that some students find on their own.

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
