#! /usr/bin/python3
import re

from reindeer import Reindeer

COMPETITION_DURATION = 2503
INPUT_PATTERN = '(?P<name>.+?) can fly (?P<speed>\d+?) km/s for (?P<fly_duration>\d+?) seconds, but then must rest for (?P<rest_duration>\d+?) seconds\.'

def main():
	print('Advent of Code 2015')
	reindeers = []

	with open('input.txt') as f:
		reindeers = parse_input(f.readlines())

	scores = compete(reindeers, COMPETITION_DURATION)

	print(scores)
	print('Winner is with score {}'.format(max(scores)))


def compete(reindeers, duration):
	while duration > 0:
		# A second passed.
		duration -= 1

		for reindeer in reindeers:
			reindeer.compete_one_second()

		reindeer = who_leads(reindeers)
		reindeer.grant_point()

	return [reindeer.get_points() for reindeer in reindeers]


def who_leads(reindeers):
	furthest_reindeer = reindeers[0]

	for reindeer in reindeers:
		if reindeer.get_distance() > furthest_reindeer.get_distance():
			furthest_reindeer = reindeer
	return furthest_reindeer


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