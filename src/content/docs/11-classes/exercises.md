---
title: Unit 11 exercises
sidebar:
  label: Exercises
---
Every exercise here comes down to two questions. What does this thing hold, and what can
it do? Write `__init__` first, make one object, and print its attributes. Only add the
methods once that works.

---

## Before you start

These are the ideas the exercises use. Read them once, then come back if you get stuck.

You have been calling methods (functions that belong to a value, written after a dot)
since unit 02. `name.upper()` and `items.append(4)` are two of them. A class is a way to
make your own type of value, with its own data and its own methods. When you call the class with brackets, you get an object (one value
made from a class). One class can make as many objects as you like, in the same way that
one blueprint (a plan for building something) can be used to build many houses.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rex = Dog("Rex", 3)
fido = Dog("Fido", 7)
print(rex.name, fido.age)   # Rex 7
```

Class names start with a capital letter, and each new word gets one too, as in
`BankAccount`. `__init__` (the method that sets up a new object) has two underscores on
each side, and Python runs it by itself when you create an object.

Here is what `Dog("Rex", 3)` does. Python makes a new, empty dog. Then it calls
`__init__` and passes the new dog in as the first argument, so `self` (the name a method
uses for the object it was called on) is the new dog, `name` is `"Rex"` and `age` is `3`. The line
`self.name = name` stores the name on the new dog. When `__init__` finishes, you get the
dog back, and it goes into `rex`.

`self.name` is an attribute (a variable that belongs to an object, written after a dot). The `name` on the
right of `self.name = name` is only the parameter, and it disappears when `__init__`
ends. The attribute stays on the object. Each object has its own attributes, so changing
`rex.age = 4` does not change `fido`.

A method is a function written inside the class.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"

    def have_birthday(self):
        self.age += 1

rex = Dog("Rex", 3)
rex.have_birthday()
print(rex.describe())   # Rex is 4 years old
```

These are the rules for methods.

- The first parameter is always `self`.
- Inside a method, you reach every attribute through `self`, as in `self.age`.
- You call a method with a dot and brackets, as in `rex.describe()`. You never pass
  `self` yourself.
- A method can give back a value with `return`, like `describe`. Or it can change the
  object, like `have_birthday`, and then it gives back `None`, the same as `append()`.
- A method can call another method of the same object, as in `self.describe()`.

`rex.describe()` is the same as `Dog.describe(rex)`. Python puts the object before the
dot into `self`. That is why an error message about a method often counts one more
argument than you typed. The extra one is `self`.

When you print an object, you get something like `<__main__.Dog object at 0x7f3a...>`.
To get something readable, add `__str__` (the method that gives the text `print()` shows
for an object). It must return a string, not print one.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

rex = Dog("Rex", 3)
print(rex)                 # Rex (3)
print(f"My dog: {rex}")    # My dog: Rex (3)
```

Objects go in lists like any other value, and a loop gives you one object at a time.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dogs = [Dog("Rex", 3), Dog("Fido", 7)]
for dog in dogs:
    print(dog.name, dog.age)
```

A method can refuse bad input by raising an error with `raise`, from unit 05. The caller
then decides what to do with `try` and `except`. Writing `except ValueError as error`
puts the error into the variable `error`, and printing it shows the message that was
given to `raise`.

```python
class Wallet:
    def __init__(self):
        self.money = 0

    def spend(self, amount):
        if amount > self.money:
            raise ValueError("Not enough money")
        self.money -= amount

wallet = Wallet()
try:
    wallet.spend(10)
except ValueError as error:
    print(f"Problem: {error}")   # Problem: Not enough money
```

Two hints for reading errors in this unit. If the message counts one more argument than
you gave, look for a missing `self` in a `def`. If a method says a name is not defined,
look for a missing `self.` in front of an attribute.

---

## Warm-ups

### 11.1 Predict the output

```python
class Box:
    def __init__(self, label, weight):
        self.label = label
        self.weight = weight

a = Box("books", 12)
b = Box("pillows", 2)
b.weight = 3
a.label = "old books"
print(a.label, a.weight)
print(b.label, b.weight)

c = a
c.weight = 20
print(a.weight)
```

The last three lines are the interesting part. Is `c` a new box?

### 11.2 Predict the output

```python
class Lamp:
    def __init__(self):
        self.on = False

    def switch(self):
        self.on = not self.on

    def status(self):
        if self.on:
            return "on"
        return "off"

lamp = Lamp()
print(lamp.status())
lamp.switch()
print(lamp.status())
print(lamp.switch())
print(lamp.status())
```

Notice that `__init__` here takes only `self`. That is allowed. Every lamp starts off.

### 11.3 Find the missing self

This is meant to print `Hello, Ada!`. It crashes.

```python
class Greeter:
    def __init__(self, name):
        self.name = name

    def hello():
        return f"Hello, {self.name}!"

greeter = Greeter("Ada")
print(greeter.hello())
```

```
TypeError: Greeter.hello() takes 0 positional arguments but 1 was given
```

The call `greeter.hello()` has nothing inside the brackets. So what is the one argument
that "was given"? Fix the bug.

### 11.4 Find the missing self, part two

This is meant to print `68.0`. There are two mistakes. Fixing the first one shows the
second.

```python
class Thermometer:
    def __init__(self, celsius):
        celsius = celsius

    def fahrenheit(self):
        return celsius * 9 / 5 + 32

thermometer = Thermometer(20)
print(thermometer.fahrenheit())
```

Run it, read the error, fix that line, and run it again. Then explain why the line
`celsius = celsius` does nothing useful.

### 11.5 The class or an object?

```python
class Basket:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

basket = Basket
print(basket)
basket.add("apple")
```

Before you run it, predict what `print(basket)` shows. Then run it and read the error on
the last line. The error says an argument is missing, even though `"apple"` is right
there. Where did `"apple"` go? Fix the bug with two characters.

### 11.6 Match the error to the mistake

Here are four short programs and four error messages. Match each program to its message
before you run anything. Then run them to check, and fix each one.

Program A.

```python
class Song:
    def __init__(self, title):
        self.title = title

song = Song()
```

Program B.

```python
class Song:
    def __init__(self, title):
        self.title = title

    def show(self):
        return self.title

print(Song.show())
```

Program C.

```python
class Song:
    def __init__(self, title):
        self.title = title

song = Song("Yellow")
print(song.titel)
```

Program D.

```python
class Song:
    def __init__(self, title):
        self.title = title

    def show():
        return "a song"

print(Song("Yellow").show())
```

The messages.

1. `TypeError: Song.show() takes 0 positional arguments but 1 was given`
2. `TypeError: Song.__init__() missing 1 required positional argument: 'title'`
3. `AttributeError: 'Song' object has no attribute 'titel'. Did you mean: 'title'?`
4. `TypeError: Song.show() missing 1 required positional argument: 'self'`

---

## Core

### 11.7 Rectangle

Write a class `Rectangle`. `__init__` takes a width and a height and stores them as
attributes. Add two methods that return a number, `area()` and `perimeter()`. The
perimeter is the distance all the way round, which is `2 * (width + height)`.

Make two rectangles of different sizes and print the area and the perimeter of each.

Then add a method `is_square()` that returns `True` or `False`. It should return a real
boolean (a value that is either True or False), not a string, as in exercise 7.8.

### 11.8 Counter

Write a class `Counter` for counting things, such as people coming through a door.

- `__init__` starts the count at 0.
- `click()` adds one to the count.
- `reset()` sets the count back to 0.
- `value()` returns the count.

Test it by clicking three times, printing the value, resetting, and printing again.

Then change `__init__` so that it takes a starting number with a default value of 0, so
that `Counter()` starts at 0 and `Counter(10)` starts at 10.

Then use two counters in one program. Ask the user for a sentence. Go through the
letters, and click one counter for each vowel and the other for every other letter.
Ignore spaces. Print both counts at the end.

### 11.9 Dog years

Write a class `Dog` with a name and an age. Add a method `human_years()` that returns
the age multiplied by 7.

Make three dogs, put them in a list, and print a line like this for each one.

```
Rex is 3, which is 21 in human years
```

Then change `human_years()` to use a better rule. Each of the first two years counts as
10.5 human years, and every year after that counts as 4. So a dog of 1 is 10.5, a dog of
2 is 21, and a dog of 3 is 25. Only the method has to change. The loop that prints
stays the same.

### 11.10 Bank account

Write a class `BankAccount` with an owner and a balance. The balance has a default value
of 0.

- `deposit(amount)` adds to the balance. It raises a `ValueError` if the amount is not
  more than zero.
- `withdraw(amount)` takes money out. It raises a `ValueError` if the amount is not more
  than zero, or if it is more than the balance.
- `get_balance()` returns the balance.

Then write a small menu program around one account, with these options, in a
`while True` loop.

```
1. Deposit
2. Withdraw
3. Show balance
4. Quit
```

Ask for amounts with `int(input(...))`. Wrap each deposit and withdrawal in `try` and
`except ValueError as error`, and print the error. Then type a word instead of a number
and see what happens. `int("abc")` also raises a `ValueError`, so the same `except`
catches it.

### 11.11 Student with marks

Write a class `Student` with a name and a list of marks, which starts empty.

- `add_mark(mark)` adds a mark to the list. It raises a `ValueError` if the mark is
  below 0 or above 100.
- `average()` returns the average of the marks.
- `best()` returns the highest mark.

Decide what `average()` and `best()` should give back when there are no marks yet. Make
that choice on purpose, as in exercise 7.13, so that the program does not crash with an
error you did not plan for.

Then make three students, give each one some marks, and print each name with the
average to one decimal place. Print the student with the highest average at the end.

### 11.12 Readable printing

Add a `__str__` method to your `Rectangle` from 11.7, your `Dog` from 11.9 and your
`BankAccount` from 11.10, so that printing them shows lines like these.

```
Rectangle 3 by 4
Rex, 3 years old
Ada has 150
```

Print each one with `print()`, and once inside an f-string.

Then put the three objects in a list and print the whole list with one `print()`. What
do you see? What do you need to do instead to see the readable form of each one?

### 11.13 A shelf of books

Write a class `Book` with a title, an author and a year. Give it a `__str__` that shows
`Dune by Frank Herbert (1965)`.

Make a list of at least five books. Then write two functions. They are normal
functions, outside the class, because they work on a whole list of books rather than
on one book.

- `find_by_author(books, author)` returns a list of the books by that author. The
  search should ignore upper and lower case.
- `oldest(books)` returns the book with the smallest year.

Ask the user for an author and print every book by them, or `No books by that author` if
there are none. Then print the oldest book.

### 11.14 Transfer between accounts

Add a method `transfer(self, other, amount)` to your `BankAccount` from 11.10. It moves
`amount` from this account to `other`, which is another `BankAccount` object.

Use `withdraw` and `deposit` inside it rather than changing `balance` directly. Then
check that when there is not enough money, the transfer raises a `ValueError` and
neither balance changes. You can test it by adding these lines below your class.

```python
ada = BankAccount("Ada", 100)
grace = BankAccount("Grace")
ada.transfer(grace, 30)
print(ada.get_balance(), grace.get_balance())   # should be 70 30
```

Think about the order. Does it matter whether `transfer` withdraws first or deposits
first?

---

## Stretch

### 11.15 Shopping cart

Write two classes that work together.

`Item` has a name, a price and a quantity, which defaults to 1. Its method `total()`
returns the price multiplied by the quantity. Use whole numbers for prices.

`ShoppingCart` holds a list of `Item` objects, which starts empty.

- `add(item)` adds an `Item` to the list.
- `remove(name)` removes the item with that name. It raises a `ValueError` if there is no
  such item.
- `total()` returns the total of every item.
- `most_expensive()` returns the item with the biggest total, or `None` if the cart is
  empty.
- `receipt()` prints one line per item and the total at the end.

```
2 x bread at 3 = 6
1 x cheese at 8 = 8
Total: 14
```

Notice that `ShoppingCart.total()` can call `total()` on each item. Each class does its
own part of the work.

### 11.16 A grade book as a class

A grade book keeps the score of each student. With a dictionary, it looks like
`{"Ada": 88, "Grace": 95}`, and the program around it asks for names and scores, saves
them, and prints a report. Rewrite that idea with a class.

Write a class `GradeBook` that keeps a dictionary of names and scores as an attribute.

- `add(name, score)` stores a score. A name given twice replaces the earlier score. The
  score must be from 0 to 100, or it raises a `ValueError`.
- `average()` returns the average score, or `0` if the book is empty.
- `best()` returns the name and the score of the top student as two values, or
  `None, None` if the book is empty.
- `report()` prints every student and score, sorted by name, then the average and the
  best student.

Then write the main program. Ask for a name and a score again and again, until the user
gives an empty name. If the score is not a number or is out of range, print the problem
and ask again. Print the report at the end.

When it works, look at the main program. It should be short, and it should not touch
the dictionary directly at all. Everything goes through the methods.

### 11.17 Saving objects to JSON

`json` from unit 09 knows how to save lists and dictionaries, but not your own objects.
Try it.

```python
import json

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

book = Book("Dune", "Frank Herbert", 1965)
try:
    print(json.dumps(book))
except TypeError as error:
    print(error)
```

The fix is to turn each object into a dictionary before saving, and to turn each
dictionary back into an object after loading.

1. Add a method `to_dict()` to `Book` that returns
   `{"title": ..., "author": ..., "year": ...}` for that book.
2. Write a function `save_books(books, filename)` that builds a list of dictionaries with
   a loop and saves it with `json.dump`.
3. Write a function `load_books(filename)` that loads the list of dictionaries and builds
   a `Book` from each one. If the file does not exist, it returns an empty list.

Save a list of three books, load them back into a new list, and print each loaded book
to check that they came back the same.

---

## Check yourself

Try to do these without looking at your notes.

- Write a class with `__init__` and two methods, and make two objects from it.
- Explain what `self` is, and where its value comes from when you call a method.
- Say the difference between `Dog` and `Dog("Rex", 3)`.
- Read an error that counts one more argument than you typed, and find the cause.
- Add `__str__` to a class so that `print()` shows something readable.
- Look at a problem and decide, on purpose, whether a dictionary or a class fits it
  better.
