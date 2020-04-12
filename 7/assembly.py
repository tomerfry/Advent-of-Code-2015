
from wire import Wire, Signal
from gate import Gate
from shift import Shift
from not_gate import Not

def assemble_input(circuit, value):
	try:
		input_signal = int(value)
	except ValueError:
		input_part = circuit.get_wire(value)
		if not input_part:
			input_part = Wire()
			wire_name = value
			circuit.add_wire(input_part, wire_name)
	else:
		input_part = Signal(input_signal)

	return input_part

def assemble_signal_wire(circuit, output_wire, a):
	part_a = assemble_input(circuit, a)
	output_wire.set_input(part_a)


def assemble_gate(circuit, output_wire, a, gate_type, b):
	part_a = assemble_input(circuit, a)
	part_b = assemble_input(circuit, b)

	gate = Gate(gate_type, part_a, part_b, output_wire)
	output_wire.set_input(gate)



def assemble_shift(circuit, output_wire, a, shift_type, b):
	part_a = assemble_input(circuit, a)
	part_b = assemble_input(circuit, b)

	shift = Shift(shift_type, part_a, part_b, output_wire)
	output_wire.set_input(shift)


def assemble_not(circuit, output_wire, a):
	part_a = assemble_input(circuit, a)

	not_gate = Not(part_a, output_wire)
	output_wire.set_input(not_gate)