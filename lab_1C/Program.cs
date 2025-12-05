using System;

namespace BiquadraticEquationSolver
{
    class Program
    {
        static void Main(string[] args)
        {
            double a, b, c;

            // Парсинг аргументов командной строки
            if (args.Length >= 3)
            {
                if (!TryParseCoefficients(args, out a, out b, out c))
                {
                    Console.WriteLine("Ошибка в аргументах командной строки. Переход к вводу с клавиатуры.\n");
                    (a, b, c) = ReadCoefficientsFromConsole();
                }
                else if (a == 0)
                {
                    PrintColor(ConsoleColor.Yellow, "Ошибка: коэффициент A = 0, уравнение не является биквадратным.");
                    PrintColor(ConsoleColor.Yellow, "Необходимо ввести коэффициенты с клавиатуры.\n");
                    (a, b, c) = ReadCoefficientsFromConsole();
                }
                else
                {
                    Console.WriteLine($"Коэффициенты из командной строки: A = {a}, B = {b}, C = {c}");
                }
            }
            else
            {
                (a, b, c) = ReadCoefficientsFromConsole();
            }

            // Вывод уравнения
            Console.WriteLine($"\nБиквадратное уравнение: {FormatCoefficient(a)}x^4 + {FormatCoefficient(b)}x^2 + {FormatCoefficient(c)} = 0");

            // Решение уравнения
            SolveAndPrintBiquadratic(a, b, c);
        }

        // Форматирование коэффициента для вывода (убираем 1 и -1)
        static string FormatCoefficient(double coeff)
        {
            if (coeff == 1) return "";
            if (coeff == -1) return "-";
            return coeff.ToString();
        }

        // Парсинг коэффициентов из аргументов командной строки
        static bool TryParseCoefficients(string[] args, out double a, out double b, out double c)
        {
            a = 0;
            b = 0;
            c = 0;

            return double.TryParse(args[0], out a) &&
                   double.TryParse(args[1], out b) &&
                   double.TryParse(args[2], out c);
        }

        // Ввод коэффициентов с клавиатуры
        static (double a, double b, double c) ReadCoefficientsFromConsole()
        {
            Console.WriteLine("Введите коэффициенты биквадратного уравнения Ax^4 + Bx^2 + C = 0");

            double a = ReadCoefficient("A", true);
            double b = ReadCoefficient("B", false);
            double c = ReadCoefficient("C", false);

            return (a, b, c);
        }

        // Чтение одного коэффициента с валидацией
        static double ReadCoefficient(string coefficientName, bool isA)
        {
            while (true)
            {
                Console.Write($"Введите коэффициент {coefficientName}: ");
                string input = Console.ReadLine();

                if (double.TryParse(input, out double value))
                {
                    if (isA && value == 0)
                    {
                        Console.WriteLine("Коэффициент A не может быть равен 0 для биквадратного уравнения.");
                        Console.WriteLine("Пожалуйста, введите ненулевое значение для A.");
                        continue;
                    }
                    return value;
                }
                else
                {
                    PrintColor(ConsoleColor.Yellow, "Некорректный ввод. Пожалуйста, введите действительное число.");
                }
            }
        }

        // Решение биквадратного уравнения и вывод результатов
        static void SolveAndPrintBiquadratic(double a, double b, double c)
        {
            // Вычисляем дискриминант квадратного уравнения относительно x²
            double discriminant = b * b - 4 * a * c;

            if (discriminant < 0)
            {
                PrintColor(ConsoleColor.Red, "Действительных корней нет.");
                return;
            }

            // Вычисляем t1 и t2 (где t = x²)
            double sqrtDiscriminant = Math.Sqrt(discriminant);
            double t1 = (-b + sqrtDiscriminant) / (2 * a);
            double t2 = (-b - sqrtDiscriminant) / (2 * a);

            // Находим корни биквадратного уравнения
            var roots = new System.Collections.Generic.List<double>();

            if (t1 >= 0)
            {
                roots.Add(Math.Sqrt(t1));
                roots.Add(-Math.Sqrt(t1));
            }

            if (t2 >= 0 && Math.Abs(t2 - t1) > 1e-10) // Проверяем, чтобы не добавлять одинаковые корни
            {
                roots.Add(Math.Sqrt(t2));
                roots.Add(-Math.Sqrt(t2));
            }

            // Удаляем дубликаты (если t1 == t2)
            var uniqueRoots = new System.Collections.Generic.HashSet<double>();
            foreach (var root in roots)
            {
                uniqueRoots.Add(Math.Round(root, 10)); // Округление для избежания ошибок округления
            }

            // Выводим результат
            if (uniqueRoots.Count == 0)
            {
                PrintColor(ConsoleColor.Red, "Действительных корней нет.");
            }
            else
            {
                PrintColor(ConsoleColor.Green, "Найденные корни:");
                foreach (var root in uniqueRoots)
                {
                    PrintColor(ConsoleColor.Green, $"x = {root}");
                }
            }
        }

        // Вывод текста цветом
        static void PrintColor(ConsoleColor color, string message)
        {
            var originalColor = Console.ForegroundColor;
            Console.ForegroundColor = color;
            Console.WriteLine(message);
            Console.ForegroundColor = originalColor;
        }
    }
}