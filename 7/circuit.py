import re

from assembly import *

class Circuit(object):

	GATE_LEFT_SIDE_PATTERN = '(?P<a>.+) (?P<gate_type>(AND|OR)) (?P<b>.+)'
	SHIFT_LEFT_SIDE_PATTERN = '(?P<a>.+) (?P<shift_type>(LSHIFT|RSHIFT)) (?P<b>.+)'
	NOT_LEFT_SIDE_PATTERN = 'NOT (?P<a>.+)'
	SIGNAL_LEFT_SIDE_PATTERN = '(?P<a>.+)'

	def __init__(self):
		self.wires = {}

	def add_wire(self, wire, wire_id):
		if not self.get_wire(wire_id):
			self.wires[wire_id] = wire

	def get_wire(self, wire_name):
		return self.wires.get(wire_name)


	def assemble_parts(self, left_side, output_wire_name):
		
		output_wire = self.get_wire(output_wire_name)
		if not output_wire:
			output_wire = Wire()
			self.add_wire(output_wire, output_wire_name)

		if re.match(self.GATE_LEFT_SIDE_PATTERN, left_side):
			left_side_parts = re.search(self.GATE_LEFT_SIDE_PATTERN, left_side.strip()).groupdict()
			assemble_gate(self, output_wire, **left_side_parts)
		elif re.match(self.SHIFT_LEFT_SIDE_PATTERN, left_side):
			left_side_parts = re.search(self.SHIFT_LEFT_SIDE_PATTERN, left_side.strip()).groupdict()
			assemble_shift(self, output_wire, **left_side_parts)
		elif re.match(self.NOT_LEFT_SIDE_PATTERN, left_side):
			left_side_parts = re.search(self.NOT_LEFT_SIDE_PATTERN, left_side.strip()).groupdict()
			assemble_not(self, output_wire, **left_side_parts)
		elif re.match(self.SIGNAL_LEFT_SIDE_PATTERN, left_side):
			left_side_parts = re.search(self.SIGNAL_LEFT_SIDE_PATTERN, left_side.strip()).groupdict()
			assemble_signal_wire(self, output_wire, **left_side_parts)

	def __str__(self):
		wires_str = ''
		for wire_id in self.wires:
			wire = self.wires.get(wire_id)
			wires_str += '{}: {}'.format(wire_id, wire.get_signal())
			wires_str += '\n'
		
		return wires_str