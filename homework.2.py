# Шаг 1: Создаем класс Figure
class Figure:
    # Атрибут уровня класса
    unit = 'cm'  # можно установить 'cm' или 'mm'

    # Шаг 2: Конструктор без атрибутов
    def __init__(self):
        pass

    # Шаг 3: Нереализованный метод для подсчета площади
    def calculate_area(self):
        raise NotImplementedError("Метод calculate_area не реализован")

    # Шаг 4: Нереализованный метод для вывода информации
    def info(self):
        raise NotImplementedError("Метод info не реализован")


# Шаг 5: Создаем класс Square (квадрат), наследуем от Figure
class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length  # Приватный атрибут

    # Шаг 7: Переопределяем метод для подсчета площади квадрата
    def calculate_area(self):
        return self.__side_length ** 2

    # Шаг 8: Переопределяем метод info для вывода информации о квадрате
    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{Figure.unit}, area: {area}{Figure.unit}.")


# Шаг 9: Создаем класс Rectangle (прямоугольник), наследуем от Figure
class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length  # Приватный атрибут
        self.__width = width  # Приватный атрибут

    # Шаг 11: Переопределяем метод для подсчета площади прямоугольника
    def calculate_area(self):
        return self.__length * self.__width

    # Шаг 12: Переопределяем метод info для вывода информации о прямоугольнике
    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {area}{Figure.unit}.")


# Шаг 13: Создаем список из 2-х квадратов и 3-х прямоугольников
shapes = [
    Square(5),
    Square(7),
    Rectangle(5, 8),
    Rectangle(3, 6),
    Rectangle(10, 2)
]

# Шаг 14: Используем цикл для вызова метода info у всех объектов
for shape in shapes:
    shape.info()
