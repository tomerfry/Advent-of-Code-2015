class Node(object):
	def __init__(self, name):
		self.name = name
		self.nodes = {}

	def insert_node(self, node, distance):
		self.nodes[node] = distance
