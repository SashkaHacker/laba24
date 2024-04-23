#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 10


class Money:
    denominations = (
        5000,
        1000,
        500,
        100,
        50,
        10,
        5,
        2,
        1,
        0.5,
        0.1,
        0.05,
        0.01,
    )

    def __init__(self, lst):
        self.money = {i: 0 for i in Money.denominations}
        for i in lst:
            if i in Money.denominations:
                self.money[i] += 1

    def total(self):
        money = str(
            sum(
                denomination * count
                for denomination, count in self.money.items()
            )
        )
        money = money.split(".")
        return ",".join(money)

    def display(self):
        print("Сумма денег состоит из:")
        for denomination, count in self.money.items():
            if count > 0:
                print(f"{denomination} руб. - {count} шт.")
        print(f"Общая стоимость: {self.total()} руб.\n")

    def read(self):
        for denomination, count in self.money.items():
            count = int(
                input(f"Введите количество купюр номиналом {denomination} руб.")
            )
            self.money[denomination] += count

    def _opetations(self, other, operator):
        result = Money([])
        for i in result.denominations:
            match operator:
                case "+":
                    result.money[i] = self.money[i] + other.money[i]
                case "-":
                    result.money[i] = self.money[i] - other.money[i]
                case "*":
                    result.money[i] = self.money[i] * other
                case "/":
                    result.money[i] = self.money[i] / other
        return result

    def __add__(self, other):
        return self._opetations(other, "+")

    def __sub__(self, other):
        return self._opetations(other, "-")

    def __mul__(self, other):
        return self._opetations(other, "*")

    def __truediv__(self, other):
        return self._opetations(other, "/")

    def __eq__(self, other):
        return self.total() == other.total()

    def __lt__(self, other):
        return self.total() < other.total()

    def __le__(self, other):
        return self.total() <= other.total()

    def __gt__(self, other):
        return self.total() > other.total()

    def __ge__(self, other):
        return self.total() >= other.total()


if __name__ == "__main__":
    money1 = Money([5000, 100, 10, 0.5])
    money2 = Money([1000, 50, 5, 0.1])

    result_sum = money1 + money2
    result_sum.display()

    result_sub = money1 - money2
    result_sub.display()

    result_mul = money1 * 4
    result_mul.display()

    result_div = money1 / 5
    result_div.display()
