#!/usr/bin/python

# Solution to problem 268B in codeforces

n = input()
found = 0
presses = 0
while n > 1:
    presses += (n - 1) * (found + 1)
    found += 1
    n -= 1
presses += found + 1
print presses