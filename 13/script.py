#! /usr/bin/python3
import itertools
import re

INPUT_PATTERN = '(?P<first_name>.+?) would (?P<operator>.+?) (?P<cost>.+?) happiness units by sitting next to (?P<second_name>.+?)\.'
OPERATORS = {'lose': -1, 'gain': 1}
SITTER_NAME = 'a'


def main():
    print('Advent of Code 2015')
    with open('input.txt', 'r') as f:
        mapping, name_list = parse_input(f.readlines())


    # Second stage for this level: Add a sitter.
    sitter_name = SITTER_NAME
    while sitter_name in name_list:
        sitter_name = input('Sitter name: ')
    
    for sitter in name_list:
        mapping[(sitter_name, sitter)] = 0
        mapping[(sitter, sitter_name)] = 0

    name_list.add(sitter_name)

    most_optimal = list(name_list)
    happiest = calc_happiness(most_optimal, mapping)

    for perm in itertools.permutations(name_list, len(name_list)):
        happiness = calc_happiness(perm, mapping)
        if happiness > happiest:
            most_optimal = perm
            happiest = happiness
    
    print(happiest)
    print(most_optimal) 
    

def parse_input(content_lines):
    pattern = re.compile(INPUT_PATTERN)
    mapping = {}
    name_list = set()

    for line in content_lines:
        values = pattern.match(line).groupdict()
        first = values['first_name']
        second = values['second_name']
        cost = OPERATORS[values['operator']] * int(values['cost'])
        mapping[(first, second)] = cost
        name_list.add(first)
        name_list.add(second)

    return mapping, name_list


def calc_happiness(sits, mapping):
    happiness = 0

    for i in range(len(sits)):
        happiness += mapping[(sits[i], sits[(i-1) % len(sits)])]
        happiness += mapping[(sits[i], sits[(i+1) % len(sits)])]
    
    return happiness



if __name__ == '__main__':
    main()