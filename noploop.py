
from latticecpu.instruction import *
from latticecpu.cpu import Cpu
from latticecpu.memory import Memory

def main():
    insts = [
            NopInstruction(),
            JumpInstruction(0),
            NopInstruction()
    ]
    memory = Memory(0, insts)
    cpu = Cpu(memory, True)
    cpu.run(10)

if __name__ == "__main__":
    main()
