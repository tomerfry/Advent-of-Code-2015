#! /usr/bin/python3
import json

TEST_INPUT = '[1,2,3]'
TEST_INPUT1 = '{"a":2,"b":4}'
TEST_INPUT2 = '[[[3]]]'

def sum_container(container):
	if isinstance(container, int):
		return container
	elif isinstance(container, list):
		return sum([sum_container(s) for s in container])
	elif isinstance(container, dict):
		if 'red' not in container.values():
			return sum([sum_container(s) for s in container.values()])
		else:
			return 0
	else:
		return 0

def main():
	print('Advent of Code 2015')
	print(json.loads(TEST_INPUT))
	print(sum_container(json.loads(TEST_INPUT)))

	print(json.loads(TEST_INPUT1))
	print(sum_container(json.loads(TEST_INPUT1)))

	print(json.loads(TEST_INPUT2))
	print(sum_container(json.loads(TEST_INPUT2)))

	with open('input.json', 'r') as fp:
		print(sum_container(json.load(fp)))



if __name__ == '__main__':
	main()