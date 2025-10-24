import sys
from math import sqrt


def get_coef(index, prompt):
    while True:
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()
        try:
            coef = float(coef_str)
            return coef
        except ValueError:
            print("Ошибка: введите корректное действительное число")
            if index < len(sys.argv):
                index = len(sys.argv) + 1


def solve_biquadratic(a, b, c):
    result = []
    if a != 0:
        D = b * b - 4 * a * c
        if D < 0:
            return result
        elif D == 0:
            t = -b / (2.0 * a)
            if t > 0:
                x1 = sqrt(y)
                x2 = -sqrt(y)
                result.extend([x1, x2])
            elif t == 0:
                result.append(0.0)
        else:
            t1 = (-b + sqrt(D)) / (2.0 * a)
            t2 = (-b - sqrt(D)) / (2.0 * a)
            if t1 > 0:
                x1 = sqrt(t1)
                x2 = -sqrt(t1)
                result.extend([x1, x2])
            elif t1 == 0:
                result.append(0.0)
            if t2 > 0:
                x3 = sqrt(t2)
                x4 = -sqrt(t2)
                if t1 != 0 or t2 != 0:
                    result.extend([x3, x4])
            elif t2 == 0 and 0.0 not in result:
                result.append(0.0)
        return result
    return "Не биквадратное уравнение"

def main():
    print("Решение биквадратного уравнения Ax^4 + Bx^2 + C = 0")

    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = solve_biquadratic(a, b, c)

    if roots == "Не биквадратное уравнение":
        print('Не биквадратное уравнение')
    elif len(roots) == 0:
        print('Нет действительных корней')
    elif roots[0] == "бесконечное количество решений":
        print('Бесконечное количество решений')
    else:
        res = sorted(list(set(roots)))
        print(f'Найдено корней: {len(res)}')
        c = 0
        for i in res:
            c += 1
            print(f'Корень {c}: {i:.4f}')


if __name__ == "__main__":
    main()