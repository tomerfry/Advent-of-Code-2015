UNKNOWN_VALUE = -1

class Sample(object):
	def __init__(self, sample_id=UNKNOWN_VALUE, children=UNKNOWN_VALUE,\
	 cats=UNKNOWN_VALUE, samoyeds=UNKNOWN_VALUE, pomeranians=UNKNOWN_VALUE,\
	 akitas=UNKNOWN_VALUE, vizslas=UNKNOWN_VALUE, goldfish=UNKNOWN_VALUE, \
	 trees=UNKNOWN_VALUE, cars=UNKNOWN_VALUE, perfumes=UNKNOWN_VALUE):
		self.sample_id = sample_id
		self.children = children
		self.cats = cats
		self.samoyeds = samoyeds
		self.pomeranians = pomeranians
		self.akitas = akitas
		self.vizslas = vizslas
		self.goldfish = goldfish
		self.trees = trees
		self.cars = cars
		self.perfumes = perfumes

	def __str__(self):
		return """children: {children}\ncats: {cats}\nsamoyeds: {samoyeds}\npomeranians: {pomeranians}\nakitas: {akitas}\
		\nvizslas: {vizslas}\ngoldfish: {goldfish}\ntrees: {trees}\ncars: {cars}\nperfumes: {perfumes}
		""".format(**self.__dict__)

	def __eq__(self, other):

		if self.children == UNKNOWN_VALUE or other.children == UNKNOWN_VALUE:
			matching = True
		elif self.children != other.children:
			return False

		if self.cats == UNKNOWN_VALUE or other.cats == UNKNOWN_VALUE:
			mathcing = True
		elif self.cats <= other.cats :
			return False
			
		if self.samoyeds == UNKNOWN_VALUE or other.samoyeds == UNKNOWN_VALUE:
			mathcing = True
		elif self.samoyeds != other.samoyeds:
			return False
			
		if self.pomeranians == UNKNOWN_VALUE or other.pomeranians == UNKNOWN_VALUE:
			mathcing = True
		elif self.pomeranians >= other.pomeranians:
			return False
			
		if self.akitas == UNKNOWN_VALUE or other.akitas == UNKNOWN_VALUE:
			mathcing = True
		elif self.akitas != other.akitas:
			return False
			
		if self.vizslas == UNKNOWN_VALUE or other.vizslas == UNKNOWN_VALUE:
			mathcing = True
		elif self.vizslas != other.vizslas:
			return False
			
		if self.goldfish == UNKNOWN_VALUE or other.goldfish == UNKNOWN_VALUE:
			mathcing = True
		elif self.goldfish >= other.goldfish:
			return False
			
		if self.trees == UNKNOWN_VALUE or other.trees == UNKNOWN_VALUE:
			mathcing = True
		elif self.trees <= other.trees:
			return False
			
		if self.cars == UNKNOWN_VALUE or other.cars == UNKNOWN_VALUE:
			mathcing = True
		elif self.cars != other.cars:
			return False
			
		if self.perfumes == UNKNOWN_VALUE or other.perfumes == UNKNOWN_VALUE:
			mathcing = True
		elif self.perfumes != other.perfumes:
			return False
			



		return matching