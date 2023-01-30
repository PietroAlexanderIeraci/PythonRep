import math

class Function:
    def __init__(self, name, a, b):
        self.a = a
        self.b = b
        self.name = name

    def eval(self, x):
        pass

    def printname(self):
        print("Funzione =", self.name,
              "\nDominio = [", self.a, ",", self.b, "]")

    def scient_name(self):
        pass

    def min_val(self, delta_x = 0.5):
        x_lis = [i for i in range(self.a, self.b +1)]
        y = [self.eval(x) for x in x_lis]
        return min(y)

    def integral(self, delta_x = 0.5):
        tot = 0
        i = self.a
        while i <= self.b:
            tot += self.eval(i)
            i += delta_x
        tot = tot*delta_x
        return tot

class Retta(Function):
    def __init__(self, name, a, b, m, q):
        super().__init__(name, a, b)
        self.m = m
        self.q = q

    def scient_name(self):
        text = str("f(x) = " + str(self.m) + "x+" + str(self.q))
        return text

    def printname(self):
        super().printname()

        print("Coefficiente angolare =", self.m)
        print("Quota =", self.q)

    def eval(self, x):
        return self.m*x + self.q

class Seno(Function):
    def __init__(self, name, a, b):
        super().__init__(name, a ,b)

    def eval(self, x):
        return math.sin(x)


tester = Retta("Retta", -2, 12, 3, 4)
print(tester.scient_name())
print(tester.integral())
print(tester.min_val())



sintest = Seno("Seno", 0, (2*math.pi))
sintest.printname()
print(sintest.integral(0.001))