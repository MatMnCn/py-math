class triangulo:
    a: int
    b: int
    c: int

    a = 0
    b = 0
    c = 0

    def area(self) -> float:
        from math import sqrt
        p = (self.a + self.b + self.c) / 2
        area = sqrt (p *(p-self.a) * (p-self.b) * (p - self.c)) **0,5
        return area