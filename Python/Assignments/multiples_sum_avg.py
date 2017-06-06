# Assignment: Multiples, Sum, Average
title = "Assignment: Multiples, Sum, Average"
print title
print ""


# This assignment has several parts. All of your code should be in one file that is well commented to indicate what each block of code is doing and which problem you are solving. Don't forget to test your code as you go!
#






# Multiples
# Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.
#

print "Print odd numbers from 1 to 1000"
for num in range(1,1000,2):
    print num

print ""


# Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
#

print "Print multiples of 5 from 5 to 1,000,000"
for num in range(5,1000000,5):
    print num

print ""


# Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
#
print "Print sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]"

a = [1, 2, 5, 10, 255, 3]
total = 0
for num in a:
    total += num

print total
print ""

# Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

print "Print the average of the values in the list: a = [1, 2, 5, 10, 255, 3]"

a = [1, 2, 5, 10, 255, 3]
total = 0

for num in a:
    total += num
avg = total / len(a)

print avg
print ""
