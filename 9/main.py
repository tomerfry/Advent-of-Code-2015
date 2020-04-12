#! /usr/bin/python
import re

from node import Node


INSTRUCTION_PATTERN = '(?P<point_a>.+) to (?P<point_b>.+) = (?P<distance>\d+)'


def main():
	nodes = {}

	print('Day 9 Advent 2015')

	with open('sample.txt', 'r') as f:
		for instruction in f.readlines():
			parts = re.search(INSTRUCTION_PATTERN, instruction).groupdict()
			point_a = parts.get('point_a')
			point_b = parts.get('point_b')
			distance = int(parts.get('distance'))
			

if __name__ == '__main__':
	main()

"""

			if not point_a in nodes:
				nodes[point_a] = Node(point_a)

			if not point_b in nodes:
				nodes[point_b] = Node(point_b)

def connect_nodes(node_a, node_b, distance):
	node_a.insert_node(node_b, distance)
	node_b.insert_node(node_a, distance)
			distance = int(parts.get('distance'))
			connect_nodes(nodes.get(point_a), nodes.get(point_b), distance)
def travel_node(node, visited_nodes, nodes):
	visited_nodes.append(node.name)
	print(visited_nodes)
	if visited_nodes == nodes.keys():
		return

	not_visited_nodes = filter(lambda x: x not in visited_nodes, node.nodes)

	for n in not_visited_nodes:
		print('Can travel {} to {}'.format(node.nodes[n], n.name))
		travel_node(n, visited_nodes, nodes)
"""