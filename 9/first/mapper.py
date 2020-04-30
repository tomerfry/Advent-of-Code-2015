class Mapper(object):
	def __init__(self, mapper_file):

		with open(mapper_file, 'r') as f:
			self.instructions = f.readlines()

	def create_mapping(self):