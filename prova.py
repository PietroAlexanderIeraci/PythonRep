class Function:
    def __init__(self, name):
        self.name = name
    def eval(self):
        pass
    def f_hat(self, a, b, N):
        self.a = a
        self.b = b
        self.N = N
        delta = (b-a)/N
        tot = 0
        for i in range(N):
            tot += self.eval(a+(i*delta))
        return (1/N)*tot

class My_fun(Function):
    def __init__(self):
        super().__init__("funz")
    def eval(self, x):
        return x**2+x*2

x = My_fun()
print(x.eval(3))
print(x.f_hat(0,6,4))