# Assignment: Assignment: Multiplication Table
title = "Assignment: Optimal Primes"
print title
print ""

num_range = range(100000)

optimal_primes = [ 2, 3, 5, 7, 11, 13 ]
prime_count = 0
perfect_count = 0
non_count = 0

primes_list = []
perfect_sqr_list = []
non_prime_list = []

for num in num_range:
    if num in optimal_primes:
        # print "Prime"
        primes_list.append(num)
        prime_count += 1
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num % 11 != 0 and num % 13 != 0:
        # print "Prime"
        primes_list.append(num)
        prime_count += 1
    elif num**(.5) % 1 == 0:
        # print "Perfect Square"
        perfect_sqr_list.append(num)
        perfect_count += 1
    else:
        # print num
        non_prime_list.append(num)
        non_count += 1

print "The count of primes in this range: " + str(prime_count)
print primes_list

print "The count of perfect squares in this range: " + str(perfect_count)
print perfect_sqr_list

print "The total count of non prime numbers in this range: " + str(non_count)
