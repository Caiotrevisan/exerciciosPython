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

    def semelhantes(self,triangulo):
        lados1 = sorted([self.a,self.b,self.c])
        
        lados2 = sorted([triangulo.a,triangulo.b,triangulo.c])
       
        

        if lados1[0]%lados2[0] == 0 and lados1[1]%lados2[1] == 0 and lados1[2]%lados2[2] == 0:
            return True
        else:
            if lados2[0]%lados1[0] == 0 and lados2[1]%lados1[1] == 0 and lados2[2]%lados1[2] == 0:
                return True
            else:
                return False
