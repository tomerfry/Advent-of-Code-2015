#! /usr/bin/python

from instructions import InstructionsManager

def main():
	print('Dat 7 Advent 2015')
	
	im = InstructionsManager('input.txt')
	circuit = im.compile()
	print(circuit)

if __name__ == '__main__':
	main()