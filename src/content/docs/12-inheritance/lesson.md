---
title: Unit 12 — Inheritance
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
**Files for this unit.** [`animals.py`](/code/12-inheritance/animals.py), [`mixed_list.py`](/code/12-inheritance/mixed_list.py)

These live in `public/code/12-inheritance/` in the repository, and the links above
open them as plain text. Every snippet the student needs is already inline in the
exercises, so the files are for the session itself, when you are both at the
keyboard.

**Goal for the session.** They can build a child class from a parent class, override one
method, and use `super().__init__(...)` to add an attribute. And they can say when
inheritance is the wrong tool, which matters as much as knowing how to use it.

**Time.** One session. This is a short unit on purpose, and it is the last one.

**Prerequisites.** Unit 11. They must be comfortable with `__init__`, `self` and
methods. If `self` is still shaky, spend the first half of the session on unit 11
exercises instead, because nothing here will make sense without it.


---

## 0. Warm-up

Have them write these two classes, typing both in full.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} and says {self.speak()}"

    def have_birthday(self):
        self.age += 1

    def speak(self):
        return "Woof"


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        return f"{self.name} is {self.age} and says {self.speak()}"

    def have_birthday(self):
        self.age += 1

    def speak(self):
        return "Meow"


print(Dog("Rex", 3).describe())
print(Cat("Tom", 5).describe())
```

Then ask them how much of the `Cat` class is different from the `Dog` class. Wait for the
answer. Only one word is different, `"Meow"`, and everything else was copied. Ask what happens if they find a bug in
`describe`, or want to add a `rename` method. They would have to do it twice, and three
times when a `Bird` comes along. It is the same feeling as the copy and paste at the
start of unit 07, and the fix is similar.

## 1. A child class gets everything

Open [`animals.py`](/code/12-inheritance/animals.py).

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} is {self.age} and says {self.speak()}"

    def have_birthday(self):
        self.age += 1


class Hamster(Animal):
    pass


nibbles = Hamster("Nibbles", 1)
nibbles.have_birthday()
print(nibbles.describe())
```

The new part is the brackets after the class name. `class Hamster(Animal):` means "a
Hamster is made from an Animal". This is inheritance (making a new class from one that
already exists). `Animal` is the parent class (the class that another class is made
from), and `Hamster` is the child class (a class made from a parent class).

`Hamster` has only `pass` in its body, and yet `Hamster("Nibbles", 1)` works, and so do
`have_birthday` and `describe`. Ask them where those came from. The child gets every
method the parent has, including `__init__`.

Then explain how Python finds a method. When you call `nibbles.describe()`, Python
looks in `Hamster` first. It is not there, so it looks in the parent, `Animal`, finds it,
and runs it with `nibbles` as `self`.

The parent has to be defined above the child. Have them move `Hamster` above `Animal`
and read the error.

```
NameError: name 'Animal' is not defined
```

## 2. Overriding a method

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} is {self.age} and says {self.speak()}"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


print(Dog("Rex", 3).describe())
print(Cat("Tom", 5).describe())
```

`Dog` and `Cat` override `speak`. To override (replace a method from the parent class),
you write a method with the same name in the child class. Python looks in the child
first, finds `speak` there, and never gets as far as the parent's version.

Now the warm-up is solved. Put the two versions side by side. The two copies of
`describe` and `have_birthday` became one, in `Animal`.

The part to slow down on is `describe`. It is written in `Animal`, and it calls
`self.speak()`. Ask them which `speak` runs for `Rex`. Wait. `self` is Rex, and Rex is a
`Dog`, so Python looks in `Dog` first and finds `"Woof"`. The parent's method calls the
child's version without knowing the child exists. This is the idea that makes
inheritance useful, and it is worth tracing on paper once.

Have them break it by misspelling the override as `def speek(self):` in a `Cow` class.
There is no error. `describe` calls `speak`, which `Cow` does not have, so the parent's
`"..."` comes back. A misspelt override fails silently, which is worth knowing when "my
method is not running" comes up later.

## 3. `super().__init__(...)`

A child often needs one more attribute than its parent. A guide dog has an owner.

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} is {self.age} and says {self.speak()}"


class Dog(Animal):
    def speak(self):
        return "Woof"


class GuideDog(Dog):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner


buddy = GuideDog("Buddy", 4, "Sam")
print(buddy.name, buddy.owner)
print(buddy.describe())
```

Writing `__init__` in the child overrides the parent's `__init__`, exactly like `speak`.
That means the parent's setup no longer runs by itself. `super()` fixes that, because it
gives you the parent class from inside a child class. `super().__init__(name, age)` runs
the parent's `__init__`, which sets `self.name` and `self.age`. Then the child adds what
is new.

Three things to point out.

- `super()` passes `self` for you, the same as calling a method with a dot. You never
  write `super().__init__(self, name, age)`.
- Put the `super().__init__` line first. Then the child can use or change what the parent
  set up.
- `GuideDog` is made from `Dog`, which is made from `Animal`. A chain like that works,
  and Python looks in each class in turn. Keep chains short, because two levels is
  plenty.

`super()` works for any method, not only `__init__`. A child can add to the parent's
version rather than replacing it.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"This is {self.name}"


class GuideDog(Animal):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def describe(self):
        return super().describe() + f", who guides {self.owner}"


print(GuideDog("Buddy", "Sam").describe())
```

Show it, but do not spend long on it. The `__init__` case is the one they will use.

### Break it on purpose

Have them delete the `super().__init__` line and call `describe()`.

```
AttributeError: 'GuideDog' object has no attribute 'name'
```

This is the classic bug of the unit, and the error points at the wrong place. It
appears in `describe`, in the parent, but the mistake is in the child's `__init__`. The
parent's setup never ran, so `name` was never set. Tell them that when a child object is
missing an attribute the parent sets, the first thing to look for is `super().__init__`.

## 4. `isinstance()`

Open [`mixed_list.py`](/code/12-inheritance/mixed_list.py).

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


class Cat(Animal):
    pass


rex = Dog("Rex")
print(isinstance(rex, Dog))
print(isinstance(rex, Animal))
print(isinstance(rex, Cat))
print(isinstance("hello", str))
```

`isinstance(object, class)` is a function that checks the type of an object, and it
answers `True` or `False`. The second line is the one to stop on. Rex is a `Dog`, and a `Dog` is an `Animal`, so the answer is `True`. Compare it
with `type(rex) == Animal`, which is `False`, because `type()` only gives the exact
class. That difference is why `isinstance` is the one to use.

It works with the built-in types too, which they can use in validation code.

With their own classes, they will rarely need it. If they find
themselves writing `if isinstance(animal, Dog): ... elif isinstance(animal, Cat): ...`,
that is usually a sign the code belongs in a method that each class overrides. That is
the next section.

## 5. One call, many answers

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


class Bird(Animal):
    def speak(self):
        return "Tweet"


animals = [Dog("Rex"), Cat("Tom"), Bird("Tweety"), Dog("Fido")]

for animal in animals:
    print(f"{animal.name}: {animal.speak()}")
```

One list holds several kinds of object. The loop calls the same method on each one, and
each object answers in its own way. The loop never asks what kind of animal it has.

Ask them what has to change in the loop to add a `Cow`. The answer is nothing. They write
the `Cow` class and put a cow in the list. This is the main reason to use inheritance,
because the code that uses the objects does not grow every time a new kind is added.

If they read about this elsewhere, they will meet the word polymorphism (many kinds of
object answering the same method call, each in its own way). Give them the word once, so
they recognise it, and then go back to plain words.

## 6. When not to use inheritance

Give this section as much time as the rest of the unit, because beginners who have just
learned inheritance tend to use it everywhere.

**The test is to read it out loud.** "A Dog is an Animal" is true, so `Dog(Animal)` is
fine. "A SavingsAccount is a BankAccount" is true. "A Car is an Engine" is false. A car
has an engine. "A ShoppingCart is an Item" is false. A cart holds items. When the true
sentence uses "has" or "holds", use an attribute instead of inheritance, as with the
cart and its list of items in exercise 11.15.

Go through a few with them and let them decide.

- Square and Shape. A square is a shape, so inheritance can fit.
- Library and Book. A library has books, so use an attribute that holds a list.
- Student and Person. A student is a person, so it can fit, but only if the program
  also has other kinds of person.
- Wheel and Bike. A bike has wheels, so use an attribute.

**Prefer simple classes.** One class with no parent is the normal case. Only reach for
inheritance when there are two or more classes that really share code, and the "is a"
sentence reads true. If there is only one kind of thing, there is nothing to share.

**Keep the chain short.** One parent and a few children is the shape that stays easy to
follow. When a method is five classes away, finding out what runs becomes a puzzle.

---

## Teaching notes for this unit

**This is a short unit and it should feel like one.** One session, a handful of core
exercises, and the final open exercise. Do not add multiple inheritance, abstract
classes, or `__repr__`, even if the student asks. Say that they exist and that the
course stops here.

**Tracing "which method runs" is the core skill.** The rule to give them is "look in the
object's own class first, then the parent". When they get a prediction wrong, have them
say that rule out loud while pointing at the code, rather than explaining it again.

**The `self.speak()` call inside the parent is the moment that matters.** Most students
expect the parent's method to call the parent's `speak`. Seeing the child's version run
is the surprise that makes inheritance make sense. Exercise 12.2 is built around it.

**The classic mistakes, with the real messages from Python 3.14.**

- Forgetting `super().__init__(...)`. `AttributeError: 'GuideDog' object has no attribute
  'name'`, and it shows up later, in whichever method first uses the attribute.
- Passing `self` to it, as `super().__init__(self, name, age)`.
  `TypeError: Animal.__init__() takes 3 positional arguments but 4 were given`. Python
  passed `self` already, so it was counted twice. This is the "one more argument than
  you typed" rule from unit 11 again.
- Forgetting the brackets after `super`, as `super.__init__(name, age)`. `TypeError:
  descriptor '__init__' requires a 'super' object but received a 'str'`. The message is
  hard to read. The useful part is the word `super`, which points at the line to check.
- Defining the child above the parent. `NameError: name 'Animal' is not defined`.
- Misspelling the name of a method they meant to override. There is no error at all, and
  the parent's version runs.

**Do not let inheritance replace thinking about data.** If they build `Car(Engine)`,
ask them to read it out loud as "a car is an engine". They will usually fix it
themselves.

**The final exercise is the end of the course.** Treat 12.12 the same way the lesson for
unit 10 treats its last exercise. They work from an empty file, and you only answer
questions. A class is part of the brief this time, but if their idea fits better without
inheritance, that is a good choice and worth praising. The signs of success are the
same as before. They get something running early, read their errors, and can explain
every part.

**Leave them with somewhere to go.** The end of the unit 12 exercises has a "Where to go
next" section for the student. Read it with them. Recommend the official tutorial at
docs.python.org/3/tutorial, and offer to look at whatever they write next.
