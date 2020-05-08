

class Reindeer(object):

	def __init__(self, name, speed, fly_duration, rest_duration):
		self.name = name
		self.speed = speed
		self.fly_duration = fly_duration
		self.rest_duration = rest_duration

		self.resting = False
		self.time_resting = 0
		self.time_flying = 0
		self.distance = 0
		self.points = 0

	def grant_point(self):
		self.points += 1

	def get_name(self):
		return self.name

	def get_points(self):
		return self.points

	def get_distance(self):
		return self.distance

	def compete_one_second(self):
		if not self.resting:
			self.time_flying += 1
			self.distance += self.speed * 1
		else:
			self.time_resting += 1

		if self.time_flying == self.fly_duration and not self.resting:
			# Needs rest
			self.resting = True
			self.time_flying = 0
		elif self.resting and self.time_resting == self.rest_duration:
			# Can fly
			self.resting = False
			self.time_resting = 0

