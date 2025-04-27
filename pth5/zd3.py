# Тестирование с unittest

import sys
import unittest

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):
    def test_1(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_2(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-10)

    def test_3(self):
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_4(self):
        with self.assertRaises(ValueError):
            factorial(100000)
        with self.assertRaises(ValueError):
            factorial(sys.maxsize + 1)

    def test_5(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_6(self):
        self.assertIsInstance(factorial(4), int)

    def test_7(self):
        with self.assertRaises(TypeError):
            factorial(3.14)
        with self.assertRaises(TypeError):
            factorial(3.0)
        with self.assertRaises(TypeError):
            factorial("орпопрооп")
        with self.assertRaises(TypeError):
            factorial("6")


if __name__ == '__main__':
    unittest.main()


# Пояснение кода:
#
# класс TestFactorial наследует от unittest.TestCase
# класс содержит тесты для функции factorial
# внутри класса мы определяем несколько методов, каждый из
# которых проверяет определенные аспекты работы функции
# В методе test_1  проверяем, что функция factorial возвращает
# правильные значения для факториалов, таких как 5 и 10
# используем метод assertEqual, чтобы сравнить результат выполнения
# функции с ожидаемым значением
# В методе test_2 проверяем, что функция вызывает исключение ValueError,
# когда ей передаются отрицательные числа
# используем контекстный менеджер with и метод assertRaises, чтобы убедиться,
# что исключение действительно возникает
# Метод test_3 проверяет, что функция правильно вычисляет факториал для числа 20,
# которое является достаточно большим, чтобы убедиться в корректности работы функции
# позволяет нам протестировать, как функция справляется с большими значениями.
# В методе test_4 снова проверяем, что функция вызывает исключение ValueError для
# очень больших значений, таких как 100000 и sys.maxsize + 1.
# факториалы этих чисел превышают пределы, которые может обрабатывать тип int,
# функция корректно должна обрабатывать такие случаи, не вызывая переполнения.
# Метод test_5 проверяет базовые случаи для факториала, подтверждая, что факториал
# нуля равен 1, а также что факториал единицы также равен 1
# Метод test_6 проверяет, что результат выполнения функции factorial для
# числа 4 является целым числом (int)
# нужно чтобы убедиться, что функция возвращает значение ожидаемого типа
# В методе test_7  проверяем, что функция вызывает исключение TypeError,
# если ей передаются аргументы неправильного типа
# тестируем несколько случаев: передаем числа с плавающей точкой, такие
# как 3.14 и 3.0, а также строки, например, "орпопрооп" и "6"
# нужно чтобы убедиться, что функция корректно обрабатывает некорректные
# входные данные и не допускает их к вычислениям
# if __name__ == '__main__':
# unittest.main()
# Эта часть кода проверяет, запущен ли скрипт напрямую
# если это так, вызывается unittest.main(), что запускает все тесты,
# определенные в классе TestFactorial