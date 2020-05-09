#! /usr/bin/python3
import re
import itertools

from ingredient import Ingredient
from recipe import Recipe


INPUT_PATTERN = '(?P<name>.+?): capacity (?P<capacity>-?\d+?), durability (?P<durability>-?\d+?), flavor (?P<flavor>-?\d+?), texture (?P<texture>-?\d+?), calories (?P<calories>-?\d+?)'
MAX_SPOONS = 100
CALORIES = 500

def main():
	print('Advent of Code 2015')

	highest_score = 0

	with open('input.txt', 'r') as f:
		ingredients = parse_ingredients(f.readlines())

	for perm in itertools.permutations(range(1, MAX_SPOONS), len(ingredients)):
		if sum(perm) == MAX_SPOONS:
			new_recipe = Recipe(ingredients, perm)
			score = new_recipe.get_score()
			calorie_count = new_recipe.get_calories()

			if calorie_count == CALORIES:
				if highest_score < score:
					print('recipe score: {}, calorie count: {}'.format(score, calorie_count))
					highest_score = score


	print(highest_score)
			

def parse_ingredients(content_lines):
	ingredients = []
	pattern = re.compile(INPUT_PATTERN)

	for line in content_lines:
		values = pattern.match(line).groupdict()
		
		for key in values:
			try:
				values[key] = int(values[key])
			except ValueError:
				continue

		ingredients.append(Ingredient(**values))

	return ingredients

if __name__ == '__main__':
	main()