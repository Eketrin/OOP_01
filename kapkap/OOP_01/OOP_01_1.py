
''''
1.  Опишите класс Book, заданный названием, автором, издательством и годом издания.
Включите в описание класса методы: вывода информации о книге на экран
'''
import math
from itertools import product


class Book:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
    def description(self):
        return (f"Название: {self.title}\n"
                f"Автор: {self.author}\n"
                f"Издательство: {self.publisher}\n"
                f"Год издания: {self.year}\n")
    def is_new(self):
        if int(self.year) < 2021:
            return False
        else: return True


# b1 = Book("Как я встретил вашу маму", "Кристи Росс", "Ростерс инк", "1967")
# b2 = Book("Незабудка", "Маргаретт Лав", "Флаверс инк", "1985")
# b3 = Book("Морковка", "Марк Сонген", "Ростерс инк", "2022")
#
# print(b1.description())
# print(b3.is_new())
# print(b2.is_new())
''''
2.  Опишите класс Car, заданный маркой, моделью, годом выпуска и пробегом.
Включите в описание класса методы: вывода информации о машине на экран, проверки,
нужно ли произвести техническое обслуживание (пробег больше 10 000 км с последнего ТО)
'''

class Car:
    def __init__(self, mark, model, year, mileage):
        self.mark = mark
        self.model = model
        self.year = year
        self.mileage = mileage

    def info(self):
        return (f"Марка: {self.mark}\n"
                f"Модель: {self.model}\n"
                f"Год: {self.year}\n"
                f"Пробег: {self.mileage}\n")

    def check_need_TO(self):
        if int(self.mileage) > 10000:
            print(f"Необходимо произвести техобслуживание, пробег больше 10000: {self.mileage} км\n")
        else: print("Техобслуживание не требуется\n")

# c1 = Car("Toyota", "t560", "2000", "55000")
# c2 = Car("Csevrole", "lachetty", "2003", "5984")
# c3 = Car("Berry", "lichi", "2006", "60850")
#
# print(c1.info())
# c1.check_need_TO()
# print(c3.info())

''''
3.  Опишите класс Employee, заданный фамилией, именем, должностью и зарплатой. 
Включите в описание класса методы: вывода информации о сотруднике на экран, проверки, больше ли она базовой величины   
(больше 100 000 рублей)
'''

class Employee:
    def __init__(self, surname, name, job, salary):
        self.surname = surname
        self.name = name
        self.job = job
        self.salary = salary
    def info(self):
        print (f"Фамилия: {self.surname}\n"
                f"Имя: {self.name}\n"
                f"Должность: {self.job}\n"
                f"Зарплата: {self.salary}\n")
    def check_salary(self):
        if int(self.salary) > 100000:
            print(f"Заработная плата сотрудника БОЛЬШЕ базоваой величины\n")
        else: print("Заработная плата сотрудника МЕНЬШЕ базоваой величины\n")


# e1 = Employee("Зайкин", "Иван", "Контролёр", "68000")
# e2 = Employee("Волчков", "Михаил", "Актёр", "101000")
# e3 = Employee("Ёлочкин", "Ростислав", "Портье", "86000")
#
# e1.info()
# e1.check_salary()
# e2.info()
# e2.check_salary()


''''
4.  Опишите класс Product, заданный названием, ценой и количеством. 
Включите в описание класса методы: вывода информации о товаре на экран, проверки, есть ли товар в наличии (количество больше 0)
'''

class Product:
    def __init__(self, name, cost, quantity):
        self.name = name
        self.cost = cost
        self.quantity = quantity
    def info(self):
        print (f"Наименование: {self.name}\n"
                f"Цена: {self.cost}\n"
                f"Количество: {self.quantity}\n")

    def check_quantity(self):
        if int(self.quantity) > 0:
            print(f"Товар в наличии\n")
        else:
            print("Товар отсутствует\n")

# p1 = Product("Сгущёнка", "186", "8")
# p2 = Product("Блинчики", "203", "0")
# p3 = Product("Сметана", "150", "60")
#
# p2.info()
# p2.check_quantity()
#
# p3.info()
# p1.info()
# p1.check_quantity()

''''
5.  Опишите класс Circle, заданный радиусом. Включите в описание класса методы: 
вывода информации о круге на экран, расчета длины окружности и площади круга.
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def info(self):
        print(f"Радиус: {self.radius}")

    def calc_dop(self):
        print(f"Длина окружности: {(self.radius)*2*math.pi}\n"
                f"Площадь круга: {int(self.radius)**2*math.pi}\n")

# c1 = Circle(50)
# c2 = Circle(10)
# c3 = Circle(20)
#
# c1.info()
# c1.calc_dop()
# c2.info()
# c3.info()


'''
6. Опишите класс ТРАНСПОРТ с методами вывода на экран информации о транспортном средстве, 
а также определить грузоподъемность транспортного средства. 
Создать дочерние классы АВТОМОБИЛЬ (марка, номер, скорость грузоподъемность), 
МОТОЦИКЛ (марка, номер, скорость грузоподъемность, наличие коляски, если она отсутствует грузоподъемность = 0). 
ГРУЗОВИК (марка, номер, скорость, грузоподъемность, наличие прицепа, если есть прицеп - грузоподъемность 
увеличивается в2 раза) Со своими метолами вывода информации на экран и определения грузоподъемности 
'''

class Transport:
    def __init__(self, mark, number, speed, lifting_capacity):
        self.mark = mark
        self.number = number
        self.speed = speed
        self.lifting_capacity = lifting_capacity

    def info(self):
        print(f"Марка: {self.mark}\n"
                f"Номер: {self.number}\n"
                f"Скорость: {self.speed}\n"
                f"Грузоподъёмность: {self.get_lift_cap()}\n")
    def get_lift_cap(self):
        return self.lifting_capacity

class Automobile(Transport):
    def __init__(self, mark, number, speed, lifting_capacity):
        super().__init__(mark, number, speed, lifting_capacity)

    def info(self):
        print (f"Класс: Автомобиль\n"
                f"Марка: {self.mark}\n"
                f"Номер: {self.number}\n"
                f"Скорость: {self.speed}\n"
                f"Грузоподъёмность: {self.get_lift_cap()}\n")
    def get_lift_cap(self):
        return self.lifting_capacity

class Motorcycle(Transport):
    def __init__(self, mark, number, speed, lifting_capacity, sidecar = False):
        super().__init__(mark, number, speed, lifting_capacity)
        self.sidecar = sidecar

    def info(self):
        print (f"Класс: Мотоцикл\n"
                f"Марка: {self.mark}\n"
                f"Номер: {self.number}\n"
                f"Скорость: {self.speed}\n"
                f"Грузоподъёмность: {self.get_lift_cap()}\n"
                f"Коляска: {"Есть" if self.sidecar else "Нет"}\n")
    def get_lift_cap(self):
        if self.sidecar:
            return self.lifting_capacity
        else: return 0

class Truck(Transport):
    def __init__(self, mark, number, speed, lifting_capacity, trailer = False):
        super().__init__(mark, number, speed, lifting_capacity)
        self.trailer = trailer

    def info(self):
        print (f"Класс: Мотоцикл\n"
                f"Марка: {self.mark}\n"
                f"Номер: {self.number}\n"
                f"Скорость: {self.speed}\n"
                f"Грузоподъёмность: {self.get_lift_cap()}\n"
                f"Прицеп: {"Есть" if self.trailer else "Нет"}\n")          #возможно ошибка
    def get_lift_cap(self):
        if self.trailer:
            return self.lifting_capacity*2
        else: return self.lifting_capacity



# tr = Transport("Шевроле", "321ОЛР", 250, 12050)
# tr.info()
#
# moto = Motorcycle("Аврора", "654ОРП", 360, 120000)
# moto.info()
# moto1 = Motorcycle("Икарус", '321ТИМ', 382, 150000, True)
# moto1.info()
#
# truck = Truck("Буханка", '987АПР', 260, 886000)
# truck.info()
# truck1 = Truck('Горбушка', '952ДЛО', 350, 966000, True)
# truck1.info()



'''
7, Создать класс ФИГУРА с методами вычисления площади и периметра, а также методы, 
выводящие информацию о фигуре на экран. Создайте дочерние классы ПРЯМОУГОЛЬНИК. КРУГ ТРЕУГОЛЬНИК 
со своими методами вычисления площади и периметра. 
Создайте З фигуры и выведите полную информацикю о фигурах на экран
'''


class Figura:
    def __init__(self, name="Фигура"):
        self.name = name

    def info(self):
        print(f"Класс: {self.name}"
                f"Площадь: {round(self.plochad(), 3)}\n"
                f"Периметр: {round(self.perimeter(), 3)}\n")

    def plochad(self):
        return 0
    def perimeter(self):
        return 0
    # фигуры могут быть с разным кол-вом сторон и характеристиками,
    # поэтому нереально определить периметр и площадь каждой по 1 шаблону
    # -> по факту функции в классе есть, но по сути выводится только имя фигуры
    # я могла бы добавить высоту и длину, но чем это будет отличаться от прямоугольника?

class Rectangle(Figura):
    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    def plochad(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def info(self):
        print(f"Класс: {self.name}\n"
                f"Ширина: {self.width}\n"
                f"Высота: {self.height}\n"
                f"Площадь: {round(self.plochad(), 3)}\n"
                f"Периметр: {round(self.perimeter(), 3)}\n")

class Circle(Figura):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def plochad(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def info(self):
        print(f"Класс: {self.name}\n"
                f"Радиус: {self.radius}\n"
                f"Площадь: {round(self.plochad(), 3)}\n"
                f"Длина окружности: {round(self.perimeter(), 3)}\n")


class Triangle(Figura):
    def __init__(self, a, b, c):
        super().__init__("Треугольник")
        self.a = a
        self.b = b
        self.c = c

    def plochad(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    def info(self):
        print(f"Класс: {self.name}\n"
                f"Сторона A: {self.a}\n"
                f"Сторона B: {self.b}\n"
                f"Сторона C: {self.c}\n"
                f"Площадь: {round(self.plochad(), 3)}\n"
                f"Периметр: {round(self.perimeter(), 3)}\n")

# r = Rectangle(5, 3)
# c = Circle(4)
# t = Triangle(3, 4, 5)
#
# r.info()
# c.info()
# t.info()












