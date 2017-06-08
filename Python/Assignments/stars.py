# Assignment: Stars
title = "Assignment: Stars"
print title
print ""


# Write the following functions.
#
# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.

x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(star_list):

    for item in star_list:
        if isinstance(item, str):
            print item[0].lower() * len(item)
        else:
            print "*" * item

draw_stars(y)
