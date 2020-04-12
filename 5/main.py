#! /usr/bin/python
import re

def main():
    print('Day 5 Advent 2015')
    nice_amount = 0

    with open('input.txt', 'r') as input_file:
        lines = input_file.readlines()

    #lines = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy', 'xyxy']

    for line in lines:
        line = line.strip()

        print(line)

        pattern = '(..).*?\\1'
        if not re.search(pattern, line):
            print('first')
            continue

        pattern = '(.).\\1'        
        if not re.search(pattern, line):
            print('Second')
            continue


        #pattern = '[aeiou]'
        #if len(re.findall(pattern, line)) < 3:
        #    print('has less vowls', re.findall(pattern, line))
        #    continue

        #if ('ab' in line) or ('cd' in line) or ('pq' in line) or ('xy' in line):
        #    print('has invalid string.')
        #    continue

        #pattern = '(.)\\1'
        #if not re.findall(pattern, line):
        #    print('Doesn\'t have duplicate.')
        #    continue

        nice_amount += 1

    print(nice_amount)


if __name__ == '__main__':
    main()