class Fibo:
    n = 1
    n_1 = 0
    current = 0
    def __init__(self, end):
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.end:  
            if self.current == 0:
                self.current += 1
                return 0
            if self.current == 1:
                self.current += 1
                return 1
            if self.current > 1:
                self.current += 1
                new = self.n + self.n_1
                self.n_1 = self.n
                self.n = new
                return new
        raise StopIteration

print([x for x in Fibo(14)])