class NoInput(Exception):
	pass

class Connectable(object):
	def get_signal(self):
		raise NotImplemented()

class Signal(Connectable):
	def __init__(self, value):
		self.value = value

	def get_signal(self):
		return self.value

class Wire(Connectable):
	def __init__(self):
		self.signal = None
		self.input_part = None

	def set_input(self, input_part):
		self.input_part = input_part

	def set_signal(self, signal):
		self.signal = signal

	def get_signal(self):
		if not self.input_part:
			raise NoInput('Missing connected input-part.')
		if not self.signal:
			self.signal = self.input_part.get_signal()
		return self.signal

	def __str__(self):
		return self.signal

