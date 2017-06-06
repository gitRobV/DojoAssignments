# Assignment: String and List Practice
title = "Assignment: String and List Practice"
print title
print ""

words = "It's thanksgiving day. It's my birthday,too!"

index_of_day = str(words.find('day'))

print 'The first instance of "day" is at index ' + index_of_day + ' of words string'

print words.replace('day', 'month')
print ""
print ""
# Min and Max
# Print the min and max values in a list like this one: x = [2,54,-2,7,12,98]. Your code should work for any list.

x = [2,54,-2,7,12,98]

min = min(x)
max = max(x)

print "The min value in list x is: " + str(min)
print "The Max value in list x is: " + str(max)
print ""
print ""

# First and Last
# Print the first and last values in a list like this one: x = ["hello",2,54,-2,7,12,98,"world"]. Now create a new list containing only the first and last values in the original list. Your code should work for any list.

x = ["hello",2,54,-2,7,12,98,"world"]

first_of_x = x[0]
last_of_x = x[len(x) - 1]

print "The first value in this list is " + str(first_of_x)
print "The last value in this list is " + str(last_of_x)
print ""
print ""

# New List
# Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = []
z = []

half = len(x)/2
counter = 0
while counter < half:
    popped = x.pop(0)
    y.append(popped)
    counter += 1

z.append(y)
z.extend(x)
print z
