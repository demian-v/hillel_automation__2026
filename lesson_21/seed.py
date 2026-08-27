import random

from models import Base, Course, Session, Student, engine

COURSES = [
    ("Python Basics", "Іваненко О."),
    ("Automation QA", "Петренко І."),
    ("SQL та бази даних", "Коваленко М."),
    ("Git та CI/CD", "Шевченко А."),
    ("API Testing", "Бондаренко Т."),
]

NAMES = [
    "Олег Іванов", "Марія Коваль", "Андрій Мельник", "Оксана Ткаченко",
    "Дмитро Бондар", "Ірина Шевчук", "Сергій Лисенко", "Наталія Гнатюк",
    "Віктор Романюк", "Юлія Кравець", "Тарас Поліщук", "Анна Савченко",
    "Максим Гринь", "Софія Марчук", "Богдан Кушнір", "Катерина Дяченко",
    "Ігор Пилипенко", "Вікторія Захарчук", "Роман Гончар", "Аліна Мороз",
]


def seed():
    # Очищаємо таблиці, щоб скрипт можна було запускати повторно
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session = Session()

    # 5 курсів
    courses = [Course(title=title, teacher=teacher) for title, teacher in COURSES]
    session.add_all(courses)

    # 20 студентів, кожен рандомно записаний на 1-3 курси
    for i, name in enumerate(NAMES, start=1):
        student = Student(
            name=name,
            email=f"student{i}@example.com",
            age=random.randint(18, 30),
        )
        student.courses = random.sample(courses, random.randint(1, 3))
        session.add(student)

    session.commit()

    print(f"Створено курсів: {session.query(Course).count()}")
    print(f"Створено студентів: {session.query(Student).count()}")

    session.close()


if __name__ == "__main__":
    seed()
