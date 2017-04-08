#!/usr/bin/python

# Solution to problem 236A in codeforces

username = ''.join(set(raw_input()))

if len(username) % 2 == 0:
    print "CHAT WITH HER!"
else:
    print "IGNORE HIM!"