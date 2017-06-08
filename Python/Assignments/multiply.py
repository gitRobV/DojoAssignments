# Assignment: Assignment: Multiplication Table
title = "Assignment: Multiplication Table"
print title
print ""

# Create program that prints multiplication table in your console.
#
# Your table should look like the following example:
#
# x   1  2  3  4  5  6  7  8   9  10  11  12
# 1   1  2  3  4  5  6  7  8   9  10  11  12
# 2   2  4  6  8 10 12 14 16  18  20  22  24
# 3   3  6  9 12 15 18 21 24  27  30  33  36
# 4   4  8 12 16 20 24 28 32  36  40  44  48
# 5   5 10 15 20 25 30 35 40  45  50  55  60
# 6   6 12 18 24 30 36 42 48  54  60  66  72
# 7   7 14 21 28 35 42 49 56  63  70  77  84
# 8   8 16 24 32 40 48 56 64  72  80  88  96
# 9   9 18 27 36 45 54 63 72  81  90  99 108
# 10 10 20 30 40 50 60 70 80  90 100 110 120
# 11 11 22 33 44 55 66 77 88  99 110 121 132
# 12 12 24 36 48 60 72 84 96 108 120 132 144
# Copy
# What is the most efficient way to produce the above output?
#
# Hint: Don't worry about getting it perfectly spaced, just ensure all the values are properly output!

table_depth = 10

counter = 0

while counter <= table_depth:
    print_str = ""
    # add line number
    if counter == 0:
        print_str += "line"
    elif counter <= 9:
        print_str += str(counter) + "   "
    else:
        print_str += str(counter) + "  "
    # build print_str
    for line in range(1,table_depth + 1):
        if counter == 0:
            if line <= 8:
                print_str += " " + str(line) + " "
            else:
                print_str += "  " + str(line)
        elif line <= 8:
            if len(str(counter * line)) == 1:
                print_str += " " + str(counter * line) + " "
            else:
                print_str += str(counter * line) + " "
        elif line > 8:
            if len(str(counter * line)) == 1:
                print_str += "  " + str(counter * line) + " "
            elif len(str(counter * line)) == 2:
                print_str += " " + str(counter * line) + " "
            else:
                print_str += str(counter * line) + " "

        # add line multiplied by iteration counter



    counter += 1
    print print_str
