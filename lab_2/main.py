from colorama import Fore, init
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main():
    init(autoreset=True)
    N = 14

    rectangle = Rectangle(N, N, "синего")
    circle = Circle(N, "зеленого")
    square = Square(N, "красного")

    print(Fore.BLUE + str(rectangle))
    print(Fore.GREEN + str(circle))
    print(Fore.RED + str(square))


if __name__ == "__main__":
    main()