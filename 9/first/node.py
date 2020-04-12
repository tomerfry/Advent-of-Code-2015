class Node(object):
	def __init__(self, name):
		self.name = name
		self.neighbors = {}

	def add_neighbor(self, node, dist):
		self.neighbors[node] = dist
		
	def __str__(self):
		node_string = '{}:\n\t'.format(self.name)
		node_string += '\n\t'.join(['{}: {}'.format(node.name, self.neighbors[node]) for node in self.neighbors])
		return node_string
"""
	def add_neighbor(self, node, dist):
		self.neighbors.append(node)
	def __str__(self):
		node_string = '{}:\n\t'.format(self.name)
		node_string += '\n\t'.join(['{}: {}'.format(key, self.dist_map[key]) for key in self.dist_map])
		return node_string
"""