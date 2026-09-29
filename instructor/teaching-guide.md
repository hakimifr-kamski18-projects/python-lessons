# Teaching guide

This file is about method. The lesson files are about content. Read this once before you
start and skim it again before each session until the rhythm is automatic.

## The one rule that matters

Every session must end with your student having written code that runs. Not code you
wrote, not code they read, not code they understood. Code they typed, that produced
output they saw, ideally output they did not expect at first.

If a session is running long and you have to cut something, cut the explanation and keep
the typing.

## The predict-run-inspect loop

This is the engine of the whole curriculum. Use it constantly.

1. **Predict.** Show a few lines of code and ask what they think will happen.
   Write their answer down, in words, before running it.
2. **Run.** Actually run it. Then look at the output together.
3. **Inspect.** If the prediction was right, say why. If it was wrong, that is
   better, and you should say so. Work out together where the mental model
   diverged.

The predicting step is where the learning happens. Resist the urge to skip it because
the answer is obvious to you. It is not obvious to them, and their wrong prediction is
more informative to you than ten correct ones.

A useful variant once they are comfortable. Give them code with a deliberate mistake and
ask them to find it before running. They will run it anyway, which is fine, the point is
that they now have a hypothesis to check.

## Explain the why, but keep it short

Beginners can absorb one sentence of motivation per concept. Use it, then move to
syntax. Examples of adequate motivation.

- Variables, "so you can use a value later without retyping it".
- Loops, "so you do not have to write the same line twenty times".
- Functions, "so you can name a piece of work and stop thinking about how it
  works inside".
- Dictionaries, "so you can look something up by name instead of by position".

Then stop talking and let them type the syntax. A five minute lecture on why functions
are good is five minutes they could have spent getting a `TypeError` from forgetting to
return.

## Type it, do not paste it

Copy-pasting code skips the part where the fingers learn the syntax. Beginners who paste
for the first three sessions will still be unable to write a `for` loop from scratch in
the fourth. Slow down.

Small caveats. Let them paste long strings of text they need as data, and let them copy
a one-character fix you point out, that is fine. What matters is that they are producing
structure themselves.

## Keyboard skills are part of the lesson

Absolute beginners lose real time to things you have forgotten were hard.

- Finding the colon key, the underscore, and the parentheses.
- The difference between a straight quote `"` and a curly quote `"` that arrives
  when they type in a chat app first.
- Tab versus space, and why "consistent indentation" means something.
- Copying a file path versus typing it.

Budget a few minutes in the first two sessions for pure typing trouble. It is not a
waste.

## Indentation, taught early and gently

Python uses indentation to mean structure, which is unusual among languages and
surprising to beginners. Do not sell it as a quirk. Sell it as Python saying out loud
what other languages only imply with braces.

Teach it early, in unit 01, with a two line example, even though nothing needs it until
`if`. Then when `if` arrives in unit 03, it is already familiar.

How to teach it in one move. Show this.

```python
print("one")
print("two")
```

Then show this and ask what is different.

```python
print("one")
    print("two")
```

Then run it and read the `IndentationError` together. Do not explain the rule first. Let
the error teach it, then you name it.

## Reading errors out loud

Make this a ritual in every single session from unit 00 onwards.

Every time code fails, before doing anything else, ask them to read the last line of the
red text out loud. Then the second to last line, which says where. Then the `^` marker
if there is one, which points at the exact column.

You are building a habit. A student who automatically looks at the bottom of the
traceback will debug independently. A student who looks at the top, gets overwhelmed,
and asks you will not.

Full method in `debugging-with-beginners.md`.

## Stay quiet during core exercises

This is the hardest instruction in this document. When they are working on the core
exercises, sit on your hands. If they go quiet and type slowly, that is thinking, not
failing. Intervene when they ask, when they have been stuck in an identical way for
several minutes, or when they are about to get frustrated past the useful point.

When you do intervene, do not take the keyboard. Ask a question instead.

- "What is in that variable right now? How could you check?"
- "What did the error say the last time this happened?"
- "Read me the line that failed. Now read the one before it."
- "What is the smallest change that would tell you something?"

## Debugging is a taught skill, not a personality trait

Students arrive believing that some people can code and some cannot, and that errors are
evidence of the second kind. Undo that belief explicitly, out loud, early, and then
repeatedly, because it comes back.

Useful phrasings.

- "The computer did exactly what you told it. We have to find out which
  instruction you gave that you did not mean."
- "This error is not a judgement, it is a message. Let us read it."
- "Every programmer, every day, sees this exact screen. The skill is the reading,
  not the avoiding."

## Pair them up if you have more than one student

With two or more students, use driver and navigator. The driver has the keyboard and
types. The navigator reads ahead, says what should happen next, and is forbidden from
touching the keyboard. Swap every ten to fifteen minutes.

Two rules that make this work.

- The navigator explains what to type, in words, so the driver can type it. If
  the navigator has to grab the keyboard, the handoff failed.
- Debugging is a navigator job. The driver reads the error aloud, the navigator
  decides what it means.

This doubles the value of exercises, because the navigator is practising the harder
skill.

## Spaced repetition, done cheaply

Start every session with five minutes on something from a previous unit. Three good
formats.

- **Explain it.** Open an old exercise and have them narrate it line by line.
- **Break it.** Paste in working code with one thing changed and ask what happens.
- **Rebuild it.** "Write, from scratch, the code that asks for a number and
  prints its double." Nothing new, purely retrieval.

If they cannot do the retrieval one, that is your signal. Spend the session
consolidating instead of moving forward. Going slower here is faster overall.

## What "done" looks like for a unit

A unit is done when they can do the core exercises with the reference sheets closed,
unaided, and can explain their solution out loud. Finishing the lesson file is not the
bar. Hearing yourself explain something is a very different activity from recognising it
on a page, and only the first one counts.

## Signals that you are moving too fast

Watch for these. Any of them means consolidate before adding new material.

- They can follow along but freeze when the exercise is slightly different from
  the example.
- They reach for their notes for `print` and variable assignment.
- They describe a loop as "it repeats things" but cannot say what repeats or how
  many times.
- They get the right answer and cannot say how.
- They start guessing at syntax rather than referring to something.

Guessing at syntax is the loudest one. It means the patterns have not settled.

## Signals that you are moving too slow

Less common, but it happens.

- They are visibly bored, finishing exercises before you finish explaining.
- They are inventing their own extensions to exercises unprompted.
- They ask "but what if I wanted to..." questions.

If you see this, skip the remaining warm-ups, hand over the stretch exercises, and jump
a unit ahead. There is nothing sacred about the order. Units 06 and 07 can swap, and
unit 05's sorting material can move to the end if lists click fast.

## A word on not teaching things

Sometimes the honest answer to a beginner's question is "that is real, and it is true,
and you should not worry about it for now". Say that, rather than opening a door you are
not ready to walk through.

Common examples, and the short version to give.

- "Why not use `is` for comparing numbers?" — "Use `==`. `is` asks a different and
  weirder question. I will show you later."
- "What is a class?" — "A way to invent your own kind of thing, like a string but
  custom. It is unit ten, and it will make much more sense once functions feel
  easy."
- "Can I do this in one line?" — "Probably. Shorter code is not automatically
  better. Write it clearly first, always."
- "Should I use tabs?" — "Four spaces. Always. Never mix. Let the editor insert
  them."

Write the deferred questions down somewhere visible. Coming back to them at the end of
the course is satisfying, and it models that "not yet" is different from "no".

## When English is not the student's first language

This course was written for a student who is not a native English speaker, and it
assumes you may not be one either. That changes a few things.

**Give every new technical word a short plain gloss the first time it appears.** Not a
definition, a gloss. "An accumulator, which just means a variable you keep adding to."
Say it, then use the English word from then on. The point is not to avoid the word, it
is to make sure the word is attached to something.

**One word per idea, all the way through.** The temptation when teaching is to vary your
language, so you say "argument", then "value", then "thing you pass in". Do not. A
student working in a second language is building a map from one English word to one
idea, and synonyms break that map. Use "argument" every single time.

This applies to the course's own wording too. The lessons say "glue together" and never
"concatenate", "go through the items" and never "iterate", "on purpose" and never
"deliberately". Python's own error messages will use the harder word, so mention both
once when the error appears.

**`cheat-sheets/glossary.md` is the canonical list.** If you need a word glossed, take
the wording from there so it is the same in every session. Add to it as you go, and give
the student permission to write in it.

**Avoid idioms and phrasal verbs where a plain verb works.** "This will bite you" is
harder than "this will cause problems for you". "Sit on your hands" is harder than "do
not help". The course files have been cleaned of the worst of these, and you should keep
an ear out for the ones you say yourself.

Some need a short note about which are worth replacing. This is not about removing
flavour from your speech, and a few ordinary phrasal verbs are fine because the student
will hear them constantly from everyone. The ones to avoid are the ones where the
meaning is not guessable from the words.

- Worth replacing. "sit on your hands", "the penny drops", "in the wild", "out of
  the blue", "off the top of my head", "under the hood".
- Fine to keep. "run the program", "look up", "go wrong", "break it", "work out".

**Write the hard word on the board anyway.** Give the gloss out loud, then write the
real English word somewhere visible, under the technical word's own heading. In two
weeks they need to read documentation in English, and the documentation will not use the
gloss.

**Do not slow down the technical content to compensate.** A student who can follow loops
but not the word "accumulator" needs one sentence, not a simpler course. The vocabulary
and the material are separate problems, and mixing them up makes the course patronising.

**Watch for a silent stop.** A student who does not understand a word often says
nothing, because the question feels too small to ask. Ask directly every session. "Which
word from today would you not want to explain to someone else?" is a good way to ask,
because it gives them a reason to name one.

