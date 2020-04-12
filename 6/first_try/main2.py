#! /usr/bin/python
import re

TOGGLE_REGEX = 'toggle (?P<start_x>\d+?),(?P<start_y>\d+?) through (?P<end_x>\d+?),(?P<end_y>\d+?)'
TURN_REGEX = 'turn (?P<state>(on|off)) (?P<start_x>\d+?),(?P<start_y>\d+?) through (?P<end_x>\d+?),(?P<end_y>\d+?)'


def get_instructions(file_name):
	with open(file_name) as input_file:
		content = input_file.readlines()
	return content


def handle_instruction(instruction):
	res = re.search(TURN_REGEX, instruction)
	brightness = 0
	if res:
		# print(res.groupdict())
		brightness = handle_turn_instruction(**res.groupdict())


	else:
		res = re.search(TOGGLE_REGEX, instruction)
		brightness = handle_toggle_instruction(**res.groupdict())

	return brightness

def handle_turn_instruction(state, start_x, start_y, end_x, end_y):
	start_x = int(start_x)
	start_y = int(start_y)
	end_x = int(end_x)
	end_y = int(end_y)

	width = end_x - start_x
	if width < 0:
		width = width * -1
	
	height = end_y - start_y
	if height < 0:
		height = height * -1

	sum = 0
	if state == 'on':
		sum += width * height
	if state == 'off':
		sum += -1 * width * height
	return sum


def handle_toggle_instruction(start_x, start_y, end_x, end_y):
	start_x = int(start_x)
	start_y = int(start_y)
	end_x = int(end_x)
	end_y = int(end_y)

	width = end_x - start_x
	if width < 0:
		width = width * -1
	
	height = end_y - start_y
	if height < 0:
		height = height * -1
	
	sum = 2 * width * height
	return sum


def main():
	print('Day 6 Advent 2015')
	instructions = get_instructions('input.txt')
	brightness = 0
	for instruction in instructions:
		brightness += handle_instruction(instruction)
	
	print(brightness)


if __name__ == '__main__':
	main()