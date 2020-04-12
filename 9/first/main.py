#! /usr/bin/python

from map import Map


def main():
	print('Day 9 Advent 2015')
	m = Map()
	m.create_map('sample.txt')	

	print(m)

"""
	print(travel_nodes(m.nodes[0], [], 0))

def travel_nodes(node, visited_nodes, dist):
	visited_nodes.append(node)

	not_visited = filter(lambda n: n not in visited_nodes, node.neighbors)

	if not not_visited:
		return dist
	else:
		dist_list = sorted([travel_nodes(n, visited_nodes, node.neighbors[n]) for n in not_visited])
		return dist + dist_list[0]
	travel_nodes(m.nodes[0], [])
def travel_nodes(node, visited_nodes):
	visited_nodes.append(node)
	not_visited = filter(lambda n: n not in visited_nodes, node.neighbors)

	if not not_visited:
		return [0]
	else:
		return [travel_nodes(n, visited_nodes) for n in not_visited]

"""


if __name__ == '__main__':
	main()