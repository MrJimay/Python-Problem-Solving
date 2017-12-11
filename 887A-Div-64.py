#!/usr/bin/python

# Solution to problem 887A in codeforces

input = raw_input()

first_one_found = False
zero_count = 0
for letter in str(input):
    if not first_one_found and letter == "1":
        first_one_found = True
        
    if first_one_found and letter == "0":
        zero_count += 1

if zero_count >= 6:
    print "yes"
else:
    print "no"