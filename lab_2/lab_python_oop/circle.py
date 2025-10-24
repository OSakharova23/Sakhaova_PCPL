from math import pi
from .abs_figure import Figure
from .color import FigureColor


class Circle(Figure):
    def __init__(self, radius, color):
        self._radius = radius
        self._color_property = FigureColor()
        self._color_property.color = color
        self._name = "Круг"

    @property
    def name(self):
        return self._name

    def S(self):
        return pi * self._radius ** 2

    def __repr__(self):
        return "{} {} цвета радиусом {}, площадью {:.2f}.".format(
            self._name,
            self._color_property.color,
            self._radius,
            self.S()
        )