---
title: Glossary
---
Every difficult word used in the lessons, explained in the shortest way I could
manage. If a word is not here and it is still confusing, write it down and ask.

The lessons use one word for each idea, the same word every time. If you see
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

---

## The ones about storing things

**list** — an ordered collection whose contents you can change. `[1, 2, 3]`.

**dictionary** — a collection you look things up in by name. `{"Ada": 88}`.

**tuple** — like a list, but it cannot be changed. `(3, 4)`. Said like "tupple", to
rhyme with "couple".

**key** — the name you use to look something up in a dictionary.

**index** — a position in a list or string. Positions start at zero, so the first
item is at index 0.

**slice** — a piece cut out of a list or string. `name[1:4]`.

**sequence** — anything with items in an order that you can walk through. Strings,
lists and tuples are sequences.

**nested** — put inside another one. A list inside a list is nested.

**in place** — changed directly, without making a new copy. `sort()` changes a list
in place. `sorted()` does not.

**alias** — two names pointing at the same thing. `b = a` makes `b` an alias of the
list `a`, so changing one changes both.

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

---

## The ones about functions

**function** — a named block of code you can run whenever you like. Made with `def`.

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

**unpack** — take a group apart into separate variables. `x, y = point` unpacks the
tuple `point`.

**docstring** — a short note at the top of a function saying what it does. Written
as a string, not a comment.

---

## The ones about errors

**bug** — a mistake in a program. Everyone makes them, every day.

**exception** — Python's word for an error that happens while the program is
running.

**catch** — handle an error with `except`, so the program does not stop.

**raise** — when Python signals that an error has happened. "It raises a
`ValueError`" means that error happened.

**traceback** — the block of red error text. Read it from the bottom up.

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

**refactor** — change the code without changing what it does. You do it to make the
code clearer.

**boilerplate** — fixed code you copy and paste every time without changing much.
The `if __name__ == "__main__":` block is boilerplate.

**validation loop** — a loop that keeps asking until it gets a usable answer.

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

## Words the lessons deliberately do not use

These are common in tutorials and in real code, and they are replaced with something
simpler here. If you meet one, come back to this list.

**iterate** — the lessons say "go through the items" instead. It means the same
thing.

**concatenate** — the lessons say "glue together" or "join". Python's own error
messages use "concatenate", so you will see it in a `TypeError`.

**parse** — the lessons say "read" or "work out". It means taking text apart and
understanding its structure.

**instantiate** — creating an object from a class. Not needed in this course.

**deprecated** — old and no longer recommended. You will see it in documentation.

**terminate** — stop. The lessons say stop.

**utilise** — use.

**implement** — write. "Implement a function" just means "write a function".

**invoke** — call. "Invoke a function" means "call a function".

**redundant** — not needed, because something else already does it.

**verbose** — too long. The lessons say "more code than it needs".

**concise** — short. The lessons say "short".

**explicit** — stated clearly, written out. The lessons say "spelled out".

**implicit** — not stated, but understood. The lessons say "not written down".

**arbitrary** — any value would do, it does not matter which. The lessons say
"any" or "does not matter".

**ambiguous** — could mean more than one thing. The lessons say "unclear".

**caveat** — a warning. The lessons say "warning" or "but there is a catch".

**boilerplate** is above, and it is the one exception, because there is no shorter
way to say it.
