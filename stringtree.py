#!/usr/bin/python

# Given a string of L's and R's
# Find the number of unique binary trees created
# If any of the L's and R's can be skipped
# E.g. LRLLR can be L, R, LR, LL, RL, RR, LRL, LRR, LLL, RLL, RLR, LLR, LRLL, RLLR, LLLR, LRLR, LRLLR
# So the solution for input LRLLR is 17

string = list(raw_input())

solutions = 0
lefts = 1
rights = 1

for char in string:
	if char == "L":
		solutions = solutions + lefts
		rights = rights + lefts
	if char == "R":
		solutions = solutions + rights
		lefts = rights + lefts

print solutions