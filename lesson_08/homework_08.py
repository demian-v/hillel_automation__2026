'''Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.'''

class Student:

    def __init__(self, name, second_name, age):
        self.name = name
        self.second_name = second_name
        self.age = age
        self.gpa = 0

    def change_gpa(self, value):
        self.gpa = value

student_one = Student('Alex', 'Frank', 17)
student_one.change_gpa(4)
print(f"Student name: {student_one.name}\n"
      f"Student second name: {student_one.second_name}\n"
      f"Student age: {student_one.age}\n"
      f"Student Grade point average: {student_one.gpa}")