from .abs_figure import Figure
from .color import FigureColor


class Rectangle(Figure):
    def __init__(self, width, height, color):
        self._width = width
        self._height = height
        self._color_property = FigureColor()
        self._color_property.color = color
        self._name = "Прямоугольник"

    @property
    def name(self):
        return self._name

    def S(self):
        return self._width * self._height

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {}, площадью {}.".format(
            self._name,
            self._color_property.color,
            self._width,
            self._height,
            self.S()
        )