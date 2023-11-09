from enum import IntEnum

class InstructionId(IntEnum):
    Invalid = -1
    Nop = 0
    Jump = 1
    Set = 2
    Add = 3

class Instruction(object):
    name = "Invalid Instruction"
    instid = InstructionId.Invalid

    def __init__(self):
        pass

class NopInstruction(Instruction):
    name = "nop"
    instid = InstructionId.Nop

    def __init__(self):
        pass

class JumpInstruction(Instruction):
    name = "jmp"
    instid = InstructionId.Jump

    def __init__(self, destination):
        self.destination = destination

class SetInstruction(Instruction):
    name = "set"
    instid = InstructionId.Set

    def __init__(self, addr, value):
        self.addr = addr
        self.value = value

class AddInstruction(Instruction):
    name = "add"
    instid = InstructionId.Add

    def __init__(self, dest, src1, src2):
        self.dest = dest
        self.src1 = src1
        self.src2 = src2
