#!/usr/bin/python

# Solution to problem 71A in codeforces

max_count = input()
count = 0
while count < max_count:
    string = raw_input()
    end = len(string)
    if (end>10):
        print string[0] + str(end-2) + string[end-1]
    else:
        print string
    count += 1