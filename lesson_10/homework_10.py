'''1. Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.'''

'''2. Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника з команди розробників. 
Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead'''



class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, team_size, department, programming_language):
        super().__init__(name, salary, department=department, programming_language=programming_language)
        self.team_size = team_size

team_lead = TeamLead("Test", 100, 5, "Developer", "Python")
print(hasattr(team_lead, "name"))
print(hasattr(team_lead, "salary"))
print(hasattr(team_lead, "department"))
print(hasattr(team_lead, "programming_language"))
print(hasattr(team_lead, "team_size"))


'''Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. 
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. 
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. 
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.'''



from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Triangle(Figure):
    def __init__(self, leg1, leg2, hypotenuse):
        super().__init__("Triangle")
        self.__leg1 = leg1
        self.__leg2 = leg2
        self.__hypotenuse = hypotenuse

    def square(self):
        return (self.__leg1 * self.__leg2) / 2

    def perimeter(self):
        return self.__leg1 + self.__leg2 + self.__hypotenuse


class Rhombus(Figure):
    def __init__(self, side, diagonal1, diagonal2):
        super().__init__("Rhombus")
        self.__side = side
        self.__diagonal1 = diagonal1
        self.__diagonal2 = diagonal2

    def square(self):
        return (self.__diagonal1 * self.__diagonal2) / 2

    def perimeter(self):
        return self.__side * 4


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.__width = width
        self.__height = height

    def square(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width + self.__height) * 2

list_of_figures = [
    Triangle(3, 4, 5),
    Rhombus(5, 6, 8),
    Rectangle(4, 7),
]

for shape in list_of_figures:
    print(f"{shape.name}: площа = {shape.square()}, периметр = {shape.perimeter()}")