from .instruction import *

class Cpu():
    """Simulator of the CPU"""
    def __init__(self, inst_rom, memory, trace = False):
        self.inst_rom = inst_rom
        self.memory = memory
        self.trace = trace
        self.pc = 0

    def reset(self):
        self.pc = 0

    def run(self, n):
        for _ in range(n):
            self.step()

    def fetch(self, pc):
        instruction = self.inst_rom.fetch(pc)
        self.pc += 1
        return instruction

    def step(self):
        self.dump()
        inst = self.fetch(self.pc)
        self.exec(inst)

    def exec(self, inst):
        instid = inst.instid
        if instid == InstructionId.Nop:
            pass
        elif instid == InstructionId.Jump:
            self.pc = inst.destination
        elif instid == InstructionId.Set:
            addr = inst.addr
            value = inst.value
            self.memory.memory[addr] = value
        elif instid == InstructionId.Add:
            addr_dest,addr_src1,addr_src2 = inst.dest, inst.src1, inst.src2
            val1,val2 = self.memory.fetch(addr_src1), self.memory.fetch(addr_src2)
            self.memory.memory[addr_dest] = val1 + val2
        else:
            raise ValueError(f"Invalid inst {inst}")

    def dump(self):
        if not self.trace:
            return

        print(f"PC:{self.pc}")


