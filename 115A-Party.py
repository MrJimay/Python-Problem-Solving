#!/usr/bin/python

# Solution to problem 115A in codeforces

total = input()
employees = []

for i in range(total):
    employees.append(input())

longest_chain = 0
for i in range(total):
    curr = employees[i]
    count = 1
    while curr != -1:
        count += 1
        curr = employees[curr - 1]
    if count >= longest_chain:
        longest_chain = count

print longest_chain