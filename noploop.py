
from latticecpu.instruction import *
from latticecpu.cpu import Cpu
from latticecpu.memory import Memory

def main():
    insts = [
            NopInstruction(),
            JumpInstruction(0),
            NopInstruction()
    ]
    rom = Memory(0, insts)
    ram = Memory(0, [0]*128)

    cpu = Cpu(rom, ram, True)
    cpu.run(10)

if __name__ == "__main__":
    main()
