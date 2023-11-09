
class Memory(object):
    """Simulate the memory"""

    def __init__(self, base, memory):
        self.base = base
        self.memory = memory
        self.top = self.base + len(self.memory)

    def fetch(self, pc):
        if not (pc >= self.base and pc < self.top):
            raise IndexError(f"fetch address {pc} not in memory range")
        value = self.memory[pc]
        return value
