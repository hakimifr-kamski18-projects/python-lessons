# Python from Zero

Teaching material for people who have never written a line of code.

This collection has two audiences, and it is worth knowing which file is which before
you start.

The `lesson.md` files and everything in `instructor/` are written for the person
teaching. They assume you are sitting next to your student (or on a call), and they
contain pacing advice, common mistakes to watch for, and notes on how to react to a
wrong answer.

The `exercises.md` and `solutions.md` files are written for the student. Exercises are
meant to be handed over as they are, and the solutions are written so a student can
read them after attempting the work and understand not just what the answer was but
why. Nothing in them addresses you in the third person.

The one thing still worth holding back is the "Goal for the session" paragraph at the
top of each `lesson.md`. Ask them what they think the point of a session is before
telling them.

## How the folder is laid out

```
python-course/
  README.md              you are here
  instructor/            how to teach this, not what to teach
  cheat-sheets/          one-page references you can hand out or keep open
  00-setup/              one folder per unit, numbered in teaching order
  01-values-and-variables/
  ...
  09-modules-and-beyond/
```

The cheat sheets are meant to be printed or kept open in a second window. They are
written for the student, like the exercises and the solutions.

```
cheat-sheets/python-basics.md   every piece of syntax in the course, on one page
cheat-sheets/errors.md          each error type, what it means, what to check
cheat-sheets/glossary.md        every word the lessons use without explaining
```

Each unit folder has the same four things.

```
lesson.md        the concepts, in the order to teach them        for you
exercises.md     tiered problems, hand them over as they are     for the student
solutions.md     worked answers, with the reasoning              for the student
code/            small runnable files used during the session
```

## The units

| Unit | Title | What it lands | Prereq |
| --- | --- | --- | --- |
| 00 | Setup | They can run a .py file and see output | none |
| 01 | Values and variables | Storing things, printing them, doing maths | 00 |
| 02 | Text and input | Asking the user something and using the answer | 01 |
| 03 | Decisions | Code that chooses between paths | 02 |
| 04 | Repetition | Loops, the accumulator pattern, break and continue | 03 |
| 05 | Lists | Holding many values, iterating, sorting | 04 |
| 06 | Functions | Naming a block of work and reusing it | 05 |
| 07 | Dicts and tuples | Grouping related data, counting things | 06 |
| 08 | Files and errors | Saving to disk, surviving bad input | 07 |
| 09 | Modules and beyond | Using the standard library, where to go next | 08 |

Each unit is roughly one to two sessions of 60 to 90 minutes. Do not treat the unit
boundaries as day boundaries. A unit is done when they can do the core exercises without
help, not when you have finished talking.

## How to run a session

The shape that works, in order.

1. **Warm-up (5 to 10 minutes).** Open one of last session's exercises and have
   them explain what it does line by line, out loud. Not what it is supposed to
   do. What each line actually does.
2. **Motivate the unit (2 minutes).** Show the finished thing. A loop that prints
   a countdown, a function that converts temperatures. Something small that runs.
   They should want the output before they know how to make it.
3. **Teach one concept, then have them type it.** Never teach three concepts and
   then hand over the keyboard. Explain one thing, then they type it themselves
   and run it. Their typing, not yours, not copy paste.
4. **Break it on purpose.** Ask them to predict what happens if you remove the
   colon, or pass a string to `range()`. Predicting the error before seeing it is
   the single highest value activity in this whole curriculum.
5. **Exercises.** Warm-ups first, together. Core exercises on their own while you
   watch and stay quiet unless they ask. Stretch only if the core went fast.
6. **Close the loop (5 minutes).** Ask them to say, in their own words, what they
   learned, and to name one thing that still feels fuzzy. Write the fuzzy thing
   down and open the next session with it.

## Things that matter more than coverage

**Typing beats reading.** Copy-pasting code teaches almost nothing. Hands on the
keyboard is where syntax becomes memory. This slows early sessions down a lot and you
should let it.

**Errors are content.** Students who read tracebacks calmly will keep going alone after
the course ends. Students who fear them will stop. Spend real time on
`instructor/debugging-with-beginners.md`, and reward correct error-reading out loud when
it happens.

**Being stuck is normal and boring, not dramatic.** Normalise it. "Everyone spends most
of their time confused, that is what programming is" is a true sentence that removes a
lot of anxiety.

**Never leave a stretch exercise unexplained.** If they solve it, that is great. If they
do not, walk through it at the start of the next session anyway. An unexplained hard
problem teaches them that some code is magic.

**Do not chase completeness.** This curriculum deliberately leaves out classes,
comprehensions, decorators, generators, async and everything else that makes Python feel
intimidating. A student who is comfortable with functions, lists and dictionaries can
learn the rest on their own, and will, if the first ten units did not scare them off.

## What to read before your first session

1. `instructor/teaching-guide.md` — the philosophy behind the session shape above.
2. `instructor/common-mistakes.md` — so you recognise the classics on sight.
3. `instructor/debugging-with-beginners.md` — how to teach error reading.
4. `00-setup/lesson.md` — environment setup, and it has the most dependencies on
   what laptop they turned up with.

## A note about the tone of the lesson files

The `lesson.md` files are written so you can read them straight off the screen to your
student if you want, or paraphrase. They explain the why before the syntax whenever the
why is short. Where they say "ask them" or "wait", that is an actual instruction to you,
not decoration.

## If your student is not a native English speaker

This course was written for one, so the vocabulary work is already done. What that means
in practice.

Technical words are kept, because your student will need them to read documentation in
English later. But every one of them is glossed in brackets in a few plain words the
first time it appears, so `accumulator` arrives as "accumulator (a variable you add to
on every pass)". The glosses are the same wording everywhere in the course, on purpose,
so the student builds one map from one English word to one idea.

Words that are hard but not technical have been replaced with the everyday word. The
lessons say "glue together" and never "concatenate", "go through the items" rather than
"iterate", "on purpose" rather than "deliberately". The exceptions are noted in the
glossary, and Python's own error messages are one of them, since a `TypeError` really
does say "concatenate" and the student needs to recognise it.

`cheat-sheets/glossary.md` is the source of truth for the glosses. Read it yourself
before the first session, and add to it as you go. There is more on teaching across a
language barrier at the end of `instructor/teaching-guide.md`, including the one rule
that matters most, which is to use one word for one idea and never a synonym.

