#! /usr/bin/python
import os

def calc_len(line_bytes):
	pass	

def newly_encode(line):
	line = line.replace('\\', '\\\\').replace('"', '\\"')
	newly_encode = '"{}"'.format(line)
	return newly_encode

def main():
	print('Day 8 Advent 2015')

	with open('input.txt', 'rb') as f:
		lines = f.readlines()
	sum_lines = 0

	for line in lines:
		line = line.strip()
		#eval_line = eval(line)
		newly_encoded = newly_encode(line)
		print(newly_encoded)

		sum_lines += len(newly_encoded) - len(line)

	print(sum_lines)

		



if __name__ == '__main__':
	main()