# Assignment: Making Dictionaries
title = "Assignment: Making Dictionaries"
print title
print ""


# Create a function that takes in two lists and creates a single dictionary where the first list contains keys and the second values. Assume the lists will be of equal length.
#
# Your first function will take in two lists containing some strings. Here are two example lists:

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    key_list = list1
    value_list = list2
    if len(list2) > len(list1):
        key_list = list2
        value_list = list1

    for item in range(len(key_list)):
        if item >= len(value_list):
            new_dict[key_list[item]] = None
        else:
            new_dict[key_list[item]] = value_list[item]

    return new_dict

print make_dict(name,favorite_animal)
