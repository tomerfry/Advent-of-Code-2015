#! /usr/bin/python
import re

TOGGLE_REGEX = 'toggle (?P<start_x>\d+?),(?P<start_y>\d+?) through (?P<end_x>\d+?),(?P<end_y>\d+?)'
TURN_REGEX = 'turn (?P<state>(on|off)) (?P<start_x>\d+?),(?P<start_y>\d+?) through (?P<end_x>\d+?),(?P<end_y>\d+?)'

def get_instructions(file_name):
	with open(file_name) as input_file:
		content = input_file.readlines()
	return content

def handle_turn(grid, state, start_x, start_y, end_x, end_y):
	start_x = int(start_x)
	start_y = int(start_y)
	end_x = int(end_x)
	end_y = int(end_y)

	if start_y > end_y:
		y = end_y
		end_y = start_y
		start_y = y

	for i in range(start_x, end_x + 1):
		for j in range(start_y, end_y + 1):
			if state == 'on':
				grid[i, j] += 1
			else:
				grid[i, j] -= 1

def handle_toggle(grid, start_x, start_y, end_x, end_y):
	start_x = int(start_x)
	start_y = int(start_y)
	end_x = int(end_x)
	end_y = int(end_y)

	if start_y > end_y:
		y = end_y
		end_y = start_y
		start_y = y

	for i in range(start_x, end_x + 1):
		for j in range(start_y, end_y + 1):
			grid[i, j] += 2

def count_brightness(grid):
	sum_b = 0
	for i in range(1000):
		for j in range(1000):
			sum_b += grid[i, j]
	return sum_b

def handle_instruction(grid, instruction):
	res = re.search(TURN_REGEX, instruction)
	brightness = 0

	if not res:
		res = re.search(TOGGLE_REGEX, instruction)
	
	res = res.groupdict()
	start_x = int(res.get('start_x')) 
	start_y = int(res.get('start_y'))
	end_x = int(res.get('end_x'))
	end_y = int(res.get('end_y'))

	width = (end_x - start_x) + 1
	height = (end_y - start_y) + 1

	if width * height < 0:
		area = width * height * -1
	else:
		area = width * height

	if 'state' in res:
		if res.get('state') == 'on':
			brightness += area
		else:
			brightness -= area
	else:
		brightness += 2 * area

	return brightness

def main():
	print('Day 6 Advent 2015')
	instructions = get_instructions('input.txt')
	
	grid = {}

	for i in range(1000):
		for j in range(1000):
			grid[i,j] = 0

	b = 0
	for instruction in instructions:
		b += handle_instruction(grid, instruction)

	print(b)


if __name__ == '__main__':
	main()