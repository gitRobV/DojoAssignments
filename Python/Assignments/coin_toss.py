# Assignment: Coin Tosses
title = "Assignment: Coin Tosses"
print title
print ""

# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

import random

def coin_toss(num):
    attempts = num
    count = 1
    head_count = 0
    tail_count = 0

    while count <= num:
        toss = random.randint(1,2)
        if toss == 1:
            head_count += 1
            print "Attempt #" + str(count) + ": Throwing a coin... It's a Head! ... Got " + str(head_count) + " head(s) so far and " + str(tail_count) + " tail(s) so far"
        elif toss == 2:
            tail_count += 1
            print "Attempt #" + str(count) + ": Throwing a coin... It's a Tail! ... Got " + str(head_count) + " head(s) so far and " + str(tail_count) + " tail(s) so far"
        count += 1

coin_toss(5000)
