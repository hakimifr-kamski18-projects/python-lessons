---
title: Glossary
---
The difficult words used in this course, explained in the shortest way that works. If a
word is not here and it is still confusing, look it up or search for it online. Add
the word `python` to your search.

This course uses one word for each idea, the same word every time. If you see
"argument" and "parameter" in the same sentence, that is on purpose, and this page
tells you the small difference.

---

## The ones about values

**value** — a piece of data. `25`, `"hello"`, `[1, 2]`.

**variable** — a name for a value. `age = 25` makes a variable called `age`.

**type** — what kind of value something is. Check it with `type(x)`.

**int** — a whole number. `25`. Short for integer.

**float** — a number with a decimal point. `1.75`. It is called a float for
historical reasons and the name does not mean anything useful.

**string** — text, in quotes. `"hello"`. Short for "string of characters".

**boolean** — a value that is either `True` or `False`. Named after a mathematician
called Boole.

**None** — the value that means "nothing here". What you get back from a function
that forgot to `return`.

**literal** — a value written directly in the code, like `25` or `"hello"`. A name
such as `age` is not a literal.

**truthy and falsy** — how a value counts inside an `if`. Falsy values count as
`False`. They are `0`, `""` (empty text), `[]` (an empty list) and `None`. Almost
everything else is truthy.

**f-string** — text with an `f` in front, where `{}` holds a value. `f"Hi {name}"`.

**title case** — every Word Starts With A Capital Letter. `"ada lovelace".title()`
gives `"Ada Lovelace"`.

**newline** — the invisible character that ends a line. Written `\n` inside text. Each
line you read from a file ends with one.

**escape character** — a backslash `\` followed by a letter, which stands for a
special character. `\n` is a newline and `\t` is a tab.

**trailing** — at the end. A trailing space is a space at the end of the text, which
you cannot see.

**repr** — a function that shows a value the way it is written in code, with quotes
and hidden spaces visible. `print(repr("hi "))` shows `'hi '`.

**case sensitive** — treating `A` and `a` as different. Python names and text
comparisons are case sensitive.

**normalise** — change text into one standard form, so that two things that mean the
same become equal. For example `.strip().lower()` on an answer.

---

## The ones about storing things

**list** — an ordered collection whose contents you can change. `[1, 2, 3]`.

**dictionary** — a collection you look things up in by name. `{"Ada": 88}`.

**tuple** — like a list, but it cannot be changed. `(3, 4)`. Said like "tupple", to
rhyme with "couple".

**unpack** — take a group apart into separate variables. `x, y = point` unpacks the
tuple `point`. `for a, b in pairs:` unpacks each pair in turn.

**key** — the name you use to look something up in a dictionary.

**index** — a position in a list or string. Positions start at zero, so the first
item is at index 0.

**slice** — a piece cut out of a list or string. `name[1:4]`.

**sequence** — anything with items in an order that you can walk through. Strings,
lists and tuples are sequences.

**swap** — trade the values of two variables. In Python, `a, b = b, a`.

**nested** — put inside another one. A list inside a list is nested.

**in place** — changed directly, without making a new copy. `sort()` changes a list
in place. `sorted()` does not.

**alias** — a second name for the same list (or dictionary). `b = a` makes `b` an alias
of `a`, so changing one changes both. It is not a copy.

**pair** — two values that belong together, such as `("Ada", 88)`.

**parallel lists** — two lists where the item at position 0 in one belongs with the
item at position 0 in the other.

**hashable** — a value that cannot be changed, so it is allowed as a dictionary key.
Text, numbers and tuples are hashable. Lists are not.

---

## The ones about changing things

**mutable** — can be changed after it is made. Lists and dictionaries are mutable.

**immutable** — cannot be changed after it is made. Strings and tuples are
immutable. Once you make a string, it stays that way. To "change" it you build a
new one.

**assignment** — putting a value into a variable, with `=`. Assignment replaces
whatever was in the variable before.

**initialise** — give something its first value. "Initialise `total` to 0" means
write `total = 0` before the loop.

**increment** — add one to something. `count += 1`. It comes from a Latin word. If
you are adding something other than 1, say "add to" instead.

**accumulator** — a variable you add to on every pass of a loop. It accumulates,
meaning it collects more and more. `total` in a sum is an accumulator.

**pattern** — a way of writing code that you use again and again. The counting pattern
and the accumulator are two.

**trace** — follow a loop by hand on paper, with one column for each variable and one
row for each pass.

**off-by-one** — a mistake where a loop or a position is one too many or one too few.
`range(5)` stops at 4, not 5.

**edge case** — an unusual input at the edge of what is allowed, like an empty list or
zero. Test it on purpose.

---

## The ones about doing things

**operator** — a symbol that does something to values. `+`, `-`, `==`, `and`.

**operand** — one of the values an operator works on. In `2 + 3`, both `2` and `3`
are operands.

**expression** — anything that produces a value. `2 + 3` is an expression, and so is
`"hello"`.

**statement** — one complete instruction. `x = 5` is a statement.

**precedence** — which operation happens first. In `2 + 3 * 4` the multiplication
has higher precedence, so it happens first and the answer is 14.

**condition** — something that comes out `True` or `False`. An `if` runs on a
condition.

**evaluate** — work out the value of. "Python evaluates the right side first" means
it works out the right side first.

**branch** — one of the paths in an `if`. The `if`, each `elif` and the `else` are
branches. Only one of them runs.

**keyword** — a word that Python has reserved for itself, such as `if`, `for`, `def`
and `return`. You cannot use it as a variable name.

**side effect** — something a function does besides giving back a value, such as
printing or changing a list.

---

## The ones about functions

**function** — a named block of code you can run whenever you like. Made with `def`.

**method** — a function that belongs to a value, written after a dot. In
`name.upper()`, `upper` is a method of the string `name`. The methods you write
yourself go inside a class, and their first parameter is `self`.

**call** — run a function. `greet()` calls `greet`.

**parameter** — the name in the function definition that receives a value. In
`def greet(name):`, `name` is the parameter.

**argument** — the value you actually pass in. In `greet("Ada")`, `"Ada"` is the
argument.

The difference is small. Parameter is the name in the definition, argument is the
real value you pass. Nobody will be confused if you mix them up.

**return** — hand a value back from a function to whatever called it. Different from
`print`, which only shows it on the screen.

**default argument** — a value used when the caller does not give one.
`def greet(name, greeting="Hello")` has a default of `"Hello"`.

**keyword argument** — passing a value by naming the parameter.
`greet(name="Ada")`.

**scope** — which parts of the program can see a variable. A variable made inside a
function is only in scope inside that function.

**local** — only exists inside the function where it was made.

**global** — exists for the whole program, not just inside one function.

**docstring** — a short note at the top of a function saying what it does. Written
as a string, not a comment.

---

## The ones about errors

**bug** — a mistake in a program. Everyone makes them, every day.

**exception** — Python's word for an error that happens while the program is
running. Unit 05 is about them.

**try / except** — `try` runs code that might fail, and `except` says what to do if one
named type of error happens. `except ValueError:` handles only a `ValueError`.

**catch** — handle an error with `except`, so the program does not stop.

**bare except** — an `except:` with no type after it. It catches every error, including
typos in your own code, so do not use it.

**raise** — start an error. Python raises an error when something goes wrong, so "it
raises a `ValueError`" means that error happened. You can also do it yourself with
`raise ValueError("message")`.

**traceback** — the text Python prints when a program stops with an error. It starts
with the words `Traceback (most recent call last)`. Read it from the bottom up.

**caret** — the `^` mark. In a SyntaxError it points at the spot where Python got
confused.

**syntax** — the rules about what valid Python looks like. A syntax error means the
file is not valid Python, so none of it runs.

**whitespace** — spaces, tabs and blank lines. In Python, whitespace at the start of
a line is part of the code, not decoration.

**indentation** — the spaces at the start of a line. Four spaces, always.

---

## The ones about organising code

**module** — a file of code you can import and use. `random`, `json`, and your own
files.

**import** — pull a module into your program so you can use it.

**comment** — a note for humans, starting with `#`. Python ignores it completely.

**prompt** — the text shown to ask the user for something. In `input("Name? ")`, the
prompt is `Name? `.

**editor** — the program where you type and run your code.

**console** — the window or panel where a program shows its output and where you can
type. Also called the terminal or the shell.

**type hint** — a note in the code about which type a value should have, like
`def f(n: int)`. Python does not enforce it. Not taught in this course.

**refactor** — change the code without changing what it does. You do it to make the
code clearer.

**boilerplate** — fixed code you copy and paste every time without changing much.
The `if __name__ == "__main__":` block is boilerplate.

**validation loop** — a loop that asks again until the answer is valid. Usually
`while True` with `try`, `int(input())` and `break`, from unit 05.

**guard** — a check at the top of a block that stops something bad happening. The
`if not items:` check before a loop is a guard.

**algorithm** — a set of steps for solving a problem. A recipe is an algorithm.

**binary search** — cutting the range in half again and again to find something
fast. Guess 50, then 25 or 75, and so on.

**recursion** — a function that calls itself.

**comprehension** — a short way of writing a loop that builds a list. Not taught in
this course, but you will see it.

**library** — a collection of code somebody else wrote, ready to use. The standard
library is the one that comes with Python.

---

## The ones about classes

**class** — a way to make your own type of value, with its own data and its own
methods. Made with `class`, like `class BankAccount:`. Unit 11 is about them.

**object** — one value made from a class. `account = BankAccount("Ada")` makes an
object. Every value in Python is an object, which is why errors say `'str' object`.

**instance** — another word for object. An object made from `BankAccount` is an
instance of `BankAccount`. This course mostly says object.

**attribute** — a variable that belongs to an object, written after a dot.
`account.balance` is an attribute.

**self** — the name a method uses for the object it was called on. It is always the
first parameter of a method, and attributes inside the class are written
`self.balance`.

**`__init__`** — the method that sets up a new object. Python runs it by itself when you
create the object, so it is where the attributes get their first values. Two
underscores on each side. People say it as "dunder init".

**`__str__`** — the method that gives the text `print()` shows for an object.

**inheritance** — making a new class from one that already exists, so the new class
gets all of its methods. Unit 12 is about it.

**parent class** — the class that another class is made from. In `class Dog(Animal):`,
`Animal` is the parent class. Other tutorials say base class or superclass.

**child class** — a class made from a parent class. In `class Dog(Animal):`, `Dog` is
the child class. It gets everything the parent has, and can add or change things.
Other tutorials say subclass.

**override** — replace a method from the parent class, by writing a method with the same
name in the child class. The child's version is the one that runs.

**super()** — gives you the parent class from inside a child class.
`super().__init__(name)` runs the parent's `__init__`.

**isinstance** — a function that checks the type of an object. `isinstance(rex, Dog)`
is `True` if `rex` is a `Dog`, or an object of a child class of `Dog`.

**polymorphism** — many types of object answering the same method call, each in its own
way. A list of shapes where every shape has its own `area()` is an example. This course
does not use the word, but other tutorials do.

---

## Words this course does not use, on purpose

These are common in tutorials and in real code, and this course replaces them with
something simpler. If you meet one, come back to this list.

**iterate** — This course says "go through the items" instead. It means the same
thing.

**concatenate** — This course says "glue together" or "join". Python's own error
messages use "concatenate", so you will see it in a `TypeError`.

**parse** — This course says "read" or "work out". It means taking text apart and
understanding its structure.

**instantiate** — creating an object from a class. This course says "create an
object" instead.

**deprecated** — old and no longer recommended. You will see it in documentation.

**terminate** — stop. This course says stop.

**utilise** — use.

**implement** — write. "Implement a function" just means "write a function".

**invoke** — call. "Invoke a function" means "call a function".

**redundant** — not needed, because something else already does it.

**verbose** — too long. This course says "more code than it needs".

**concise** — short. This course says "short".

**explicit** — stated clearly, written out. This course says "spelled out".

**implicit** — not stated, but understood. This course says "not written down".

**arbitrary** — any value would do, it does not matter which. This course says
"any" or "does not matter".

**ambiguous** — could mean more than one thing. This course says "unclear".

**caveat** — a warning. This course says "warning" or "but there is a catch".

**boilerplate** is above, and it is the one exception, because there is no shorter
way to say it.
