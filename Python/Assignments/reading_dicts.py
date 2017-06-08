# Assignment: Making and Reading from Dictionaries
title = "Assignment: Making and Reading from Dictionaries"
print title
print ""


# Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.
# Write a function that will print something like the following as it executes:

robert = {'name': 'Robert', 'age': '37', 'country of birth': 'USA', 'favorite language':'python'}

def parse_person(person):
    for prop in person:
        print "my " + prop + " is " + person[prop]

parse_person(robert)
