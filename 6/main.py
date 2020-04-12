#! /usr/bin/python
import re

INDEXES_REGEX = '(?P<start_x>\d+),(?P<start_y>\d+) through (?P<end_x>\d+),(?P<end_y>\d+)'
TURN_REGEX = 'turn (?P<state>(on|off))'

def get_instructions(filename):
	with open(filename, 'r') as f:
		return [line.strip() for line in f.readlines()]

def count_brightness(grid):
	brightness = 0
	for i in range(1000):
		for j in range(1000):
			brightness += grid[i, j]
	return brightness

def main():
	print('Day 6 Advent 2015')

	instructions = get_instructions('input.txt')
	grid = {}

	for i in range(1000):
		for j in range(1000):
			grid[i, j] = 0

	for instruction in instructions:
		indexes = re.search(INDEXES_REGEX, instruction).groupdict()
		start_x = int(indexes.get('start_x'))
		start_y = int(indexes.get('start_y'))
		end_x = int(indexes.get('end_x'))
		end_y = int(indexes.get('end_y'))

		print(start_x, start_y, end_x, end_y)

		if instruction.split()[0] == 'turn':
			state = instruction.split()[1]
			if state == 'on':
				for i in range(start_x, end_x + 1):
					for j in range(start_y, end_y + 1):
						grid[i, j] += 1
			else:
				for i in range(start_x, end_x + 1):
					for j in range(start_y, end_y + 1):
						if grid[i, j] > 0:
							grid[i, j] -= 1
		else:
			for i in range(start_x, end_x + 1):
				for j in range(start_y, end_y + 1):
					grid[i, j] += 2

	print(count_brightness(grid))

if __name__ == '__main__':
	main()