# Unit 09 — the main guard
# Run this with the Run button in your editor.
# Then import it from another file, or from the console:
# >>> import main_guard
#
# The message only appears when the file is RUN, not when it is IMPORTED.

def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def show_report(scores):
    print(f"Average: {average(scores):.1f}")


# ---------------------------------------------------------------
# THE GUARD

if __name__ == "__main__":
    show_report([88, 95, 72])

# How it works.
#
# When you RUN a file directly, Python sets a variable called __name__
# to the string "__main__".
#
# When a file is IMPORTED, __name__ is the name of the module instead.
#
# So the check is: "am I the file that was run?"
#
# ---------------------------------------------------------------
# WHY it is needed.
#
# Anything at the top level of a file, outside any function, runs when the
# file runs. It ALSO runs when the file is imported.
#
# So if my_tools.py has a print() at the bottom for testing, that print()
# fires every time anybody imports my_tools. Putting it inside the guard
# means it only fires when you run my_tools.py yourself.
#
# ---------------------------------------------------------------
# You do not need this yet. You will see it in every real Python file you
# open, so it is worth recognising.
#
# This is what a tidy version of my_tools.py looks like:

def main():
    print("Setting up my_tools...")
    scores = [88, 95, 72]
    print(f"Average of the test scores: {average(scores):.1f}")


if __name__ == "__main__":
    main()
