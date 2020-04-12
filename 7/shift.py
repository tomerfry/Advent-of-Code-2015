from wire import Connectable, Wire

class Shift(Connectable):
	SHIFT_PROCCESORS = {
	'LSHIFT': lambda x, y: x << y,
	'RSHIFT': lambda x, y: x >> y
	}

	def __init__(self, shift_type, a, b, output_wire):
		self.a = a
		self.b = b
		self.processor = self.SHIFT_PROCCESORS.get(shift_type)
		self.output_wire = output_wire

	def get_signal(self):
		return self.processor(self.a.get_signal(), self.b.get_signal())
