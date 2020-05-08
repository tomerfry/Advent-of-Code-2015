

class Reindeer(object):

	def __init__(self, name, speed, fly_duration, rest_duration):
		self.name = name
		self.speed = speed
		self.fly_duration = fly_duration
		self.rest_duration = rest_duration

	def get_name(self):
		return self.name

	def fly_for(self, duration):
		distance = 0
		time_resting = 0
		time_flying = 0
		resting = False

		while duration > 0:
			# A second passes.
			duration -= 1
			
			if not resting:
				time_flying += 1
				distance += self.speed * 1
			else:
				time_resting += 1

			if time_flying == self.fly_duration and not resting:
				# Needs rest
				resting = True
				time_flying = 0
			elif resting and time_resting == self.rest_duration:
				# Can fly
				resting = False
				time_resting = 0

		return distance
