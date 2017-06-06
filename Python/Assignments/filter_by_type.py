# Assignment: Filter by Type
title = "Assignment: Filter by Type"
print title
print ""


# Write a program that, given some value, tests that value for its type. Here's what you should do for each type:
#

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

tests = [sI, mI, bI,eI,spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]

string = "string"
integer = 5
lists = ['this', 'is', 'list']

is_str = type(string)
is_int = type(integer)
is_list = type(lists)

for value in tests:
    # String
    # If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."
    #
    if isinstance(value, is_str):
        if len(value) < 50:
            print "Short Sentence."
        elif len(value) >= 50:
            print "Long Sentence."
    # Integer
    # If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"
    #
    elif isinstance(value, is_int):
        if value >= 100:
            print "That's a big number!"
        elif value < 100:
            print "That's a small number"
    # List
    # If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."
    #
    elif isinstance(value, is_list):
        if len(value) >= 10:
            print "Big List!"
        elif len(value) < 10:
            print "Short List"
    else:
        print "This is neither an integer, list or string."








# print tests
