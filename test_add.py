
from latticecpu.instruction import *
from latticecpu.cpu import Cpu
from latticecpu.memory import Memory

import unittest

class TestAdd(unittest.TestCase):
    def test_3plus4(self):
        insts = [
            SetInstruction(0, 3),
            SetInstruction(1, 4),
            AddInstruction(2, 0, 1),
            JumpInstruction(3),
        ]
        rom = Memory(0, insts)
        ram = Memory(0, [0]*128)
        cpu = Cpu(rom, ram)
        cpu.run(10)

        self.assertEqual(ram.fetch(2), 7)

if __name__ == "__main__":
    unittest.main()
