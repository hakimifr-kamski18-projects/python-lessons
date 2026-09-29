# Unit 03 — grade calculator
# Run this with the Run button in your editor.

name = input("Name: ").strip().title()
score = int(input("Score out of 100: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"{name} scored {score}, which is a {grade}")

# Notice the pattern. Each branch sets the same variable, and the print()
# happens once at the end. That is usually tidier than printing inside
# every branch.

# ---------------------------------------------------------------
# Now extend this yourself, one piece at a time.

# 1. Print "Passed" unless the grade is F.

# 2. Print an extra line for an A, something encouraging.

# 3. Ask whether they attended every class, and only give a high grade
#    if they did. You will need "and".

# 4. Print a warning if the score is over 100.
#    Where does that check have to go in the chain, and why?

# 5. What happens if they type -5? What should happen?
