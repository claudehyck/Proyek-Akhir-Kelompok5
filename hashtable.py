class TicketHash:
    def __init__(self):
        self.table = [[] for _ in range(10)]  
    def _hash(self, key): return sum(ord(c) for c in str(key)) % 10
    def insert(self, tid):
        slot = self._hash(tid)
       
        if tid not in self.table[slot]:
            self.table[slot].append(tid)
    def check(self, tid):
        slot = self._hash(tid)
        return tid in self.table[slot]
