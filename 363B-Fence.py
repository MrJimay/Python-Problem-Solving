#!/usr/bin/python

# Solution to problem 363B in codeforces

line_one = map(int, raw_input().split())
width = line_one[1]
planks = map(int, raw_input().split())

curr = 0
answer = 1

for i in range(width):
    curr += planks[i]
    
min = curr

for i in range(len(planks) - width):
    j = i + width - 1
    curr -= planks[i]
    curr += planks[j + 1]
    if curr < min:
        min = curr
        answer = i + 2 # (i + 1) index + 1 to make it position

print answer