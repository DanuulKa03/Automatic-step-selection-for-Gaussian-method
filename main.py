import math

from prettytable import PrettyTable


def function(x: float) -> float:
    return math.sin(x ** 2)


class Simpson:
    @staticmethod
    def quadrature_formula(a: float, b: float, n: int) -> float:
        h = float((b - a) / n)
        return h / 6 * (function(a) + function(b) +
                        2 * sum(function(a + h * x) for x in range(1, n)) +
                        4 * sum(function(a + h * x - h / 2) for x in range(1, n + 1)))


class Rectangles:
    @staticmethod
    def rectangle_formula(a: float, b: float, n: int):
        h = float((b - a) / n)
        return h * sum(function(a + h * x - h / 2) for x in range(1, n + 1))


def rectangle_approximation(a: float, b: float, eps: float):
    table = PrettyTable()
    table.field_names = ["n", "I_n"]

    n = 2
    I_1 = Rectangles.rectangle_formula(a, b, n)

    table.add_row([n, I_1])

    n *= 2
    I_2 = Rectangles.rectangle_formula(a, b, n)

    table.add_row([n, I_2])

    while abs(I_1 - I_2) / (2 ** 2 - 1) >= eps:
        I_1 = I_2
        n *= 2
        I_2 = Rectangles.rectangle_formula(a, b, n)
        table.add_row([n, I_2])

    print(table)


def simpson_approximation(a: float, b: float, eps: float):
    table = PrettyTable()
    table.field_names = ["n", "I_n"]

    n = 2
    I_1 = Simpson.quadrature_formula(a, b, n)

    table.add_row([n, I_1])

    n *= 2
    I_2 = Simpson.quadrature_formula(a, b, n)

    table.add_row([n, I_2])

    while abs(I_1 - I_2) / (2 ** 4 - 1) >= eps:
        I_1 = I_2
        n *= 2
        I_2 = Simpson.quadrature_formula(a, b, n)
        table.add_row([n, I_2])

    print(table)

rectangle_approximation(0, 1, 0.0000000000001)
simpson_approximation(0, 1, 0.000001)
