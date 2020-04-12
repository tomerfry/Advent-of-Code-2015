import re

from circuit import Circuit


class InstructionsManager(object):
	INSTRUCTION_PATTERN = '(?P<left_side>.+) -> (?P<output_wire_name>.+)'


	def __init__(self, filename):
		with open(filename, 'r') as f:
			self.instructions = [line.strip() for line in f.readlines()]

	def handle_instruction(self, instruction, circuit):
		instruction_parts = re.search(self.INSTRUCTION_PATTERN, instruction)
		circuit.assemble_parts(**instruction_parts.groupdict())

	def compile(self):

		circuit = Circuit()

		for instruction in self.instructions:
			self.handle_instruction(instruction, circuit)

		return circuit