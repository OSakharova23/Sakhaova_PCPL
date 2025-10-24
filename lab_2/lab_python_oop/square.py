from .rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side, color):
        super().__init__(side, side, color)
        self._name = "Квадрат"

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return "{} {} цвета со стороной {}, площадью {}.".format(
            self._name,
            self._color_property.color,
            self._width,
            self.S()
        )