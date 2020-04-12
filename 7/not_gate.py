from wire import Connectable, Wire

class Not(Connectable):
	def __init__(self, a, output_wire):
		self.a = a
		self.output_wire = output_wire

	def get_signal(self):
		return ~(self.a.get_signal()) & 0xffff