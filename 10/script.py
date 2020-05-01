#! /usr/bin/python3

def main():
	print('Advent-of-Code 2015')

	num_seq = input('insert number sequence: ')
	for i in range(50):
		num_seq = seq_creator(num_seq)
	
	print(len(num_seq))

def seq_creator(num_seq):
	curr_num = num_seq[0]
	counter = 1
	new_seq = ''

	for num in num_seq[1:]:
		if curr_num != num:
			new_seq += str(counter)
			new_seq += str(curr_num)
			curr_num = num
			counter = 1
		else:
			counter += 1

	new_seq += str(counter)
	new_seq += str(curr_num)

	return new_seq



if __name__ == '__main__':
	main()