import math

class FiguraGeometrica:
    def area(self):
        pass
    def perimetro(self):
        pass

class Triangolo(FiguraGeometrica):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def string(self):
        if self.a == self.b == self.c:
            return "Triangolo equilatero"
        if self.a == self.b or self.b == self.c or self.a == self.c:
            return "Triangolo isoscele"
        return "Triangolo scaleno"
    
    def perimetro(self):
        return self.a+self.b+self.c

    def area(self):
        p = self.perimetro()/2
        x = p*((p-self.a)*(p-self.b)*(p-self.c))
        return math.sqrt(x)

class Rettangolo(FiguraGeometrica):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def string(self):
        if self.a == self.b:
            return "Quadrato"
        return "Rettangolo"
    
    def perimetro(self):
        return (self.a+self.b) * 2

    def area(self):
        return self.a * self.b

def sum_aree(figure):
    return sum([fig.area() for fig in figure])


b = Rettangolo (2,2)
c = Rettangolo(3,3)
l = [b,c]
print(sum_aree(l))