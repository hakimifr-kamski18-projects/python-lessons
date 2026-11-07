---
title: Unit 12 solutions
sidebar:
  label: Solutions
---
## Warm-ups

### 12.1 Predict which method runs

```
Nina sails stops
Comet flies lands
Van moves stops
```

Here is where each method came from.

- `boat.move()` comes from `Boat`, which overrides it. `boat.stop()` comes from
  `Vehicle`, because `Boat` has no `stop`, so Python looks in the parent.
- `plane.move()` and `plane.stop()` both come from `Plane`, which overrides both.
- `van` is a plain `Vehicle`, so both methods come from `Vehicle`. A parent class never
  uses its children's methods for its own objects.
- `name` is set by `Vehicle.__init__` in all three cases. None of the children has an
  `__init__`, so they all use the parent's.

The rule behind every answer is "look in the object's own class first, then the
parent".

### 12.2 Predict which method runs, part two

```
Hello, I am R2
Ahoy, I am Hook
Hello, I am Jeeves. Pleased to meet you.
```

The second line is the interesting one. `PirateRobot` has no `introduce`, so Python runs
the one in `Robot`. Inside it, `self.greeting()` is called. `self` is Hook, which is a
`PirateRobot`, so Python looks in `PirateRobot` first and finds `"Ahoy"`. The method was
written in the parent, but it used the child's `greeting`.

If you said `Hello, I am Hook`, this is the idea to look at again. The method that runs
depends on the object that `self` is, not on the class where the calling code was
written.

The third line uses `super().introduce()`. That runs the parent's `introduce`, which
gives `Hello, I am Jeeves`, and then the child adds its own sentence on the end.

### 12.3 The forgotten super().__init__

```
AttributeError: 'Student' object has no attribute 'name'
```

The error points at the line in `greet`, inside `Person`. But `greet` is fine. The real
mistake is in `Student.__init__`.

Writing an `__init__` in `Student` overrides the one in `Person`. So when
`Student("Ada", "Hill School")` runs, only the child's `__init__` runs. It sets
`self.school`, and nothing ever sets `self.name`. The problem only shows up later, when
`greet` tries to read it.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, I am {self.name}"


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school


ada = Student("Ada", "Hill School")
print(ada.school)   # Hill School
print(ada.greet())  # Hi, I am Ada
```

When a child object is missing an attribute that the parent sets, look for a missing
`super().__init__` first. It is the most common bug with inheritance.

### 12.4 isinstance, true or false

```
True
True
False
True
False
True
False
```

- `isinstance(rex, Animal)` is `True`, because a `Dog` is an `Animal`. The check
  includes the parent.
- `isinstance(tom, Dog)` is `False`. Cats and dogs share a parent, but a cat is not a
  dog.
- `isinstance(thing, Cat)` is `False`. It only works upwards. A plain `Animal` is not any
  particular child.
- The last two lines work with the built-in types. `"5"` is text, not an `int`, which is
  the `input()` problem from unit 02 in a new form.

---

## Core

### 12.5 Shapes

```python
import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def describe(self):
        return f"{self.name} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(1), Square(3), Circle(2.5), Rectangle(2, 5)]

total = 0
for shape in shapes:
    print(shape.describe())
    total += shape.area()

print(f"Total area: {total:.2f}")
```

```
Circle with area 3.14
Square with area 9.00
Circle with area 19.63
Rectangle with area 10.00
Total area: 41.78
```

Each child passes its own name to `super().__init__`, so `Circle(2)` only needs the
radius. The name is a fixed part of being a circle, so the user does not have to type
it.

`describe` is written once, in `Shape`. It calls `self.area()`, and each child's own
`area` runs. That is the same idea as 12.2.

Adding `Rectangle` changed nothing outside the new class, and the loop and `describe`
stayed exactly the same. This is the main reason to use inheritance, because the code
that uses the shapes does not grow when a new kind of shape arrives.

### 12.6 Employee and Manager

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_pay(self):
        return self.salary

    def describe(self):
        return f"{self.name} earns {self.yearly_pay()} a year"


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def yearly_pay(self):
        return super().yearly_pay() + self.bonus


staff = [
    Employee("Ada", 30000),
    Manager("Grace", 40000, 5000),
    Employee("Alan", 28000),
]

for person in staff:
    print(person.describe())

total = 0
for person in staff:
    total += person.yearly_pay()
print(f"Total: {total}")
```

```
Ada earns 30000 a year
Grace earns 45000 a year
Alan earns 28000 a year
Total: 103000
```

`describe()` still shows the bonus for Grace because it calls `self.yearly_pay()`, and
for Grace, `self` is a `Manager`. Python finds the manager's `yearly_pay` first. You
changed one method, and every method that uses it got the new answer.

`super().yearly_pay()` gets the parent's answer, which is the salary, and adds the
bonus. Writing `self.salary + self.bonus` gives the same number today. The `super()`
version keeps working if the rule for normal pay ever changes, for example to add
overtime, because the manager builds on the employee's rule rather than copying it.

### 12.7 Vehicle, Car and Bike

```python
class Vehicle:
    def __init__(self, name, wheels):
        self.name = name
        self.wheels = wheels

    def noise(self):
        return "..."

    def describe(self):
        return f"{self.name} has {self.wheels} wheels and goes {self.noise()}"


class Car(Vehicle):
    def __init__(self, name, seats):
        super().__init__(name, 4)
        self.seats = seats

    def noise(self):
        return "vroom"

    def describe(self):
        return super().describe() + f", with {self.seats} seats"


class Bike(Vehicle):
    def __init__(self, name):
        super().__init__(name, 2)

    def noise(self):
        return "ring ring"


vehicles = [Car("Fiesta", 5), Bike("Raleigh"), Car("Mini", 4), Vehicle("Cart", 3)]

for vehicle in vehicles:
    print(vehicle.describe())

wheels = 0
for vehicle in vehicles:
    wheels += vehicle.wheels
print(f"Wheels in total: {wheels}")
```

```
Fiesta has 4 wheels and goes vroom, with 5 seats
Raleigh has 2 wheels and goes ring ring
Mini has 4 wheels and goes vroom, with 4 seats
Cart has 3 wheels and goes ...
Wheels in total: 13
```

The child's `__init__` does not have to take the same parameters as the parent's. `Car`
takes a name and seats, and fills in the wheels itself, because every car has 4. The
parent still gets both of the values it needs.

`Car.describe` adds to the parent's version with `super().describe()`. Notice that the
parent's `describe` still calls `self.noise()`, which gives `"vroom"` for a car. So the
car adds to one parent method and overrides another, and the two work together.

`Bike.__init__` only exists to fill in the 2. Without it, you would have to write
`Bike("Raleigh", 2)` every time.

### 12.8 Only the managers

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_pay(self):
        return self.salary


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def yearly_pay(self):
        return super().yearly_pay() + self.bonus


staff = [
    Employee("Ada", 30000),
    Manager("Grace", 40000, 5000),
    Employee("Alan", 28000),
    Manager("Linus", 45000, 7000),
]

managers = 0
bonuses = 0
for person in staff:
    if isinstance(person, Manager):
        managers += 1
        bonuses += person.bonus
        print(f"Manager: {person.name}")

print(f"{managers} managers, {bonuses} in bonuses")

everyone = 0
for person in staff:
    if isinstance(person, Employee):
        everyone += 1
print(f"{everyone} employees")
```

```
Manager: Grace
Manager: Linus
2 managers, 12000 in bonuses
4 employees
```

The managers are counted as employees, because a `Manager` is an `Employee`. That is
the "is a" sentence, in code.

Without the `isinstance` check, `person.bonus` would crash on Ada with
`AttributeError: 'Employee' object has no attribute 'bonus'`. Only managers have a
bonus, because only `Manager.__init__` sets it. The check makes sure you only ask for it
on objects that have it.

`isinstance` is the right tool here, because the question really is "which of these are
managers?". When you want each kind of object to behave differently, an overridden
method is usually better, as in 12.6.

### 12.9 Is a, or has a?

1. A square is a shape, so a child class fits.
2. A car has an engine, so use an attribute. A car is not a kind of engine.
3. A student is a person. A child class can fit, but only if the program has other kinds
   of person that share code with students, such as teachers. If students are the only
   people in the program, one plain `Student` class is simpler.
4. A library has books, so use an attribute that holds a list of `Book` objects.
5. A penguin is a bird, so a child class fits. If the parent has a `fly()` method, the
   penguin is a warning, because a penguin cannot fly. Inheritance only works when the
   child can really do everything the parent can.
6. A playlist has songs, so use an attribute that holds a list of `Song` objects.
7. A savings account is a bank account, so a child class fits. It is exercise 12.10.
8. A bike has wheels, so use an attribute. It is usually just a number, as in 12.7.

Four of the eight are "has a", and that is typical. In real programs, holding other
objects as attributes is much more common than inheritance. If you are unsure, use an
attribute. It is easier to change later.

---

## Stretch

### 12.10 Kinds of bank account

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

    def __str__(self):
        return f"{self.owner} has {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=2):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate // 100
        self.balance += interest
        return interest


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0, overdraft=100):
        super().__init__(owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("A withdrawal must be more than zero")
        if amount > self.balance + self.overdraft:
            raise ValueError(f"That would go past the overdraft of {self.overdraft}")
        self.balance -= amount


savings = SavingsAccount("Ada", 1000, rate=5)
print(f"Interest: {savings.add_interest()}")
print(savings)

try:
    savings.withdraw(2000)
except ValueError as error:
    print(f"Savings: {error}")

checking = CheckingAccount("Grace", 50)
checking.withdraw(120)
print(checking)

try:
    checking.withdraw(100)
except ValueError as error:
    print(f"Checking: {error}")

accounts = [savings, checking, BankAccount("Alan", 10)]
for account in accounts:
    print(account)
    if isinstance(account, SavingsAccount):
        print("  this one earns interest")
```

```
Interest: 50
Ada has 1050
Savings: Not enough money, the balance is 1050
Grace has -70
Checking: That would go past the overdraft of 100
Ada has 1050
  this one earns interest
Grace has -70
Alan has 10
```

The two children use inheritance in two different ways.

- `SavingsAccount` adds something new, `add_interest`, and keeps every other method as it
  is. Its `withdraw` is the parent's, so it still refuses to go below zero.
- `CheckingAccount` changes something that exists. It overrides `withdraw` with a
  different rule. It keeps `deposit` and `__str__` from the parent.

Grace starts with 50 and takes out 120, which leaves her at -70. That is inside the limit
of 100. Taking out another 100 would leave her at -170, so it is refused, and the balance
stays at -70.

`rate=5` in `SavingsAccount("Ada", 1000, rate=5)` is a keyword argument (passing a value
by naming the parameter) from unit 07. It makes the call easier to read, because a bare
`5` would not say what it means.

`CheckingAccount.withdraw` repeats the check for a negative amount from the parent. That
is a small copy, and it is fine. Getting rid of it would make the code harder to follow,
and the rule is one line.

### 12.11 A small zoo

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

    def food(self):
        return "food"

    def __str__(self):
        return f"{self.name} says {self.speak()} and eats {self.food()}"


class Lion(Animal):
    def speak(self):
        return "Roar"

    def food(self):
        return "meat"


class Parrot(Animal):
    def __init__(self, name, words):
        super().__init__(name)
        self.words = words

    def speak(self):
        return self.words

    def food(self):
        return "seeds"


class Penguin(Animal):
    def food(self):
        return "fish"


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add(self, animal):
        self.animals.append(animal)

    def feeding_time(self):
        print(f"Feeding time at {self.name}")
        for animal in self.animals:
            print(f"  {animal.name} gets {animal.food()}")

    def count(self, kind):
        total = 0
        for animal in self.animals:
            if isinstance(animal, kind):
                total += 1
        return total


zoo = Zoo("City Zoo")
zoo.add(Lion("Leo"))
zoo.add(Parrot("Polly", "Hello!"))
zoo.add(Penguin("Pingu"))
zoo.add(Penguin("Pebble"))

for animal in zoo.animals:
    print(animal)

print()
zoo.feeding_time()

print()
print(f"Penguins: {zoo.count(Penguin)}")
print(f"Animals: {zoo.count(Animal)}")
```

```
Leo says Roar and eats meat
Polly says Hello! and eats seeds
Pingu says ... and eats fish
Pebble says ... and eats fish

Feeding time at City Zoo
  Leo gets meat
  Polly gets seeds
  Pingu gets fish
  Pebble gets fish

Penguins: 2
Animals: 4
```

This program uses both ways of putting classes together. The animals use inheritance,
because a lion is an animal. The zoo holds animals in a list attribute, because a zoo
has animals. Knowing which one to use is the main skill of this unit.

`Penguin` does not override `speak`, so a penguin says `...`, from the parent. A child
only overrides what is different.

`zoo.count(Penguin)` passes the class itself as an argument, without brackets. That is
the same idea as passing `len` to `sorted` in exercise 6.14. A class is a value like any
other, and `isinstance` needs the class, not an object. `zoo.count(Animal)` gives 4,
because every animal in the zoo is an `Animal`.

`feeding_time` does not check what kind each animal is. It calls `food()`, and each
object answers for itself.

---

## The last exercise

### 12.12 Build something of your own

There is no solution to 12.12, on purpose. Whatever you wrote is the answer.

If you want to check it, these are the questions worth asking. Did you get something
running early and build on it? Can you say what each class holds and what each method
does? Did you read your errors before changing anything? Do you know what you would add
next? If the answer to those is yes, it worked, whatever the program does.
