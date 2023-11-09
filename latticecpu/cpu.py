from .instruction import *

class Cpu():
    """Simulator of the CPU"""
    def __init__(self, memory, trace = False):
        self.memory = memory
        self.trace = trace
        self.pc = 0

    def reset(self):
        self.pc = 0

    def run(self, n):
        for _ in range(n):
            self.step()

    def fetch(self, pc):
        instruction = self.memory.fetch(pc)
        self.pc += 1
        return instruction

    def step(self):
        self.dump()
        instruction = self.fetch(self.pc)
        self.exec(instruction)

    def exec(self, instruction):
        instid = instruction.instid
        if instid == InstructionId.Nop:
            pass
        elif instid == InstructionId.Jump:
            self.pc = instruction.destination
        else:
            raise ValueError(f"Invalid instruction {instruction}")

    def dump(self):
        if not self.trace:
            return

        print(f"PC:{self.pc}")


