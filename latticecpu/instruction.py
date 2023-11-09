from enum import IntEnum

class InstructionId(IntEnum):
    Invalid = -1
    Nop = 0
    Jump = 1

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
