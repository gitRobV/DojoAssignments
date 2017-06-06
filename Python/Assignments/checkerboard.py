# Assignment: Checkerboard
title = "Assignment: Checkerboard"
print title
print ""

# Write a program that prints a 'checkerboard' pattern to the console.
#
# Your program should require no input and produce console output that looks like so:
#
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# Copy
# Each star or space represents a square. On a traditional checkerboard you'll see alternating squares of red or black. In our case we will alter

i = 0

pattern = "* * * * *"
while i <= 10:
    if i % 2 == 0:
        print pattern
    else:
        print " " + pattern
    i += 1
