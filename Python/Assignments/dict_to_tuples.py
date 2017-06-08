# Assignment: Dictionary in, tuples out
title = "Assignment: Dictionary in, tuples out"
print title
print ""

# Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:

# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict_to_tuples(dict):
    new_list = []

    for key,value in dict.items():
        new_list.append( (key,value) )

    return new_list

print dict_to_tuples(my_dict)



# #function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]
