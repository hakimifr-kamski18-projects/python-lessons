# Unit 02 — a small conversation
# Run this file with:  python3 conversation.py

# Notice the .strip() on the name. Without it, a stray trailing space
# follows the name around and causes confusing bugs later.

name = input("What is your name? ").strip()
birth_year = int(input("What year were you born? "))

age = 2026 - birth_year

print()
print(f"Hello {name.title()}!")
print(f"You will turn {age} this year.")

# ---------------------------------------------------------------
# Now extend this yourself, one piece at a time.

# 1. Ask for a favourite colour and include it in the output.
#    Is that answer a number or text? Which one do you need?

# 2. Ask for two numbers and print their sum.
#    Both answers need converting. To what?

# 3. Ask for the user's height in metres, like 1.75.
#    Would int() work here? Try it and find out.

# 4. Ask for a city and a country and print them as "City, Country",
#    with the city in title case and the country in capitals.
