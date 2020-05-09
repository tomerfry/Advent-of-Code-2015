class Ingredient(object):

	def __init__(self, name, capacity, durability, flavor, texture, calories):
		self.name = name
		self.capacity = capacity
		self.durability = durability
		self.flavor = flavor
		self.texture = texture
		self.calories = calories
		self.spoons = 0

	def get_name(self):
		return self.name

	def get_capacity(self):
		return self.capacity * self.spoons

	def get_durability(self):
		return self.durability * self.spoons

	def get_flavor(self):
		return self.flavor * self.spoons

	def get_texture(self):
		return self.texture * self.spoons

	def get_calories(self):
		return self.calories * self.spoons

	def get_spoons(self):
		return self.spoons

	def set_spoons(self, spoons):
		self.spoons = spoons

	def __str__(self):
		return '{}: capacity {}, durability {}, flavor {}, texture {}, calories {}'.format(self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories)

