class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        perimetro = self.a + self.b + self.c
    
        return perimetro

    def tipo_lado(self):
        if self.a != self.b and self.b != self.c and self.a != self.c:
            return "escaleno"
        else:
            if self.a == self.b and self.a == self.c and self.b == self.c:
                return "equilátero"
            else:
                if self.a == self.b or self.a == self.c or self.b == self.c:
                    return "isósceles"

    def retangulo(self):
        a2 = self.a**2
        b2 = self.b**2
        c2 = self.c**2

        return (a2 + b2) == c2 or (a2 + c2) == b2 or (b2 + c2) == a2
