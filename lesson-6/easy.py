# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class figure:
    def __init__(self, A1, A2, B1, B2, C1, C2):
        self.A1 = A1
        self.A2 = A2
        self.B1 = B1
        self.B2 = B2
        self.C1 = C1
        self.C2 = C2

class triangle(figure):
    def __init__(self):
        figure.__init__(self, A1, A2, B1, B2, C1, C2)
        AB = math.sqrt(int(((B1 - A1)**2) + ((B2 - A2)**2)))
        BC = math.sqrt(int(((C1 - B1)**2) + ((C2 - B2)**2)))
        AC = math.sqrt(int(((C1 - A1)**2) + ((C2 - A2)**2)))

    def perimetr(self):
        P = self.AB + self.BC + self.AC

    def square(self):
        s = self.P / 2
        S = math.sqrt(self.s*(self.s - self.AB)*(self.s - self.BC)*(self.s - self.AC))

    def height(self, ):
        height_ = S / 0.5 * AC


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math

class figure1:
    def __init__(self, A1, A2, B1, B2, C1, C2, D1, D2):
        self.A1 = A1
        self.A2 = A2
        self.B1 = B1
        self.B2 = B2
        self.C1 = C1
        self.C2 = C2
        self.D1 = D1
        self.D2 = D2

class trapecia(figure1):
    def __init__(self):
        figure.__init__(self, A1, A2, B1, B2, C1, C2, D1, D2)
        AC = math.sqrt(int(((C1 - A1)**2) + ((C2 - A2)**2)))
        BD = math.sqrt(int(((D1 - B1)**2) + ((D2 - B2)**2)))
        if AC == BD:
            print("Это равнобедренная трапеция")

    def sides(self):
        figure.__init__(self, A1, A2, B1, B2, C1, C2, D1, D2)
        AB = math.sqrt(int(((B1 - A1)**2) + ((B2 - A2)**2)))
        BC = math.sqrt(int(((C1 - B1)**2) + ((C2 - B2)**2)))
        CD = math.sqrt(int(((D1 - C1)**2) + ((D2 - C2)**2)))
        AD = math.sqrt(int(((D1 - A1)**2) + ((D2 - A2)**2)))

    def perimetr(self):
        P = self.AB + self.BC + self.CD + self.AD


    def squart(self):
        S = ((AB + BC) / 4) * math.sqrt((4 * CD**2) - ((AB - BC)**2))















