#! /usr/bin/python3
import re

from sample import Sample


SAMPLE_PATTERN = '^Sue (\d+): (.+)$'


def main():
	print('Advent of Code 2015')

	known_sample = Sample(children=3,cats=7,samoyeds=2,pomeranians=3,\
		akitas=0,vizslas=0,goldfish=5,trees=3,cars=2,perfumes=1)

	with open('input.txt', 'r') as f:
		samples = parse_samples(f)
	
	for sample in samples:
		if sample == known_sample:
			print('Aunt Sue number {} sent the gift.'.format(sample.sample_id))


def parse_samples(samples_file):
	samples = []

	for line in samples_file:
		sample_entries = {}
		sample_id, content = re.match(SAMPLE_PATTERN, line).groups()
		sample_entries['sample_id'] = sample_id

		for item in content.split(','):
			key, string_value = item.strip().split(': ')
			value = int(string_value)
			sample_entries[key] = value

		samples.append(Sample(**sample_entries))
	
	return samples





if __name__ == '__main__':
	main()