---
title: Unit 12 exercises
sidebar:
  label: Exercises
---
These are the last exercises in the course. Most of them are about one question. When
you call a method, which version runs? Answer it on paper before you run the code. The
very last exercise has no prompt at all.

---

## Before you start

These are the ideas the exercises use. Read them once, then come back if you get stuck.

Inheritance (making a new class from one that already exists) lets two or more classes
share code instead of copying it. You put the name of the existing class in brackets
after the new class name. The existing class is the parent class (the class that another
class is made from), and the new one is the child class (a class made from a parent
class).

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def describe(self):
        return f"{self.name} says {self.speak()}"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Fish(Animal):
    pass


print(Dog("Rex").describe())     # Rex says Woof
print(Fish("Nemo").describe())   # Nemo says ...
```

The child gets every method of the parent, including `__init__`. `Fish` has only
`pass` in its body, and it still has a name and a `describe` method.

To override (replace a method from the parent class), write a method with the same name
in the child class. `Dog` overrides `speak`.

When you call a method, Python looks in the object's own class first. If the method is
not there, it looks in the parent. That rule explains the surprising part of the example
above. `describe` is written in `Animal`, and it calls `self.speak()`. For Rex, `self` is
a `Dog`, so Python looks in `Dog` first and finds `"Woof"`.

If the child needs more attributes than the parent, write an `__init__` in the child and
call `super().__init__(...)` first. `super()` gives you the parent class from inside a
child class, so `super().__init__(...)` runs the parent's version, which sets up what the
parent needs. Then the child
adds what is new.

```python
class Animal:
    def __init__(self, name):
        self.name = name


class GuideDog(Animal):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner


buddy = GuideDog("Buddy", "Sam")
print(buddy.name, buddy.owner)   # Buddy Sam
```

Do not pass `self` to `super().__init__`. It is passed for you. If you leave out the
`super().__init__` line, the parent's setup never runs, and you get an `AttributeError`
later, the first time anything uses an attribute the parent should have set.

`super()` works for any method. `return super().describe() + "!"` runs the parent's
`describe` and adds to its answer.

`isinstance(object, class)` is a function that checks the type of an object. It gives
`True` if the object was made from that class or from a child of it, so a `Dog` is also
an `Animal`.

```python
class Animal:
    pass


class Dog(Animal):
    pass


rex = Dog()
print(isinstance(rex, Dog))      # True
print(isinstance(rex, Animal))   # True
print(isinstance(42, int))       # True, it works for every type
```

A list can hold objects of different child classes. When a loop calls the same method on
each one, each object answers in its own way, and the loop does not need to know which
kind it has.

Before you use inheritance, read the sentence "a Dog is an Animal" out loud with your
two class names. If it is true, inheritance can fit. If the true sentence is "a Car has
an Engine", use an attribute instead. A plain class with no parent is the normal case.

---

## Warm-ups

### 12.1 Predict which method runs

```python
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        return "moves"

    def stop(self):
        return "stops"


class Boat(Vehicle):
    def move(self):
        return "sails"


class Plane(Vehicle):
    def move(self):
        return "flies"

    def stop(self):
        return "lands"


boat = Boat("Nina")
plane = Plane("Comet")
van = Vehicle("Van")

print(boat.name, boat.move(), boat.stop())
print(plane.name, plane.move(), plane.stop())
print(van.name, van.move(), van.stop())
```

For each of the nine method calls, say which class the method came from.

### 12.2 Predict which method runs, part two

```python
class Robot:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "Hello"

    def introduce(self):
        return f"{self.greeting()}, I am {self.name}"


class PirateRobot(Robot):
    def greeting(self):
        return "Ahoy"


class PoliteRobot(Robot):
    def introduce(self):
        return super().introduce() + ". Pleased to meet you."


print(Robot("R2").introduce())
print(PirateRobot("Hook").introduce())
print(PoliteRobot("Jeeves").introduce())
```

The second line is the one to think hardest about. `PirateRobot` does not have an
`introduce` method of its own.

### 12.3 The forgotten super().__init__

This is meant to print the school and then `Hi, I am Ada`. It prints the school and then
crashes.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I am {self.name}"


class Student(Person):
    def __init__(self, name, school):
        self.school = school


ada = Student("Ada", "Hill School")
print(ada.school)
print(ada.greet())
```

Read the error. Which line does it point at, and where is the real mistake? Fix it.

### 12.4 isinstance, true or false

Write down `True` or `False` for each line before you run it.

```python
class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


rex = Dog()
tom = Cat()
thing = Animal()

print(isinstance(rex, Dog))
print(isinstance(rex, Animal))
print(isinstance(tom, Dog))
print(isinstance(thing, Animal))
print(isinstance(thing, Cat))
print(isinstance(5, int))
print(isinstance("5", int))
```

---

## Core

### 12.5 Shapes

Write a parent class `Shape` that stores a name. Give it a method `area()` that returns
0, and a method `describe()` that returns text like `Circle with area 3.14`, using
`self.area()` and two decimal places.

Then write two child classes.

- `Circle`, made with a radius. Its area is `math.pi * radius ** 2`.
- `Square`, made with the length of one side. Its area is the side times itself.

Each child calls `super().__init__(...)` with its own name, such as `"Circle"`, so the
user only has to give the measurements, as in `Circle(2)`.

Put a few circles and squares in one list. Print `describe()` for each, and the total
area of all of them at the end. Then add a `Rectangle` child, and notice what you do not
have to change.

### 12.6 Employee and Manager

Write a class `Employee` with a name and a yearly salary. Give it a method
`yearly_pay()` that returns the salary, and a method `describe()` that returns
`Ada earns 30000 a year`, using `self.yearly_pay()`.

Then write `Manager`, a child of `Employee`. A manager also has a bonus, so `Manager`
needs its own `__init__` that calls `super().__init__(name, salary)` and then stores the
bonus. Override `yearly_pay()` so that a manager's pay is the salary plus the bonus. Use
`super().yearly_pay()` inside it rather than writing `self.salary` again.

Make a list of staff with at least one manager. Print `describe()` for each person, and
the total pay of everyone.

You did not override `describe()` in `Manager`. Explain why it still shows the pay with
the bonus.

### 12.7 Vehicle, Car and Bike

Write a parent class `Vehicle` with a name and a number of wheels. Give it a method
`noise()` that returns `"..."` and a method `describe()` that returns text like
`Raleigh has 2 wheels and goes ring ring`.

Then write two children.

- `Car` is made with a name and a number of seats, as in `Car("Fiesta", 5)`. A car
  always has 4 wheels, so its `__init__` passes 4 to `super().__init__`. Its noise is
  `"vroom"`. Override `describe()` so it adds the seats at the end, using
  `super().describe()`.
- `Bike` is made with only a name. It always has 2 wheels. Its noise is `"ring ring"`.

Put cars, bikes and one plain `Vehicle` in a list. Print `describe()` for each, and the
total number of wheels.

### 12.8 Only the managers

Use your `Employee` and `Manager` classes from 12.6. Make a list of four or more staff,
with at least two managers.

Go through the list once. Use `isinstance` to print the name of every manager, to count
the managers, and to add up their bonuses. Print the count and the total of the bonuses
at the end.

Then count how many items in the list are an `Employee`, also with `isinstance`. Before
you run it, predict whether the managers are counted.

Why would `person.bonus` crash if you used it without the `isinstance` check?

### 12.9 Is a, or has a?

For each pair, write the sentence out, either "an X is a Y" or "an X has a Y". Then decide
whether the first should be a child class of the second, or whether it should hold the
second as an attribute. Some of them could go either way, so give your reason.

1. `Square` and `Shape`
2. `Car` and `Engine`
3. `Student` and `Person`
4. `Library` and `Book`
5. `Penguin` and `Bird`
6. `Playlist` and `Song`
7. `SavingsAccount` and `BankAccount`
8. `Bike` and `Wheel`

There is no code to write for this one, but making this decision well is the most useful
skill in the unit.

---

## Stretch

### 12.10 Kinds of bank account

Start from a `BankAccount` class with an owner, a balance with a default of 0, a
`deposit(amount)` and a `withdraw(amount)` that both raise a `ValueError` for bad
amounts, and a `__str__` that shows `Ada has 150`. If you wrote one in exercise 11.10,
use that.

Then write two children.

- `SavingsAccount` also takes an interest rate, as a whole number of percent, with a
  default of 2. It has a method `add_interest()` that adds the interest to the balance
  and returns how much was added. To keep the balance a whole number, work the interest
  out with `self.balance * self.rate // 100`. The `//` divides and throws away anything
  after the decimal point.
- `CheckingAccount` also takes an overdraft limit, with a default of 100. This is how far
  below zero the balance is allowed to go. Override `withdraw` so that it allows the
  balance to go negative, but not past the limit.

Test each rule. Add interest to a savings account. Try to take too much out of it. Take
an account with an overdraft below zero, then try to go past the limit.

Then put one of each kind of account in a list, print each one, and use `isinstance` to
point out the one that earns interest.

### 12.11 A small zoo

Write a parent class `Animal` with a name, a `speak()` method, a `food()` method and a
`__str__` that shows `Leo says Roar and eats meat`. Then write at least three children,
each with its own sound and food. Give one of them an extra attribute, such as a parrot
that is made with the words it says, so that it needs `super().__init__`.

Then write a class `Zoo`. Think about 12.9 first. A zoo is not an animal. A zoo has
animals. So `Zoo` is a plain class with no parent, and it holds a list of animals as an
attribute.

- `add(animal)` adds an animal.
- `feeding_time()` prints one line per animal with its name and its food.
- `count(kind)` returns how many animals in the zoo are of that kind, using
  `isinstance`. You call it with a class, as in `zoo.count(Penguin)`. A class can be
  passed to a function like any other value.

Fill the zoo, print every animal, run feeding time, and print a couple of counts. Try
`zoo.count(Animal)` too, and explain the answer.

---

## Check yourself

Try to do these without looking at your notes.

- Write a child class that overrides one method and keeps the rest from its parent.
- Write a child `__init__` that uses `super().__init__(...)` and adds an attribute.
- Say which method runs when a parent's method calls `self.something()` and the child
  overrides `something`.
- Find the bug when a child object is missing an attribute that the parent sets.
- Use `isinstance` to pick one kind of object out of a mixed list.
- Decide, with the "is a" sentence, whether inheritance fits a problem at all.

---

## The last exercise

### 12.12 Build something of your own

No prompt and no starter code. From an empty file, write a program that you want, built
around at least one class you design yourself. Use inheritance only if the "is a"
sentence reads true for your idea. Many good programs have one or two plain classes and
no inheritance at all.

If you need a starting point, here are some shapes that work well with a class. A
habit tracker where each habit knows how many days in a row you have done it. A small
card game with a `Card` and a `Deck`. A recipe book that saves its recipes to JSON. A
quiz where each question checks its own answer.

The advice is the same as at the end of unit 10, and it is the advice for every project
from now on.

- Start by writing down what the program holds and what it does. The things it holds are
  attributes, and the things it does are methods.
- Write the smallest class that does anything at all, make one object, and print it.
- Get that running before adding anything.
- When something breaks, read the error before changing anything.
- Add one thing at a time.

If you get stuck, ask a smaller question. Instead of "how do I write this program", ask
"how do I get this one object to print its name".

---

## Where to go next

You have finished the course. You can write programs with variables, decisions, loops,
lists, dictionaries, functions, files and your own classes, and you can read the errors
when they go wrong. Here is what to learn next, in a sensible order.

1. **List comprehensions** (a short way of writing a loop that builds a list), such as
   `[x * 2 for x in numbers]`. They take about twenty minutes to learn, and they are
   everywhere in real code.
2. **Your own kinds of error.** You can do this already. An error type is a class, so
   `class NotEnoughMoney(ValueError): pass` makes a new one, and you can `raise` it and
   catch it with `except NotEnoughMoney`. Try it with the bank account from exercise
   12.10.
3. **More about classes.** `__repr__` (the method that controls how an object looks
   inside a printed list) and dataclasses (a shorter way to write a class that mostly
   holds data) are the next two to look up. Both build on what you know.
4. **Type hints** (notes in the code about which type a value should have), such as
   `def add(a: int, b: int) -> int:`. You do not have to write them, and Python does
   not check them, but other tools can. They are very common in real code.
5. **Testing,** meaning writing code that checks your other code. Python comes with a
   module for it called `unittest`, and many people use a library called `pytest`.
6. **Reading and writing better code,** which mostly means naming things well, keeping
   functions and methods short, and reading code that other people wrote.

The official Python tutorial at docs.python.org/3/tutorial covers all of this, and you
now know enough to read it.

The most useful thing of all is not on any list. Write something you actually want, even
if you write it badly, and then improve it. That is what everybody does, including people who have
been doing this for twenty years.
