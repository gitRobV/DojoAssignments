# Assignment: Find Characters
title = "Assignment: Find Characters"
print title
print ""


# Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'y'

new_list = []

for word in word_list:
    for letter in word:
        if char == letter:
            new_list.append(word)
            break

print new_list
