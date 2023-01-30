class Series:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        if self.a <= self.b:
            self.a += 1
            return (self.a-1)**2
        else: 
            raise StopIteration

class Primi:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __iter__(self):
        return self
    def __next__(self):
        while self.a <= self.b:
            self.a += 1
            current = self.a -1
            if current < 3:
                return current
            else:
                i = 2
                divided = False
                while i<(current/2) and not divided:
                    if current%i==0:
                        divided = True
                    i += 1
                if not divided:
                    return current
        raise StopIteration

x = [n for n in Primi(0,30)]
print(x)