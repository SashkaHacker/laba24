#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Вариант 10
# Линейное уравнение y = Ax + B. Поле first — дробное число, коэффициент A; поле second
# — дробное число, коэффициент B. Реализовать метод function() — вычисление для
# заданного x значения функции y.


class LinearEquation:
    def __init__(self, first, second):
        if not isinstance(first, (int, float)) or not isinstance(
            second, (int, float)
        ):
            raise ValueError("Коэффициенты должны быть числами.")
        self.first = first
        self.second = second

    def read(self):
        self.first = float(input("Введите коэффициент a: "))
        self.second = float(input("Введите коэффициент b: "))

    def display(self):
        print(f"Линейное уравнение: {self.first}x + {self.second} = 0")

    def function(self, x):
        return self.first * x + self.second


if __name__ == "__main__":
    equation1 = LinearEquation(1, 2)
    equation1.display()
    print(equation1.function(10))

    equation2 = LinearEquation(0, 0)
    equation2.read()
    equation2.display()
    x = float(input("Введите значение x для вычисления функции: "))
    print(f"Значение функции: {equation2.function(x)}")
