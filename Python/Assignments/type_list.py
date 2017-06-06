# Assignment: Type List
title = "Assignment: Type List"
print title
print ""

# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
#
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the array contains. If it contains only one type, print that type, otherwise, print 'mixed'.
#

# Test Cases
# test = ['magical unicorns',19,'hello',98.98,'world']
test = [2,3,1,7,4,12]

# Initiate variables to print
total = 0
strings = ""

# Initiate Counts
int_count = 0
str_count = 0

# Test Type of value in List
for value in test:
    if isinstance(value, str):
        # add string to print variable
        strings += value
        # increment string count
        str_count += 1
    elif isinstance(value, int) or isinstance(value, float):
        # add int or float to running total
        total += value
        # increment integer count
        int_count += 1

if int_count == 0 and str_count != 0:
    print "list of " + str(str_count) + " Strings"
    print strings
elif str_count == 0 and int_count != 0:
    print "list of " + str(int_count) + " Integers"
    print total
elif str_count != 0 and int_count != 0:
    print "list of " + str(int_count) + " Integers and " + str(str_count) + " Strings"
    print total
    print strings
else:
    print "Something Went Way Wrong"
    print total
    print int_count
    print strings
    print str_count
