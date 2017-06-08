# Assignment: Scores and Grades
title = "Assignment: Scores and Grades"
print title
print ""


# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:
#
# Score: 60 - 69; Grade - D Score: 70 - 79; Grade - C Score: 80 - 89; Grade - B Score: 90 - 100; Grade - A


import random

def generate_scores():
    generated_grades = [];
    count = 0
    while count < 10:
        generated_grades.append(random.randint(60,100))
        count += 1
        
    for grade in generated_grades:
        if grade >= 60 and grade <= 69:
            print "Score: " + str(grade) + "; Your grade is D"
        elif grade >= 70 and grade <= 79:
            print "Score: " + str(grade) + "; Your grade is C"
        elif grade >= 80 and grade <= 89:
            print "Score: " + str(grade) + "; Your grade is B"
        elif grade >= 90 and grade <= 100:
            print "Score: " + str(grade) + "; Your grade is A"

generate_scores()
