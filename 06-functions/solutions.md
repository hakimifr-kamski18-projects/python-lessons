# Unit 06 solutions

## Warm-ups

### 6.1 and 6.2

6.1 prints `5` and then `None`.

The function prints `5` when it is called. Then `result` holds `None`, because there is
no `return`, so the second print gives `None`.

6.2 prints `5` once. Nothing is printed inside the function, because there is no `print()`
in it, and `result` holds the number 5.

The one sentence answer to the comparison. Printing shows a value to a human, returning
hands a value to the code that called the function.

### 6.3 Predict the output

```
big
small
small
```

The third one is the interesting case. `mystery(10)` does not match `x > 10`, since 10
is not greater than 10, so it falls through to `return "small"`. If you said `big`, this
is the case to look at again.

This is also a good example of the early return pattern. The first `return` handles one
case and stops the function, so the second line is what happens for everything else.

### 6.4 Find the bug

```python
def area(width, height):
    result = width * height
```

There is no `return`. The function computes the area into a local variable (only exists
inside the function) and then finishes, discarding it. The caller gets `None`.

```python
def area(width, height):
    return width * height
```

It is worth asking yourself what `result` was for in the original. The answer is nothing, and the
variable could be dropped entirely. A `return` can return an expression directly, and a
single-use variable in between is often just not needed.

### 6.5 Find the bug, part two

```python
def with_tax(price):
    print(price * 1.15)

total = with_tax(20) + 5
```

The function prints the number and returns `None`, so the next line is `None + 5`, which
is a `TypeError`.

```python
def with_tax(price):
    return price * 1.15

total = with_tax(20) + 5
print(total) # 28.0
```

The error message will mention `NoneType`. Read that as "a function
earlier in the program did not return anything", because that is almost always what it
means.

### 6.6 Scope

```python
def make_name:
    name = "Ada"

make_name
print(name)
```

A `NameError`. `name` was created inside the function and it ceased to exist when the
function finished. The function's variables do not leak out into the rest of the
program.

```python
def make_name:
    return "Ada"

name = make_name
print(name)
```

Which is the fix, and it is the general answer. If you want something from inside a
function, return it.

---

## Core

### 6.7 Celsius to Fahrenheit

```python
def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print(to_fahrenheit(0)) # 32.0
print(to_fahrenheit(100)) # 212.0
print(to_fahrenheit(37)) # 98.6
```

The point of the exercise is that the function does not print. All three prints are in
the main part of the program, which means the same function could be used inside another
calculation, or stored in a list, or compared, without any changes.

Check that 0 gives 32 and 100 gives 212. If the formula is written with the
brackets in the wrong place, those two will not come out right, and it is much easier to
spot with known values.

### 6.8 Even or odd, as a function

```python
def is_even(number):
    return number % 2 == 0

for i in range(1, 21):
    if is_even(i):
        print(i)

# or, to collect them
evens = []
for i in range(1, 21):
    if is_even(i):
        evens.append(i)
print(evens)
```

The important detail is `return number % 2 == 0` rather than an `if` statement. The
comparison already produces `True` or `False`, so returning it directly is both shorter
and clearer.

If you wrote this, it works and it is worse.

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
```

Compare it with the one line version and see which you prefer. The idea here is that an
`if` whose branches just return `True` and `False` is usually unnecessary.

### 6.9 Biggest of three, as a function

```python
def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

x = int(input("First: "))
y = int(input("Second: "))
z = int(input("Third: "))

print(f"The biggest is {biggest(x, y, z)}")
```

Same logic as exercise 3.6, in a function. Note the last line of the function has no
`elif` guard, because if neither of the first two matched, `c` must be the answer. That
is a small but real piece of reasoning worth noticing.

### 6.10 Greeting with a default

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Ada")) # Hello, Ada!
print(greet("Ada", "Good morning")) # Good morning, Ada!
print(greet("Ada", greeting="Hi")) # Hi, Ada!
print(greet(greeting="Hi", name="Ada")) # Hi, Ada! order does not matter
```

The last two lines are the point of keyword arguments (passing a value by naming the
parameter). When you spell out the parameter names (the name in the definition that
receives the value), the order stops mattering. That is useful when a function has
several optional parameters.

### 6.11 BMI

```python
def bmi(weight, height):
    return weight / (height ** 2)

def bmi_category(value):
    if value < 18.5:
        return "underweight"
    if value < 25:
        return "normal"
    if value < 30:
        return "overweight"
    return "obese"

weight = float(input("Weight in kg: "))
height = float(input("Height in metres: "))

value = bmi(weight, height)
print(f"BMI: {value:.1f}, which is {bmi_category(value)}")
```

Three lines in the main part, and each one says exactly what it does. Compare that with
the fifteen line version from exercise 3.11. That comparison is the exercise.

Note how `bmi_category` uses the early return pattern rather than `elif` chains. Both
work. The early return version has one less level of nesting, and some people find it
easier to read.

### 6.12 Count vowels, as a function

```python
def count_letters(text, letter):
    count = 0
    for character in text:
        if character == letter:
            count += 1
    return count

def count_vowels(text):
    text = text.lower
    total = 0
    for vowel in "aeiou":
        total += count_letters(text, vowel)
    return total

sentence = input("Sentence: ")
print(f"Vowels: {count_vowels(sentence)}")
```

Note that `count_vowels` calls `count_letters` five times rather than looping over the
characters once. It is less efficient and much easier to read, and that is usually the
right trade. Worth noticing.

The `.lower` inside `count_vowels` means callers do not have to remember to do it
themselves. That is a small design decision, and it is the right one. A function should
handle the awkward details so its callers do not have to.

### 6.13 Statistics

```python
def statistics(numbers):
    if not numbers:
        return None, None, None

    smallest = numbers[0]
    largest = numbers[0]
    total = 0

    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
        total += number

    average = total / len(numbers)
    return smallest, largest, average

low, high, avg = statistics([4, 7, 2, 9, 4])
print(f"low {low}, high {high}, average {avg:.2f}")
```

The empty list case is the interesting decision, and there is no single right answer.
Returning three `None`s is one option. Other reasonable options.

- Return the average as `0` for an empty list and the extremes as `None`.
- Print a message and return nothing.
- Let it crash with a clear error, because an empty list is a caller mistake.

Think about which you chose and why. The point is that you made the decision on purpose
rather than having it happen by accident. `None` is unit 08 material if you have not
met it yet, and `if not numbers:` is the unit 03 truthiness rule.

### 6.14 Squares list

```python
def squares_up_to(n):
    result = []
    for number in range(1, n + 1):
        result.append(number ** 2)
    return result

print(squares_up_to(4)) # [1, 4, 9, 16]
```

The key point is that `result` has to be returned. Without the `return`, the list is
built and then destroyed when the function ends, and the caller gets `None`. That is the
same lesson as 6.4, in a different form.

`range(1, n + 1)` gives 1 to n inclusive, thanks to the off-by-one rule. If you wrote
`range(1, n)` the answer is short by one, and the test with 4 catches it.

### 6.15 Is it a prime, as a function

```python
def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

for number in range(2, 50):
    if is_prime(number):
        print(number, end=" ")
```

The early return makes this cleaner than the flag version in exercise 4.15. As soon as a
divisor is found, return `False` and stop. If the loop finishes without finding one, it
must be prime.

That "return early when you know, and let the end of the function handle the other case"
shape is the same one as 6.9 and it is worth noticing.

Note that the caller does not know or care that there is a loop inside. It just asks a
question and gets an answer. The loop is now an internal detail, which is exactly what a
function is for.

### 6.16 Menu

```python
def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def biggest(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= c:
        return b
    return c

def count_vowels(text):
    count = 0
    for character in text.lower:
        if character in "aeiou":
            count += 1
    return count

def show_menu:
    print()
    print("1. Celsius to Fahrenheit")
    print("2. Biggest of three")
    print("3. Count vowels")
    print("4. Quit")

while True:
    show_menu
    choice = input("Choose: ").strip

    if choice == "1":
        celsius = float(input("Celsius: "))
        print(f"{to_fahrenheit(celsius):.1f} F")

    elif choice == "2":
        a = float(input("First: "))
        b = float(input("Second: "))
        c = float(input("Third: "))
        print(f"Biggest: {biggest(a, b, c)}")

    elif choice == "3":
        text = input("Text: ")
        print(f"Vowels: {count_vowels(text)}")

    elif choice == "4":
        print("Bye")
        break

    else:
        print("I did not understand that choice")
```

The main loop collects input and calls functions, and the functions do the work. The
`else` branch catches typos, which is the same habit as exercise 3.12.

This shape, a loop with a menu and one branch per option, is what most small command
line programs look like. It is worth having written one.

---

## Stretch

### 6.17 Refactor the grade calculator

```python
def letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"

def print_report(name, score):
    grade = letter_grade(score)
    print(f"{name} scored {score}, which is a {grade}")

name = input("Name: ").strip.title
score = int(input("Score out of 100: "))
print_report(name, score)
```

Three lines in the main part, and each one is clear.

The judgement call is that `print_report` prints rather than returns. That is correct
here, because its whole job is to produce output for a human. A function that prints is
not wrong, it just has a narrower purpose. The rule is not "never print in a function".
It is "know which one you are doing and why".

For the shopping list, a reasonable decomposition.

```python
def read_items:
    items = []
    while True:
        item = input("Item (or 'done' to finish): ").strip
        if item.lower == "done":
            break
        if item:
            items.append(item)
    return items

def show_items(items):
    for item in items:
        print(f" - {item}")

def remove_item(items, item):
    if item in items:
        items.remove(item)
        return True
    return False

items = read_items
print(f"{len(items)} items:")
show_items(items)
```

Note that `remove_item` returns `True` or `False` so the caller knows whether it worked,
rather than printing a message itself. That is a good design habit. The function reports
what happened, and the caller decides what to do about it.

Note also that `remove_item` changes the list in place (changed directly, without a
copy), which is the one place this decomposition breaks the "no side effects" rule. It
is a real judgement call. An alternative is to have it return a new list, which is
cleaner but slower and less natural here.

### 6.18 Debugging by cutting down

```python
def count_long_words(sentence):
    words = sentence.split
    count = 0
    for word in words:
        if len(word) > 3:
            return count # <- the bug
        count += 1
    return count
```

The intended answer for `"a bb ccc dddd"` is 1, since only `dddd` is longer than three
characters.

What actually happens.

```
word = "a" len 1, not > 3, count = 1
word = "bb" len 2, not > 3, count = 2
word = "ccc" len 3, not > 3, count = 3
word = "dddd" len 4, > 3 -> return 3
```

It returns 3.

The bug is that `return` leaves the function entirely. It was put inside the `if` where
an increment belonged. This is a very common mistake and worth naming clearly. `return`
does not mean "give back the current answer and keep going". It means "stop and leave,
right now".

`break` would leave the loop but continue the function. `continue` would skip one pass.
Only `return` exits the whole function. That comparison is a good one to make here,
since you now know all three.

The fix.

```python
def count_long_words(sentence):
    count = 0
    for word in sentence.split:
        if len(word) > 3:
            count += 1
    return count
```

### 6.19 Recursion

```python
def countdown(n):
    if n <= 0:
        print("Liftoff")
        return
    print(n)
    countdown(n - 1)
```

Trace for `countdown(3)`.

```
countdown(3): 3 <= 0 is false, print 3, call countdown(2)
  countdown(2): 2 <= 0 is false, print 2, call countdown(1)
    countdown(1): 1 <= 0 is false, print 1, call countdown(0)
      countdown(0): 0 <= 0 is true, print Liftoff, return
    countdown(1) finishes
  countdown(2) finishes
countdown(3) finishes
```

What stops it is the base case, `n <= 0`. Every call reduces `n` by one, so it always
reaches 0 eventually. Without the base case, the function would call itself forever
until Python gives up with a `RecursionError`, which is a real error worth seeing once.

The loop version, which is what most people would actually write.

```python
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff")
```

Both are correct. The loop is easier to follow here. Recursion becomes really useful for
tree-shaped problems, which are a long way off. The point of this is so that
recursion is not frightening when you meet it later.

### 6.20 Functions that take functions

`apply_twice(double, 5)` does this.

```
func = double, value = 5
func(value) = double(5) = 10
func(func(value)) = double(10) = 20
```

So it returns 20.

The inner call happens first, giving 10, and then `double` is applied to that result,
giving 20.

A version with your own function.

```python
def add_one(n):
    return n + 1

print(apply_twice(add_one, 5)) # 7, because 5 -> 6 -> 7
```

The connection to exercise 5.14 is the real lesson. `sorted(words, key=len)` passes the
function `len` as a value, in exactly the same way. That is why `key` works without
brackets. You are handing the function itself, not the result of calling it, and
`sorted()` decides when to call it.

That distinction, between `len` and `len()`, is the thing to take away.
