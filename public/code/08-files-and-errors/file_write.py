# Unit 08 — writing files
# Run this file from inside the code folder:
#     cd code
#     python3 file_write.py
#
# Then look at output.txt. Run it again, and look again.

# ---------------------------------------------------------------
# "w" means WRITE, and it WIPES the file.

with open("output.txt", "w") as file:
    file.write("Hello\n")
    file.write("Second line\n")

# Run this program twice. The file has TWO lines, not four.
# Opening a file in "w" mode empties it immediately.

# ---------------------------------------------------------------
# write() does NOT add a newline. print() does, write() does not.
# So "\n" has to be written out.
#
# Uncomment these two lines and look at output.txt. Everything ends
# up on one line.

# with open("output.txt", "w") as file:
#     file.write("one")
#     file.write("two")
#     file.write("three")

# ---------------------------------------------------------------
# Everything written has to be a STRING.
# Uncomment to see the TypeError.
#
# with open("output.txt", "w") as file:
#     file.write(42)

# The fix:
with open("numbers.txt", "w") as file:
    file.write(str(42) + "\n")

# ---------------------------------------------------------------
# "a" means APPEND. It adds to the end instead of wiping.

with open("log.txt", "a") as file:
    file.write("Something happened\n")

# Run this program several times and watch log.txt grow.
# Then change the "a" to a "w" and run it again. It stops growing.

# ---------------------------------------------------------------
# THE CLASSIC BUG. Opening the file INSIDE the loop.

# Uncomment this, run it, and look at numbers.txt. It contains only "5".

# for i in range(1, 6):
#     with open("numbers.txt", "w") as file:
#         file.write(f"{i}\n")

# The file is opened and wiped on every pass, so only the last write
# survives. The fix is to open the file ONCE, outside the loop:

with open("numbers.txt", "w") as file:
    for i in range(1, 6):
        file.write(f"{i}\n")

# ---------------------------------------------------------------
# THE THREE MODES
#
#   "r"   read      the file must exist
#   "w"   write     wipes the file, or creates it
#   "a"   append    adds to the end, or creates it
