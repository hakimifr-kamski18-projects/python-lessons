# Unit 02 — strings as sequences
# Run this file with: python3 strings.py
# Predict each line before you run it.

word = "Python"
print(len(word))      # 6 characters

print()

# Positions start at ZERO. The first character is at position 0.

print(word[0])        # P
print(word[1])        # y
print(word[5])        # n
print(word[-1])       # n, counting backwards from the end
print(word[-2])       # o

print()

# Uncomment this to see the IndexError.
# print(word[6])

print()

# ---------------------------------------------------------------
# Slicing. Includes the start position, and stops BEFORE the end position.

print(word[0:3])      # Pyt positions 0, 1, 2 (three characters)
print(word[2:5])      # tho
print(word[:3])       # Pyt from the start
print(word[3:])       # hon to the end
print(word[1:1])      # (empty)
print(word[0:100])    # the whole thing, no error

# Going past the end of a SLICE is fine.
# Going past the end of an INDEX is an IndexError.

print()

# ---------------------------------------------------------------
# Strings cannot be changed in place. Uncomment to see the TypeError.

# word[0] = "J"

# You make a NEW string instead.

new_word = "J" + word[1:]
print(new_word)       # Jython
print(word)           # Python, untouched

print()

# Uncomment this to see the ValueError again.
# number = int(word)
