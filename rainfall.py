#!/usr/bin/python

# Given a list of heights (integers) of buildings
# Imagine there is rainfall onto the buildings
# How much rain will be captured? 
# E.g. if the heights are 919, there will be an area of 8 rain captured
# since the two buildings with height 9 will trap all the rain landing on the building with height 1
# E.g. if heights are 1234, there will be an area of 0 rain captured
# since the rain will just flow down into the ground, 
# as there are no two buildings tall enough surrounding shorter buildings to catch the rainfall

numbers = list(raw_input())

area = 0
temp_area = 0
second_temp_area = 0
tallest = -1
second_tallest = -1
buildings_since_last_second_tallest = 0

for num in numbers:
	num = int(num)
	if num >= tallest:
		area += temp_area
		temp_area = 0
		second_temp_area = 0
		buildings_since_last_second_tallest = 0
		second_tallest = -1
		tallest = num
	elif num >= second_tallest and second_tallest != -1:
		second_temp_area += (num - second_tallest) * buildings_since_last_second_tallest
		buildings_since_last_second_tallest = 1
		second_tallest = num
		temp_area += tallest - num
	else:
		if second_tallest == -1:
			second_tallest = num
			buildings_since_last_second_tallest = 1
		else:
			buildings_since_last_second_tallest += 1
		temp_area += tallest - num
area += second_temp_area

print area