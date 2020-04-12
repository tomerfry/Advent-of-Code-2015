import re

from node import Node


class Map(object):

	MAP_LINE_PATTERN = '(?P<a>.+) to (?P<b>.+) = (?P<dist>\d+)'

	def __init__(self):
		self.nodes = []

	def create_map(self, input_file_name):
		with open(input_file_name, 'r') as f:
			lines = f.readlines()

		for line in lines:
			line_parts = re.search(self.MAP_LINE_PATTERN, line).groupdict()

			a = self.get_node(line_parts['a'])
			b = self.get_node(line_parts['b'])

			if not a:
				a = Node(line_parts['a'])
				self.nodes.append(a)
			if not b:
				b = Node(line_parts['b'])
				self.nodes.append(b)

			a.add_neighbor(b, int(line_parts['dist']))
			b.add_neighbor(a, int(line_parts['dist']))

	def get_node(self, node_name):
		for node in self.nodes:
			if node.name == node_name:
				return node
		return None

	def __str__(self):
		map_string = '\n\n'.join([str(node) for node in self.nodes])
		return map_string



"""
	def get_names(self):
		return [node.name for node in self.nodes]

	def travel_map(self, node, visited_nodes):

		if set(visited_nodes) == set(self.get_names()):
			return 0

		
	def travel_map(self):
		smallest_dist = 0

		for node in self.nodes:
			trip_dist = self.travel_from_node(node, [])
			if smallest_dist > trip_dist:
				smallest_dist = trip_dist

		return smallest_dist
	def travel_from_node(self, node, visited_nodes):
		if set(visited_nodes) == set(self.get_names()):
			return 0


		# dist_list = [self.travel_from_node(n, visited_nodes) for n in ]

		def travel_nodes(node, visited_nodes, all_nodes, dist):
	visited_nodes.append(node)

	if set(visited_nodes) == set(all_nodes):
		return dist

	smallest_dist = dist
	for n in node.neighbors:
		ndist = dist + node.neighbors[n]
		total_dist = travel_nodes(n, visited_nodes, all_nodes, ndist)
		if total_dist < smallest_dist:
			smallest_dist = total_dist

	return smallest_dist
"""