# Unit 08 — saving structured data with json
# Run this file from inside the code folder:
# cd code
# python3 save_data.py
#
# Then open scores.json in a text editor and look at it.

import json

scores = {"Ada": 88, "Grace": 95}

# ---------------------------------------------------------------
# Writing a dictionary to a file

with open("scores.json", "w") as file:
    json.dump(scores, file)

# ---------------------------------------------------------------
# Reading it back

with open("scores.json") as file:
    loaded = json.load(file)

print(loaded)
print(type(loaded))

# The round trip works, and the TYPES survive. Numbers come back as
# numbers, not as the strings you would get from reading the file
# by hand and converting everything yourself.

print()

# ---------------------------------------------------------------
# A list of dictionaries, which is the shape from unit 07.
# indent=2 makes the file readable instead of one long line.

students = [
    {"name": "Ada", "score": 88},
    {"name": "Grace", "score": 95},
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

# Open students.json and compare it with scores.json.

print()

# ---------------------------------------------------------------
# This is useful for much more than saving data. It also means you can
# set up test data once, in a file, instead of retyping it every time
# you run a program.

# ---------------------------------------------------------------
# A WARNING. json.load on an empty file, or on a file that does not
# contain valid JSON, gives a JSONDecodeError.
# Uncomment this to see it.

# with open("output.txt") as file:
# json.load(file)

# JSONDecodeError is a kind of ValueError, so "except ValueError"
# catches it too (handles the error so the program does not stop). That is a
# slightly surprising detail worth knowing.

print()

# ---------------------------------------------------------------
# The pattern for loading, which handles the file not existing yet.
# The first run is the normal case, not an error.

def load_data(filename):
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except ValueError:
        print(f"{filename} is damaged, starting fresh")
        return {}

data = load_data("nothing_here_yet.json")
print(f"Loaded: {data}")
