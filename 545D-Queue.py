#!/usr/bin/python

# Solution to problem 545D in codeforces

n = input()
patience = map(int, raw_input().split())
patience.sort()
curr_time_waited = 0
answer = 0

for i in range(len(patience)):
    if patience[i] >= curr_time_waited:
        answer += 1
        curr_time_waited += patience[i]

print answer