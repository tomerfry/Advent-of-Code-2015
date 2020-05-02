#! /usr/bin/python3
import string
import re


GIVEN_INPUT = 'vzbxkghb'
SECOND_GIVEN_INPUT = 'vzbxxyzz'

ALPHABET = string.ascii_lowercase
CHR_OFFSET = ord('a')

NON_OVERLAPPING_PAIRS_PATTERN = '(.)\\1.*(.)\\2'


def main():
	print('Advent of Code 2015')

	num = alphabse_2_dec(SECOND_GIVEN_INPUT)

	while True:
		num += 1
		if first_req(dec_2_alphabase(num)):
			if second_req(dec_2_alphabase(num)):
				if third_req(dec_2_alphabase(num)):
					print(dec_2_alphabase(num))
					break


def first_req(expr):
	"""
	First requirment: password must include 
	one increasing straight of at least three letters.
	"""
	for i in range(len(expr) - 3):
		a,b,c = expr[i:i+3]

		if ord(a) + 1 == ord(b) and ord(b) + 1 == ord(c):
			return True
	return False


def second_req(expr):
	"""
	Second requirment: Passwords may not contain 
	the letters i, o, or l
	"""
	return not (('i' in expr) or ('o' in expr) or ('l' in expr))


def third_req(expr):
	"""
	Third requirment: Passwords must contain at least two different, 
	non-overlapping pairs of letters
	"""
	res = re.findall(NON_OVERLAPPING_PAIRS_PATTERN, expr)
	return bool(res)


def alphabse_2_dec(expr):
	res = 0

	for i in expr:
		res *= len(ALPHABET)
		res += ord(i) - CHR_OFFSET

	return res


def dec_2_alphabase(dec):
	res = ''

	while dec > 0:
		res += ALPHABET[dec % len(ALPHABET)]
		dec = int(dec / len(ALPHABET))

	return res[::-1]


if __name__ == '__main__':
	main()