class StringIterator:

    def __init__(self, compressedString: str):
        self.q = deque()
        char = None
        freq = 0
        for c in compressedString:
            if not c.isdigit():
                if freq != 0:
                    self.q.append([char, freq])
                    freq = 0
                char = c
            else:
                freq = 10 * freq + int(c)
        self.q.append([char, freq])

    def next(self) -> str:
        if not self.q:
            return " "
        
        res = self.q[0][0]
        self.q[0][1] -= 1
        if self.q[0][1] == 0:
            self.q.popleft()
        
        return res
        
        
    def hasNext(self) -> bool:
        if self.q:
            return True
        else:
            return False 