#! /usr/bin/python3
import re

from reindeer import Reindeer

COMPETITION_DURATION = 2503
INPUT_PATTERN = '(?P<name>.+?) can fly (?P<speed>\d+?) km/s for (?P<fly_duration>\d+?) seconds, but then must rest for (?P<rest_duration>\d+?) seconds\.'

def main():
	print('Advent of Code 2015')
	reindeers = []
	results = {}

	with open('input.txt') as f:
		reindeers = parse_input(f.readlines())

	for reindeer in reindeers:
		results[reindeer.get_name()] = reindeer.fly_for(COMPETITION_DURATION)

	print(results)
	print('Winner is with distance {}'.format(max(results.values())))


def parse_input(content_lines):
	reindeers = []
	pattern = re.compile(INPUT_PATTERN)

	for line in content_lines:
		values = pattern.match(line).groupdict()
		name = values['name']
		speed = int(values['speed'])
		fly_duration = int(values['fly_duration'])
		rest_duration = int(values['rest_duration'])

		reindeers.append(Reindeer(name, speed, fly_duration, rest_duration))

	return reindeers


if __name__ == '__main__':
	main()