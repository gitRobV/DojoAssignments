# Assignment: Fun with Functions
title = "Assignment: Fun with Functions"
print title
print ""

# Create a series of functions based on the below descriptions.


# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

def odd_even():
    for i in range(2001):
        if i % 2 == 0:
            print "Number is " + str(i) + ". This is an even number."
        else:
            print "Number is " + str(i) + ". This is an odd number."

odd_even()


# Multiply:
# Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

def multiply(list, num):
    new_list = []
    for item in list:
        new_list.append(item * num)
    return new_list

a = [2,4,10,16]

new_list = multiply(a, 5)

print new_list


# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the number of 1's as the number in the original list. Here's an example:

def layered_multiples(list):
    processed_list = []
    for item in list:
        new_item_list = []
        while item > 0:
            new_item_list.append(1)
            item -= 1
        processed_list.append(new_item_list)
    return processed_list

x = layered_multiples(multiply([2,4,10,16],3))

print x
