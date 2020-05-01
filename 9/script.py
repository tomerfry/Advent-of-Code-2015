#! /usr/bin/python3
import itertools
import re

PATTERN = '^(?P<a>.+) to (?P<b>.+) = (?P<dist>\d+?)$'


def calc_dist(mappings, road):
	dist = 0

	for index in range(len(road) - 1):
		dist += mappings[(road[index], road[index+1])]
	return dist


def main():
	print('Advent-of-Code 2015')

	with open('input.txt', 'r') as f:
		locations = set()
		mappings = {}

		for line in f:
			match = re.search(PATTERN, line)
			record = match.groupdict()
			locations.add(record['a'])
			locations.add(record['b'])
			mappings[(record['a'], record['b'])] = int(record['dist'])
			mappings[(record['b'], record['a'])] = int(record['dist'])

	smallest_dist = 1000
	biggest_dist = 0

	for perm in itertools.permutations(locations, len(locations)):
		dist = calc_dist(mappings, perm)
		if smallest_dist >= dist:
			smallest_dist = dist

		if biggest_dist < dist:
			biggest_dist = dist

	print(smallest_dist, biggest_dist)





if __name__ == '__main__':
	main()