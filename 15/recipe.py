class Recipe(object):

	def __init__(self, ingredients, quantities):
		self.ingredients = ingredients
		if len(ingredients) != len(quantities):
			raise Exception('Error: mismatch in recipe.')

		for index, quantity in enumerate(quantities):
			self.ingredients[index].set_spoons(quantity)

	def get_score(self):
		capacity = sum([ingredient.get_capacity() for ingredient in self.ingredients])
		durability = sum([ingredient.get_durability() for ingredient in self.ingredients])
		flavor = sum([ingredient.get_flavor() for ingredient in self.ingredients])
		texture = sum([ingredient.get_texture() for ingredient in self.ingredients])
		
		if capacity < 0:
			capacity = 0

		if durability < 0:
			durability = 0

		if flavor < 0:
			flavor = 0

		if texture < 0:
			texture = 0

		return capacity * durability * flavor * texture

	def get_calories(self):
		calorie_count = sum([ingredient.get_calories() for ingredient in self.ingredients])
		return calorie_count

	def __str__(self):
		return '\n'.join([str(ing.get_spoons()) for ing in self.ingredients])