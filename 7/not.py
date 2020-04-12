from wire import Connectable, Wire

class Not(Connectable):
	def __init__(self, wire_a, output_wire):
		self.wire_a = wire_a
		self.output_wire = output_wire
		self.output_wire.set_input(self)

	def get_signal(self):
		return ~(self.wire_a.get_signal())