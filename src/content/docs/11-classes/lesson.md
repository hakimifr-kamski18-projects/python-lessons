---
title: Unit 11 — Classes
sidebar:
  hidden: true
pagefind: false
head:
  - tag: meta
    attrs:
      name: robots
      content: noindex
prev: false
next: false
---
**Files for this unit.** [`first_class.py`](/code/11-classes/first_class.py), [`methods.py`](/code/11-classes/methods.py), [`objects_in_a_list.py`](/code/11-classes/objects_in_a_list.py), [`bank_account.py`](/code/11-classes/bank_account.py)

These live in `public/code/11-classes/` in the repository, and the links above
open them as plain text. Every snippet the student needs is already inline in the
exercises, so the files are for the session itself, when you are both at the
keyboard.

**Goal for the session.** They can write a small class with `__init__`, a few attributes
and a few methods, make several objects from it, and use those objects in a list. They
can also say, in their own words, what `self` is. That idea and the difference between
a class and an object made from it are the two hardest parts of the unit.

**Time.** Two sessions. The first one runs up to the end of section 5. The second one
covers `__str__`, the class or dictionary question, and the bank account, and leaves
time for the core exercises.

**Prerequisites.** Units 00 to 10. The ones that matter most are unit 07 (functions,
parameters, `return` and scope) and unit 08 (dictionaries and lists of dictionaries).
Section 8 also needs `raise` and `try` and `except` from unit 05.


---

## 0. Warm-up

Have them write this from scratch, without looking. It is a list of dictionaries and two
functions, all of which they have done before.

```python
students = [
    {"name": "Ada", "scores": [88, 92]},
    {"name": "Grace", "scores": [95, 98]},
]

def add_score(student, score):
    student["scores"].append(score)

def average(student):
    return sum(student["scores"]) / len(student["scores"])

add_score(students[0], 79)

for student in students:
    print(f"{student['name']}: {average(student):.1f}")
```

When it runs, ask them what is awkward about it. Wait. They may say "nothing", which is a
fair answer, because it works. Then point at these, one at a time.

- Every function takes `student` as its first parameter. The functions only make sense
  for a student dictionary, but nothing in the code says so. You could hand `average`
  any dictionary at all and it would crash.
- The keys are text. A typo such as `student["socres"]` is only noticed when that line
  runs, as a `KeyError`.
- The data and the functions that work on it live in separate places. In a bigger
  program, someone has to remember which functions go with which dictionaries.

Do not solve it yet. Just leave them with the feeling that the data and the functions
belong together. Today is about the tool that puts them together.

## 1. Why classes

Ask them what `name.upper()` does. Then ask what `upper` is. They have been calling
methods (functions that belong to a value, written after a dot) since unit 02, and
`items.append(4)` since unit 06.

```python
print(type("hello"))
print(type([1, 2]))
```

Have them run that. They have seen `<class 'str'>` since unit 01 and probably never
asked about the word `class`. Now explain it. A string is a type of value that comes
with its own functions attached, such as `upper`, `strip` and `split`. A list is another
type, with `append` and `sort`. Somebody wrote those types once, and every string and
every list gets the methods for free.

A class (a way to make your own type of value, with its own data and its own methods)
lets them do the same thing. Say this sentence to them out loud. "You have been calling
methods since unit 02, and today you write the thing they live on."

A class bundles two things together.

1. Data, such as a student's name and scores.
2. The functions that work on that data, such as adding a score or working out the
   average.

These are the two things the warm-up kept in separate places. Do not show the code yet.

## 2. A first class

Open [`first_class.py`](/code/11-classes/first_class.py).

```python
class Dog:
    pass

rex = Dog()
fido = Dog()

print(type(rex))
print(rex)
print(fido)
```

The shape is `class`, a name, a colon, and an indented body. `pass` means "do nothing, on
purpose", which they met in unit 03. This class is empty, and that is fine for now.

Three things to point out.

**Class names start with a capital letter,** and each new word gets a capital too, as in
`BankAccount`. Function and variable names stay lower case with underscores. Python does
not force this, but everyone does it, and it lets you tell a class from a function at a
glance.

**Calling the class with brackets makes an object** (one value made from a class).
`Dog()` looks like a function call, and it works like a function that
gives back a new dog every time. `rex` and `fido` are two separate objects.

**The printout is ugly but it tells you something.** It shows
`<__main__.Dog object at 0x...>`. `__main__` is the file you ran, the same word as in the
main guard from unit 10. The number is where the object lives in memory, and it is
different for `rex` and `fido` because they are two different objects. Ask them to run
the file twice and notice that the numbers change. Nobody ever needs that number.

The picture to give is a blueprint (a plan for building something). The class is the
blueprint for a house. Each object is one house built from it. You can build many houses
from one blueprint, and painting one house does not paint the others.

Other tutorials call an object an instance (another word for object). This course says
object.

Next, show them one step that real code does not do. It makes the next section easier
to follow.

```python
class Dog:
    pass

rex = Dog()
fido = Dog()
rex.name = "Rex"
fido.name = "Fido"
print(rex.name)
print(fido.name)
```

`rex.name` is an attribute (a variable that belongs to an object, written after a dot).
It lives on `rex`, and `fido` has its own. Ask them what happens if they make a third dog and print its
name without setting it. Let them run it.

```
AttributeError: 'Dog' object has no attribute 'name'
```

That is the problem `__init__` solves. Setting attributes from outside is easy to forget,
and then one object is missing something the others have.

## 3. `__init__` and `self`

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rex = Dog("Rex", 3)
fido = Dog("Fido", 7)

print(rex.name, rex.age)
print(fido.name, fido.age)
```

`__init__` (the method that sets up a new object) is spelled with two underscores on
each side. It is a function inside the class, written with `def`, exactly like the
functions from unit 07. Python runs it by itself every time you create an object.

Walk through what `Dog("Rex", 3)` does, slowly, because the rest of the unit depends on
it.

1. Python makes a new, empty `Dog` object.
2. It calls `__init__`, and hands it that new object as the first argument. So `self` is
   the new dog, `name` is `"Rex"` and `age` is `3`.
3. `self.name = name` puts the name on the new dog. `self.age = age` puts the age on it.
4. `__init__` finishes, and `Dog("Rex", 3)` gives back the new dog, which goes into
   `rex`.

Now connect it to section 2. `self.name = "Rex"` inside the class does exactly what
`rex.name = "Rex"` did from outside. The only difference is that inside the class you
do not know yet which variable the object will end up in. It might be `rex` or it might
be `fido`. So you call it `self` (the name a method uses for the object it was called
on), which means "this one, whichever it is".

Ask them what `self` is when `fido = Dog("Fido", 7)` runs. Wait for the answer. It is
the new Fido object, so the same code in `__init__` now works on a different object.

**The two names in `self.name = name` are different things.** The `name` on the right is
the parameter, a local variable from unit 07, and it disappears when `__init__`
finishes. The `self.name` on the left is an attribute, and it stays on the object for as
long as the object exists. Have them prove it by renaming the parameter.

```python
class Dog:
    def __init__(self, dog_name, age):
        self.name = dog_name
        self.age = age

rex = Dog("Rex", 3)
print(rex.name)
```

It still works. The names usually match only because that is easier to read.

**`self` is just a parameter.** The word `self` is not a keyword (a word that Python has
reserved for itself). It is a habit that every Python programmer follows, so tell them to
always use it and never invent another name.

**Attributes can be read and changed with the dot.**

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rex = Dog("Rex", 3)
fido = Dog("Fido", 7)
rex.age = 4
print(rex.age, fido.age)
```

That prints `4 7`. Changing one object leaves the others alone. This is the house and
paint picture from section 2, now shown with numbers.

### Break it on purpose

Have them try each of these and read the error before you say anything.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

rex = Dog("Rex")
```

```
TypeError: Dog.__init__() missing 1 required positional argument: 'age'
```

The error names `Dog.__init__()`, which shows that `Dog(...)` really did call `__init__`.

Then `Dog("Rex", 3, 4)`.

```
TypeError: Dog.__init__() takes 3 positional arguments but 4 were given
```

Ask them to count the values they gave. They gave three, and Python says four. That is
`self`, which Python passed without being asked. This is the first time they see `self`
being counted, and it will matter in the next section.

Then have them misspell it as `_init_`, with one underscore on each side, and run
`Dog("Rex", 3)`.

```
TypeError: Dog() takes no arguments
```

Python did not find a method called `__init__`, so it thinks the class takes nothing.
This one is confusing, so it is worth seeing once.

## 4. Methods

Open [`methods.py`](/code/11-classes/methods.py).

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.tricks = []

    def describe(self):
        return f"{self.name} is {self.age} years old"

    def have_birthday(self):
        self.age += 1

    def add_trick(self, trick):
        self.tricks.append(trick)

rex = Dog("Rex", 3)
print(rex.describe())
rex.have_birthday()
print(rex.describe())
rex.add_trick("sit")
print(rex.tricks)
```

A method is a function written inside the class. The rules are the ones from unit 07,
plus two more.

1. The first parameter is always `self`.
2. Inside the method, every attribute is reached through `self`, as `self.name` and
   `self.age`.

You call a method with the dot, the same way as `name.upper()`. The brackets are needed,
and any other arguments go inside them, as in `rex.add_trick("sit")`. You never pass
`self` yourself.

### Where `self` comes from

This is the moment when most people finally understand `self`. Have them run both lines.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} years old"

rex = Dog("Rex", 3)
print(rex.describe())
print(Dog.describe(rex))
```

They print the same thing. When you write `rex.describe()`, Python turns it into
`Dog.describe(rex)`. The object before the dot becomes `self`. This also explains why
the error in section 3 counted one more argument than they typed.

The same is true of the methods they already know.

```python
print("ada".upper())
print(str.upper("ada"))
```

`str` is the class for strings, and `"ada"` becomes the `self` inside `upper`. Pause
here so they can take it in, because the methods they have used for weeks work exactly
like the ones they are writing now.

### Two kinds of method

Point at the three methods and sort them into two groups.

- `describe` gives back a value, like `name.upper()`. You use the result, so you print
  it or store it.
- `have_birthday` and `add_trick` change the object, like `items.append()`. They do not
  return anything.

This is `print` versus `return` from unit 07 again. Ask them what this shows.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1

rex = Dog("Rex", 3)
print(rex.have_birthday())
print(rex.age)
```

`None` and then `4`. The method changed the dog and gave back nothing, the same as
`print(items.append(4))` gives `None`. If they remember that from unit 06, they already
understand this.

Note that `self.tricks = []` goes inside `__init__`. That gives every dog its own empty
list. Ask them why that matters, and connect it to aliases from unit 06 if they want to
go further.

### Break it on purpose

**Forgetting `self` in the `def`.**

```python
class Cat:
    def speak():
        return "Meow"

print(Cat().speak())
```

```
TypeError: Cat.speak() takes 0 positional arguments but 1 was given
```

"But I did not give it anything!" is the right reaction. Ask them who gave it the one
argument. It was Python, passing the cat as `self`. The method had no room for it.

**Forgetting `self.` before an attribute.**

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def shout(self):
        return name.upper()

print(Cat("Tom").shout())
```

```
NameError: name 'name' is not defined. Did you mean: 'self.name'?
```

Python 3.14 even suggests the fix. Without `self.`, the name is a plain local variable,
and there is no local variable called `name` inside `shout`. The parameter `name` from
`__init__` disappeared when `__init__` finished, which is scope from unit 07.

**Forgetting the brackets on a method call.**

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"This is {self.name}"

rex = Dog("Rex")
print(rex.describe)
```

```
<bound method Dog.describe of <__main__.Dog object at 0x...>>
```

There is no error, which makes this mistake hard to spot. They get the method itself, not
its answer. It is the same mistake as `greet` without brackets in unit 07.

## 5. Many objects

Open [`objects_in_a_list.py`](/code/11-classes/objects_in_a_list.py). Now solve the
warm-up properly.

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def report(self):
        return f"{self.name}: {self.average():.1f}"

students = [Student("Ada"), Student("Grace"), Student("Alan")]
students[0].add_score(88)
students[0].add_score(92)
students[1].add_score(95)
students[2].add_score(71)

for student in students:
    print(student.report())
```

Put it next to the warm-up and compare them. Ask them what changed.

- `add_score` and `average` now live inside the thing they work on.
- `student["scores"]` became `self.scores`. A typo in an attribute name still fails, but
  the error is an `AttributeError` that names the object and usually suggests the right
  spelling.
- The loop looks almost the same. A list of objects is just a list, so `for`, `len()`,
  `append()` and indexes all work as before.

`report` calls `self.average()`. A method can use another method of the same object
through `self`, the same way it reaches attributes. It is the same idea as functions
calling functions in section 5 of unit 07, only inside a class.

**Each object keeps its own data.** Have them print `students[0].scores` and
`students[1].scores` and see two different lists. Adding a score to Ada did not touch
Grace.

Then show two patterns they already know, now with objects. The first is "best so far",
from unit 04.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

students = [Student("Ada", 88), Student("Grace", 95), Student("Alan", 71)]

best = students[0]
for student in students:
    if student.score > best.score:
        best = student
print(best.name)
```

The second is searching, from unit 06, written as a function that gives back the object
or `None`.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def find_student(students, name):
    for student in students:
        if student.name == name:
            return student
    return None

students = [Student("Ada", 88), Student("Grace", 95)]
found = find_student(students, "Grace")
print(found.score)
print(find_student(students, "Linus"))
```

Point out that `best` and `found` are not copies. They are the same objects that are in
the list, under a second name. If they change `found.score`, the student in the list
changes too. That is an alias from unit 06 again.

## 6. `__str__`, so `print` shows something readable

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

rex = Dog("Rex", 3)
print(rex)
print(f"My dog is {rex}")
```

`__str__` (the method that gives the text `print()` shows for an object) has two
underscores on each side, like `__init__`. Nobody calls it by hand. `print()`, `str()` and f-strings
call it for you.

The rule to give them is that `__str__` must return a string. It must not print. Have
them break it.

```python
class Cat:
    def __str__(self):
        print("a cat")

print(Cat())
```

It shows `a cat`, because the `print` inside runs, and then it crashes.

```
TypeError: __str__ returned non-string (type NoneType)
```

`NoneType` means a function gave back `None`, which they know from unit 07 means a
missing `return`.

One thing that surprises people is that `print(students)`, a whole list of objects,
still shows the ugly form for each object, even with `__str__`. Lists use a different
method to show what is inside them. Do not teach that method. Tell them to loop over the
list and print each object, which is what they would do anyway.

## 7. A class or a dictionary?

They will ask this. Both are fine for small programs, and real code uses both, so give
them a simple guide to start from.

**Use a dictionary when** the data is a lookup table, where you look things up by a key
and the keys are not known in advance, as with word counts, a phone book, settings or
stock levels. A dictionary is also the better choice when the data goes straight into
JSON and back, because `json` already understands dictionaries.

**Use a class when** you have a thing with a fixed set of attributes and some actions that
belong to it, such as a student with scores, or a bank account with deposit and withdraw.
The sign to look for is the one from the warm-up. If you have several functions that all
take the same kind of dictionary as their first parameter, that dictionary should
probably become a class.

**A class is also the right choice when there is a rule to protect.** The bank account in
the next section must never go below zero. With a dictionary, any line of the program can
write `account["balance"] = -500`. With a class, all the changes go through `withdraw`,
so the rule lives in one place.

The two are often used together. A dictionary of objects, keyed by name, is common, and
so is an object that holds a list or a dictionary as an attribute. If they are not sure,
tell them to start with a dictionary and switch to a class when the functions start to
pile up. That is what experienced programmers do too.

## 8. Putting it together

Open [`bank_account.py`](/code/11-classes/bank_account.py). Have them type it, not copy
it.

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
        if amount > self.balance:
            raise ValueError(f"Not enough money, the balance is {self.balance}")
        self.balance -= amount

    def __str__(self):
        return f"{self.owner} has {self.balance}"

account = BankAccount("Ada", 100)
account.deposit(50)
print(account)

try:
    account.withdraw(500)
except ValueError as error:
    print(f"Could not withdraw: {error}")

print(account)
```

Things to notice, in order.

**`balance=0` is a default value** from unit 07. `BankAccount("Grace")` makes an
account with nothing in it. Defaults work in `__init__` the same as in any function.

**`withdraw` raises a `ValueError` rather than printing a message.** Ask them why. The
method does not know what the caller wants to do about it. A menu program might show a
message and ask again, and a program that reads a file of payments might write the
failure to a log. The method reports the problem, and the caller decides. That is the
same idea as `remove_item` returning `True` or `False` in exercise 7.17, and the same
`raise` they learned in unit 05.

**`except ValueError as error` gives the error a name.** `as error` puts the error into
a variable, and printing it shows the message that was passed to `raise`. If unit 05
already covered this, a quick reminder is enough.

**The balance did not change** when the withdrawal failed, because `raise` stopped the
method before `self.balance -= amount` ran. Ask them to predict the last line of output
before running it.

Then have them extend it, one step at a time.

1. Make two accounts and show that they keep separate balances.
2. Add a check in `withdraw` that refuses zero or negative amounts.
3. Write a loop that tries to withdraw each amount in `[20, -5, 1000, 50]` and prints
   whether it worked, without the program stopping.

The last one is in the file if they get stuck. It is a good end to the session, because
it uses a class, a list, a loop and `try` and `except` together, which is most of the
course in ten lines.

---

## Teaching notes for this unit

**`self` is the whole unit.** Everything else is details. The two moments that help them
understand it are `rex.name = "Rex"` from outside turning into `self.name = name` inside, and
`rex.describe()` printing the same as `Dog.describe(rex)`. Spend real time on both. When
they get it wrong later, do not explain it again. Ask "which object is `self` here?" and
let them answer.

**The classic mistakes, and the real messages from Python 3.14.** Show each one once, on
purpose, so they recognise it later.

- Forgetting `self` in the `def`. `Cat.speak() takes 0 positional arguments but 1 was
  given`. The "1 was given" is the object, passed as `self`.
- Forgetting `self.` before an attribute. `NameError: name 'name' is not defined. Did you
  mean: 'self.name'?`. If they set it in `__init__` without `self.`, for example
  `name = name`, the error comes later and looks different. It shows up as
  `AttributeError: 'Dog' object has no attribute 'name'` the first time anything reads
  `rex.name`.
- Calling the class without brackets. `account = BankAccount` puts the class itself in
  the variable, not a new account. `print(account)` shows `<class '__main__.BankAccount'>`,
  and the word `class` is the clue. Then `account.deposit(50)` gives
  `BankAccount.deposit() missing 1 required positional argument: 'amount'`, because the
  `50` went into `self`. That message is really confusing, so walk through it.
- Confusing the class with an object. `Dog.describe()` gives
  `Dog.describe() missing 1 required positional argument: 'self'`. There is no dog
  before the dot, only the blueprint, so there is nothing to be `self`.
- Wrong number of arguments when making an object.
  `Dog.__init__() missing 1 required positional argument: 'age'`, or
  `takes 3 positional arguments but 4 were given`, where the count includes `self`.
- Misspelling `__init__`. `Dog() takes no arguments`.
- Typo in an attribute. `AttributeError: 'Dog' object has no attribute 'nme'. Did you
  mean: 'name'?`.

**A useful habit when they read these errors.** If a message mentions one more argument
than they typed, the extra one is `self`. That one sentence covers half the errors in
this unit.

**Watch for `scores = []` written directly in the class body,** outside `__init__`. It
runs, but every object then shares one list, so adding a score to Ada adds it to Grace
as well. It is the alias trap from unit 06. If it happens, do not explain class
attributes. Tell them that every attribute is set in `__init__` with `self.`, and that
this rule avoids the problem.

**Keep money in whole numbers.** `0.1 + 0.2` is not exactly `0.3` in Python, and a
student who meets that in a bank account will lose twenty minutes to it. The examples
and exercises use whole amounts on purpose.

**Do not teach** `__repr__`, class attributes, `@property`, `@staticmethod`,
`@classmethod`, names with a leading underscore, or dataclasses. All of them exist and
none of them are needed yet. If a student finds one, say that it exists and that the
course stops before it.

**The class or dictionary question has no wrong answer at this size.** If they write a
dictionary where you would write a class, let it go unless the functions are piling up.
The point of section 7 is that they can make the choice on purpose.

**Expect the first class they write alone to have no methods.** That is fine. A class
with only `__init__` works like a dictionary with dots. The class starts to be worth it
when they move a function into it. Exercise 11.11 (the student with marks) is a good place to make that move
on purpose.

**Preview of next unit.** They can make their own type of value. Next session they meet
inheritance, which is how one class can start from another and change only the parts
that are different. It is a short unit, and it is the last one.
