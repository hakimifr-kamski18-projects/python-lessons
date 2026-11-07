---
title: Unit 11 solutions
sidebar:
  label: Solutions
---
## Warm-ups

### 11.1 Predict the output

```
old books 12
pillows 3
20
```

The first two lines show that each box keeps its own attributes. Changing `b.weight`
did not touch `a`, and changing `a.label` did not touch `b`.

The last line is the one to think about. `c = a` does not make a new box. Only calling
`Box(...)` makes a new box. `c` is an alias (a second name for the same value) of `a`,
the same idea as with lists in unit 06. There is one box with two names, so changing
`c.weight` changes the box that `a` names too.

### 11.2 Predict the output

```
off
on
None
off
```

The lamp starts off, because `__init__` sets `self.on = False`. The first `switch()`
turns it on.

The third line is the trap. `print(lamp.switch())` runs `switch`, which turns the lamp
off again, and then prints what `switch` gave back. `switch` has no `return`, so it gave
back `None`. It is the same as `print(items.append(4))`. A method that changes the object
usually returns nothing, and the change still happens.

`self.on = not self.on` flips a boolean. `not True` is `False` and `not False` is
`True`.

### 11.3 Find the missing self

```python
class Greeter:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hello, {self.name}!"

greeter = Greeter("Ada")
print(greeter.hello())   # Hello, Ada!
```

The one argument that "was given" is the object itself. `greeter.hello()` is the same as
`Greeter.hello(greeter)`, so Python passes `greeter` in, even though the brackets are
empty. The method was written as `def hello():`, with no room for it, so Python
complained. Every method needs `self` as its first parameter, even when it uses nothing
else.

### 11.4 Find the missing self, part two

The first run fails inside `fahrenheit`.

```
NameError: name 'celsius' is not defined
```

Inside `fahrenheit` there is no variable called `celsius`. The fix for that line is
`self.celsius`. But the second run fails with a different error.

```
AttributeError: 'Thermometer' object has no attribute 'celsius'
```

So the object has no `celsius` attribute either, and that is the first mistake, back in
`__init__`. Here is the fixed version.

```python
class Thermometer:
    def __init__(self, celsius):
        self.celsius = celsius

    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

thermometer = Thermometer(20)
print(thermometer.fahrenheit())   # 68.0
```

`celsius = celsius` takes the parameter and puts it into a variable with the same name,
which is the same variable. Nothing changes, and when `__init__` ends the variable
disappears, which is scope from unit 07. Only `self.celsius = celsius` puts the value on
the object, where other methods can find it.

The order of the errors is worth noticing. The mistake was in `__init__`, but Python only
complained later, when another method tried to use the missing value. When you see an
`AttributeError` about your own object, look at `__init__` first.

### 11.5 The class or an object?

`print(basket)` shows this.

```
<class '__main__.Basket'>
```

The word `class` is the clue. `basket = Basket` has no brackets, so it does not make a
basket. It puts the class itself, the blueprint, into the variable.

Then `basket.add("apple")` crashes.

```
TypeError: Basket.add() missing 1 required positional argument: 'item'
```

Because `basket` is the class and not an object, there is no object for Python to pass
as `self`. So `"apple"` went into `self`, the first parameter, and nothing was left for
`item`. That is why the message says `item` is missing when you can see the argument
right there.

The fix is two characters, the brackets.

```python
class Basket:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

basket = Basket()
basket.add("apple")
print(basket.items)   # ['apple']
```

### 11.6 Match the error to the mistake

- Program A gives message 2. `Song()` makes a song without a title, but `__init__`
  needs one. Fix it with `Song("Yellow")`.
- Program B gives message 4. `Song.show()` calls the method on the class, so there is no
  song to be `self`. Fix it by making a song first, `Song("Yellow").show()`.
- Program C gives message 3. `titel` is a typo, and Python 3.14 even suggests `title`.
- Program D gives message 1. `def show():` has no `self`, and Python passes the song
  in anyway. Fix it with `def show(self):`.

Here is a version that has none of the four mistakes.

```python
class Song:
    def __init__(self, title):
        self.title = title

    def show(self):
        return self.title

song = Song("Yellow")
print(song.title)    # Yellow
print(song.show())   # Yellow
```

Messages 1 and 4 look alike, and they are easy to confuse. Message 1 says Python gave
one more argument than the method has room for, which means `self` is missing from the
`def`. Message 4 says `self` itself is missing, which means there was no object before
the dot.

---

## Core

### 11.7 Rectangle

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

small = Rectangle(3, 4)
big = Rectangle(10, 10)

print(small.area(), small.perimeter())
print(big.area(), big.perimeter())
print(small.is_square())
print(big.is_square())
```

```
12 14
100 40
False
True
```

The two rectangles share the methods but not the data. `small.area()` uses the width and
height of `small`, because `small` is `self` in that call.

`is_square` returns the comparison directly, the same as `is_even` in exercise 7.8. The
`==` already gives `True` or `False`, so an `if` with two `return` lines is not needed.

### 11.8 Counter

```python
class Counter:
    def __init__(self, start=0):
        self.count = start

    def click(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def value(self):
        return self.count

counter = Counter()
counter.click()
counter.click()
counter.click()
print(counter.value())

counter.reset()
print(counter.value())

print(Counter(10).value())
```

```
3
0
10
```

`start=0` is a default value from unit 07, and it works in `__init__` the same as in any
function. The attribute is called `count` and the method is called `value`. Do not give
a method and an attribute the same name, because then `self.value = 0` would replace the
method with a number.

Here is the program with two counters.

```python
class Counter:
    def __init__(self, start=0):
        self.count = start

    def click(self):
        self.count += 1

    def reset(self):
        self.count = 0

    def value(self):
        return self.count

vowels = Counter()
others = Counter()

sentence = input("Sentence: ")
for character in sentence.lower():
    if character == " ":
        continue
    if character in "aeiou":
        vowels.click()
    else:
        others.click()

print(f"Vowels: {vowels.value()}")
print(f"Other letters: {others.value()}")
```

With `Hello World` it prints this.

```
Vowels: 3
Other letters: 7
```

Two objects from one class, each with its own count. Clicking `vowels` never changes
`others`. A comma or a full stop would be counted as an "other letter" here. If you want
to count only letters, use `if not character.isalpha():` in place of the space check.

### 11.9 Dog years

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def human_years(self):
        return self.age * 7

dogs = [Dog("Rex", 3), Dog("Fido", 7), Dog("Bella", 1)]

for dog in dogs:
    print(f"{dog.name} is {dog.age}, which is {dog.human_years()} in human years")
```

```
Rex is 3, which is 21 in human years
Fido is 7, which is 49 in human years
Bella is 1, which is 7 in human years
```

Here is the better rule. Only the method changes.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def human_years(self):
        if self.age <= 2:
            return self.age * 10.5
        return 21 + (self.age - 2) * 4

dogs = [Dog("Rex", 3), Dog("Fido", 7), Dog("Bella", 1)]

for dog in dogs:
    print(f"{dog.name} is {dog.age}, which is {dog.human_years()} in human years")
```

```
Rex is 3, which is 25 in human years
Fido is 7, which is 41 in human years
Bella is 1, which is 10.5 in human years
```

The 21 is the first two years, 2 times 10.5. After that, each year adds 4.

This is the reason for the exercise. The rule lives in one method, so changing it
changed every dog, and the loop did not need to know. The code that uses an object does
not have to care how the method works inside, which is the same reason functions exist.

### 11.10 Bank account

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("A deposit must be more than zero")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("A withdrawal must be more than zero")
        if amount > self.balance:
            raise ValueError(f"Not enough money, the balance is {self.balance}")
        self.balance -= amount

    def get_balance(self):
        return self.balance


account = BankAccount("Ada")

while True:
    print()
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Quit")
    choice = input("Choose: ").strip()

    if choice == "1":
        try:
            amount = int(input("Amount to deposit: "))
            account.deposit(amount)
            print("Done")
        except ValueError as error:
            print(f"Problem: {error}")

    elif choice == "2":
        try:
            amount = int(input("Amount to withdraw: "))
            account.withdraw(amount)
            print("Done")
        except ValueError as error:
            print(f"Problem: {error}")

    elif choice == "3":
        print(f"Balance: {account.get_balance()}")

    elif choice == "4":
        print("Bye")
        break

    else:
        print("I did not understand that choice")
```

Here is part of a run, with a deposit of 100, a withdrawal of 500, and then `abc` typed as
an amount.

```
Choose: 1
Amount to deposit: 100
Done
...
Choose: 2
Amount to withdraw: 500
Problem: Not enough money, the balance is 100
...
Choose: 2
Amount to withdraw: abc
Problem: invalid literal for int() with base 10: 'abc'
```

The methods raise errors and do not print anything. The menu decides what to do about
them, which here is to print the message and show the menu again. Keeping the two apart
means the same class could be used by a program with no menu at all, such as one that reads
payments from a file, and that program would want to handle a refused withdrawal in its
own way.

One `except ValueError` catches two different problems. One is a bad number from
`int()`, and the other is a refused amount from the method. Both are a `ValueError`, so
both land in the same place. The message from `int()` is not very friendly. If you want
a nicer one, catch the `int()` problem in its own `try` first.

Notice that a failed withdrawal leaves the balance alone. The `raise` stops `withdraw`
before the line `self.balance -= amount` is reached.

### 11.11 Student with marks

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            raise ValueError(f"A mark must be from 0 to 100, not {mark}")
        self.marks.append(mark)

    def average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def best(self):
        if not self.marks:
            return None
        return max(self.marks)


ada = Student("Ada")
grace = Student("Grace")
alan = Student("Alan")

for mark in [88, 92, 79]:
    ada.add_mark(mark)
for mark in [95, 90]:
    grace.add_mark(mark)
alan.add_mark(71)

try:
    alan.add_mark(150)
except ValueError as error:
    print(error)

students = [ada, grace, alan]

for student in students:
    print(f"{student.name}: {student.average():.1f}, best {student.best()}")

top = students[0]
for student in students:
    if student.average() > top.average():
        top = student
print(f"Highest average: {top.name}")

print(Student("Linus").average(), Student("Linus").best())
```

```
A mark must be from 0 to 100, not 150
Ada: 86.3, best 92
Grace: 92.5, best 95
Alan: 71.0, best 71
Highest average: Grace
0 None
```

The choice made here is that `average()` gives `0` and `best()` gives `None` when there
are no marks. Without the `if not self.marks:` checks, `average()` would crash with a
`ZeroDivisionError` and `best()` with a `ValueError` from `max()` of an empty list. Other
choices are fine too, such as raising a `ValueError` with a clear message. What matters
is that you made the choice on purpose.

`self.marks = []` is inside `__init__`, so every student gets their own new list. Adding
a mark to Ada never adds it to Grace.

The last part is the "best so far" pattern from unit 04, with objects in place of
numbers. `top` holds a whole student, so at the end you can print the name, the marks or
anything else about them.

### 11.12 Readable printing

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle {self.width} by {self.height}"


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"{self.owner} has {self.balance}"


box = Rectangle(3, 4)
rex = Dog("Rex", 3)
account = BankAccount("Ada", 150)

print(box)
print(rex)
print(account)
print(f"My dog is {rex}")

things = [box, rex, account]
print(things)

for thing in things:
    print(thing)
```

Only `__init__` and `__str__` are shown here, to keep it short. Your classes keep the
methods they already had.

```
Rectangle 3 by 4
Rex, 3 years old
Ada has 150
My dog is Rex, 3 years old
[<__main__.Rectangle object at 0x...>, <__main__.Dog object at 0x...>, <__main__.BankAccount object at 0x...>]
Rectangle 3 by 4
Rex, 3 years old
Ada has 150
```

The numbers after `0x` are different on every run.

`print()` and f-strings both use `__str__`. A list does not. When you print a whole list,
Python uses a different method for the things inside it, and you have not written that
one, so you get the ugly form. The answer is to loop over the list and print each object,
which is what the last two lines do. That is also what you would do anyway to get one
object per line.

### 11.13 A shelf of books

```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


def find_by_author(books, author):
    found = []
    for book in books:
        if book.author.lower() == author.lower():
            found.append(book)
    return found


def oldest(books):
    result = books[0]
    for book in books:
        if book.year < result.year:
            result = book
    return result


books = [
    Book("Dune", "Frank Herbert", 1965),
    Book("Emma", "Jane Austen", 1815),
    Book("Persuasion", "Jane Austen", 1817),
    Book("Frankenstein", "Mary Shelley", 1818),
    Book("Children of Dune", "Frank Herbert", 1976),
]

author = input("Author: ").strip()
matches = find_by_author(books, author)

if matches:
    for book in matches:
        print(book)
else:
    print("No books by that author")

print(f"Oldest: {oldest(books)}")
```

With `jane austen` typed in, it prints this.

```
Emma by Jane Austen (1815)
Persuasion by Jane Austen (1817)
Oldest: Emma by Jane Austen (1815)
```

`find_by_author` is the filter pattern from unit 06. It makes an empty list, goes through
the books and keeps the ones that match. Both sides of the comparison get `.lower()`, so
`jane austen` matches `Jane Austen`.

The functions sit outside the class on purpose. A method answers a question about one
object, such as "how old is this book?". A question about a whole list of books belongs
to a normal function that takes the list. Both are fine places for code, and choosing
between them is part of the design.

`oldest` would crash on an empty list, because of `books[0]`. Here the list is never
empty. If it could be, add a check at the top that returns `None`.

### 11.14 Transfer between accounts

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("A deposit must be more than zero")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("A withdrawal must be more than zero")
        if amount > self.balance:
            raise ValueError(f"Not enough money, the balance is {self.balance}")
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)


ada = BankAccount("Ada", 100)
grace = BankAccount("Grace")

ada.transfer(grace, 30)
print(ada.get_balance(), grace.get_balance())

try:
    ada.transfer(grace, 500)
except ValueError as error:
    print(f"Transfer refused: {error}")

print(ada.get_balance(), grace.get_balance())
```

```
70 30
Transfer refused: Not enough money, the balance is 70
70 30
```

Inside `transfer`, `self` is the account the money comes from, and `other` is a second
account object passed in as a normal argument. A method can take other objects as
parameters, including objects of its own class.

The order matters. `withdraw` goes first. If it raises an error, the method stops right
there and `deposit` never runs, so neither balance changes. If you deposited first and
then the withdrawal failed, Grace would have money that never left Ada's account. The
money would have come from nowhere.

Using `withdraw` and `deposit`, rather than changing `balance` directly, means the rules
about negative amounts and missing money are checked for free. The rules live in one
place, and every way of moving money goes through them.

---

## Stretch

### 11.15 Shopping cart

```python
class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return
        raise ValueError(f"There is no {name} in the cart")

    def total(self):
        result = 0
        for item in self.items:
            result += item.total()
        return result

    def most_expensive(self):
        if not self.items:
            return None
        best = self.items[0]
        for item in self.items:
            if item.total() > best.total():
                best = item
        return best

    def receipt(self):
        for item in self.items:
            print(f"{item.quantity} x {item.name} at {item.price} = {item.total()}")
        print(f"Total: {self.total()}")


cart = ShoppingCart()
cart.add(Item("bread", 3, 2))
cart.add(Item("cheese", 8))
cart.add(Item("apples", 1, 6))
cart.receipt()

print()
print(f"Most expensive: {cart.most_expensive().name}")

cart.remove("apples")
cart.receipt()

try:
    cart.remove("milk")
except ValueError as error:
    print(error)

print(ShoppingCart().most_expensive())
```

```
2 x bread at 3 = 6
1 x cheese at 8 = 8
6 x apples at 1 = 6
Total: 20

Most expensive: cheese
2 x bread at 3 = 6
1 x cheese at 8 = 8
Total: 14
There is no milk in the cart
None
```

There are two classes here, and each does its own part. An `Item` knows its own total. The cart does not
multiply anything itself. It asks each item, and adds up the answers. If the way an item
works out its total ever changes, for example to give a discount, only `Item` changes.

Both classes have a method called `total`, and that is fine. `item.total()` and
`cart.total()` are different methods, because they belong to different classes. Python
picks the right one from the object before the dot.

In `remove`, the `return` straight after `self.items.remove(item)` is important. It
stops the loop as soon as the item is gone, and it skips the `raise` at the end. That
`raise` only runs when the loop finished without finding anything. It is the same early
return shape as `is_prime` in exercise 7.15.

### 11.16 A grade book as a class

```python
class GradeBook:
    def __init__(self):
        self.scores = {}

    def add(self, name, score):
        if score < 0 or score > 100:
            raise ValueError(f"A score must be from 0 to 100, not {score}")
        self.scores[name] = score

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores.values()) / len(self.scores)

    def best(self):
        if not self.scores:
            return None, None
        top_name = None
        top_score = -1
        for name, score in self.scores.items():
            if score > top_score:
                top_name = name
                top_score = score
        return top_name, top_score

    def report(self):
        for name in sorted(self.scores):
            print(f"{name}: {self.scores[name]}")
        print(f"Average: {self.average():.1f}")
        if self.scores:
            name, score = self.best()
            print(f"Best: {name} with {score}")


book = GradeBook()

while True:
    name = input("Name (empty to finish): ").strip().title()
    if not name:
        break
    while True:
        try:
            score = int(input(f"Score for {name}: "))
            book.add(name, score)
            break
        except ValueError as error:
            print(f"Problem: {error}")

book.report()
```

Here is the report after entering Ada 88, Grace 95, Alan 71, and then Ada again with 90.

```
Ada: 90
Alan: 71
Grace: 95
Average: 85.3
Best: Grace with 95
```

Ada appears once, with 90, because `self.scores[name] = score` replaces the earlier
score. That is how dictionaries work, so the class gets that rule for free.

This is a dictionary inside an object. The dictionary is still the right tool for "look up a score by name". The class wraps it with
the rules (scores from 0 to 100) and the questions you want to ask (average, best,
report).

The inner `while True` loop is the validation loop from unit 05. It keeps asking until
`book.add` accepts the score. A bad number from `int()` and an out-of-range score are
both a `ValueError`, so one `except` handles both and asks again.

Look at the main program. It never writes `book.scores[...]`. Everything goes through
`add` and `report`. If you later decide to store each student as a list of scores rather
than one score, only the class has to change.

### 11.17 Saving objects to JSON

The first program prints this.

```
Object of type Book is not JSON serializable
```

"Serializable" means "can be turned into text for saving". `json` knows how to do that
for dictionaries, lists, text, numbers, `True`, `False` and `None`, and for nothing
else.

```python
import json


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def to_dict(self):
        return {"title": self.title, "author": self.author, "year": self.year}

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"


def save_books(books, filename):
    data = []
    for book in books:
        data.append(book.to_dict())
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)


def load_books(filename):
    try:
        with open(filename) as file:
            data = json.load(file)
    except FileNotFoundError:
        return []

    books = []
    for item in data:
        books.append(Book(item["title"], item["author"], item["year"]))
    return books


books = [
    Book("Dune", "Frank Herbert", 1965),
    Book("Emma", "Jane Austen", 1815),
    Book("Frankenstein", "Mary Shelley", 1818),
]

save_books(books, "books.json")
loaded = load_books("books.json")

for book in loaded:
    print(book)

print(load_books("no_such_file.json"))
```

```
Dune by Frank Herbert (1965)
Emma by Jane Austen (1815)
Frankenstein by Mary Shelley (1818)
[]
```

And `books.json` holds a plain list of dictionaries, which you can open and read.

```json
[
  {
    "title": "Dune",
    "author": "Frank Herbert",
    "year": 1965
  },
  ...
]
```

The trip goes object to dictionary to text on the way out, and text to dictionary to
object on the way back. `to_dict` handles the first step, and the `Book(...)` call in
`load_books` handles the last one. `json` only ever sees dictionaries.

The objects in `loaded` are new objects, not the ones you saved. They have the same
attributes, which is all that matters. A file can only hold text, so the objects
themselves can never be saved, only a description of them.

This is also a good example of a class and a dictionary each doing what they are good
at. The dictionary is the shape for saving, and the class is the shape for working with
the data while the program runs.
