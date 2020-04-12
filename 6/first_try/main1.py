#! /usr/bin/python
import re
from time import sleep
from PIL import Image
"""
class Instruction(object):
	def __init__(self, instruction):
		self.instruction = instruction
"""

TURN_REGEX = 'turn (.+?) '
# TOGGLE_REGEX = 'toggle (?P<start_x>),(?P<start_y>) through (?P<end_x>),(?P<end_y>)'
INDEX_REGEX = '(?P<start_x>\d+),(?P<start_y>\d+) through (?P<end_x>\d+),(?P<end_y>\d+)'

def get_instructions(file_name):
	with open(file_name) as input_file:
		content = input_file.readlines()
	return content

def handle_toggle(img, start_x, start_y, end_x, end_y):
	x = start_x
	y = start_y
	
	for i in range(start_x, end_x + 1):
		for j in range(start_y, end_y + 1):
			if img[i, j] == (0, 0, 0):
				img[i, j] = (255, 255, 255, 255)
			else:
				img[i, j] = (0, 0, 0, 255)


def handle_turn(img, start_x, start_y, end_x, end_y, value):
	x = start_x
	y = start_y

	for i in range(start_x, end_x + 1):
		for j in range(start_y, end_y + 1):
			#grid[i][j] = value
			if value == 1:
				img[i, j] = (255, 255, 255, 255)
			else:
				img[i, j] = (0, 0, 0, 255)

def digest_instruction(instruction, img):
	indexes = re.search(INDEX_REGEX, instruction).groupdict()

	start_x = int(indexes.get('start_x'))
	start_y = int(indexes.get('start_y'))
	end_x = int(indexes.get('end_x'))
	end_y = int(indexes.get('end_y'))

	if instruction.split()[0] == 'turn':
		result = re.findall(TURN_REGEX, instruction)
		if result.pop() == 'on':
			value = 1
		else:
			value = 0
		handle_turn(img, start_x, start_y, end_x, end_y, value)
	else:
		handle_toggle(img, start_x, start_y, end_x, end_y)
		# result = re.search(TOGGLE_REGEX, instruction).groupdict() 

def count_lights(img):
	count = 0

	for i in range(1000):
		for j in range(1000):
			if img[i, j] == (255, 255, 255):
				count += 1
	return count

def main():
	instructions = get_instructions('input.txt')
	img = Image.new('RGB', (1000, 1000), (0, 0, 0, 255))
	img_pixels = img.load()

	for instruction in instructions:
		digest_instruction(instruction, img_pixels)
		print('saved image - ' + instruction)
		
	print(count_lights(img_pixels))
	img.save('result.png')
	"""
	save_img(img, grid)

def save_img(img, grid):
	for i in range(1000):
		for j in range(1000):
			if grid[i][j] == 1:
				img.putpixel((i, j), (255, 255, 255, 255))
			else:
				img.putpixel((i, j), (0, 0, 0, 255))

	img.save('result.png')
	"""
if __name__ == '__main__':
	main()