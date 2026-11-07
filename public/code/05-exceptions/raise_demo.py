# Unit 05 — Raising your own errors
# Run this with the Run button in your editor.

# ---------------------------------------------------------------
# 1. raise on its own. Uncomment the line below and run the file.
#    The program stops with a traceback, exactly as if Python had
#    found the problem itself.

# raise ValueError("age cannot be negative")

# ---------------------------------------------------------------
# 2. raise inside the validation loop.
#    int() refuses "abc" by itself. It does not refuse -5 or 999,
#    because those are real whole numbers. They are just not real
#    ages. raise lets your program refuse them too, and the same
#    except catches both kinds of problem.

while True:
    text = input("How old are you? ")
    try:
        age = int(text)
        if age < 0:
            raise ValueError("age cannot be negative")
        if age > 130:
            raise ValueError("nobody has lived that long")
        break
    except ValueError as error:
        print(f"Not accepted: {error}")

print(f"In ten years you will be {age + 10}.")
print()

# Try abc, -5, 999 and then 30. For abc the message is Python's own,
# which is written for programmers. For -5 and 999 it is yours.

# ---------------------------------------------------------------
# 3. Check first, or try?
#    .isdigit() says True only when every character is a digit.
#    int() is more forgiving. It allows spaces around the number
#    and a minus sign in front.

for text in ["42", " 42 ", "-5", "4.5", "", "abc"]:
    try:
        int(text)
        works = True
    except ValueError:
        works = False
    print(f"{repr(text):7} isdigit: {str(text.isdigit()):6} int works: {works}")

# Neither one is wrong. Checking first is fine when the check is
# simple and says exactly what you want. try is the usual Python
# way, because it asks int() itself, so it can never disagree
# with int().
