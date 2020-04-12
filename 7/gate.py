from wire import Connectable, Wire

class Gate(Connectable):

	GATE_PROCCESORS = {
	'AND': lambda x, y: x & y,
	'OR': lambda x, y: x | y
	}

	def __init__(self, gate_type, a, b, output_wire):
		self.a = a
		self.b = b
		self.processor = self.GATE_PROCCESORS.get(gate_type)
		self.output_wire = output_wire


	def get_signal(self):
		return self.processor(self.a.get_signal(), self.b.get_signal())