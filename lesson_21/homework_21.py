from models import Course, Session, Student

session = Session()

# ============================================================
# 1. Додавання нового студента та запис його на курс
# ============================================================
print("=" * 55)
print("1. Додавання нового студента")
print("=" * 55)

new_student = Student(name="Демян Вирозуб", email="demian@example.com", age=25)

# Знаходимо курс і додаємо студента на нього
course = session.query(Course).filter_by(title="Automation QA").first()
new_student.courses.append(course)

session.add(new_student)
session.commit()

print(f"Додано студента: {new_student.name} (id={new_student.id})")
print(f"Записано на курс: {course.title}")

# Перевіряємо, що зміни збереглися в базі
check = session.query(Student).filter_by(email="demian@example.com").first()
print(f"Перевірка з БД: {check.name}, курси: {[c.title for c in check.courses]}")


# ============================================================
# 2. Запити до бази даних
# ============================================================
print()
print("=" * 55)
print("2. Запити до бази даних")
print("=" * 55)

# 2.1 Студенти, зареєстровані на певний курс
course_title = "Python Basics"
students_on_course = (
    session.query(Student)
    .join(Student.courses)
    .filter(Course.title == course_title)
    .all()
)

print(f"\nСтуденти на курсі '{course_title}' ({len(students_on_course)}):")
for student in students_on_course:
    print(f"  - {student.name}, {student.age} років, {student.email}")

# 2.2 Курси, на які зареєстрований певний студент
student = session.query(Student).filter_by(email="demian@example.com").first()

print(f"\nКурси студента '{student.name}':")
for c in student.courses:
    print(f"  - {c.title} (викладач: {c.teacher})")

# 2.3 Кількість студентів на кожному курсі
print("\nКількість студентів на кожному курсі:")
for c in session.query(Course).all():
    print(f"  - {c.title}: {len(c.students)}")


# ============================================================
# 3. Оновлення та видалення даних
# ============================================================
print()
print("=" * 55)
print("3. Оновлення та видалення")
print("=" * 55)

# 3.1 Оновлення даних студента
student = session.query(Student).filter_by(email="demian@example.com").first()
print(f"\nБуло: {student.name}, вік {student.age}")
student.age = 26
student.name = "Демян В."
session.commit()
print(f"Стало: {student.name}, вік {student.age}")

# 3.2 Оновлення курсу
course = session.query(Course).filter_by(title="Git та CI/CD").first()
print(f"\nБуло: {course.title}, викладач {course.teacher}")
course.teacher = "Новий Викладач"
session.commit()
print(f"Стало: {course.title}, викладач {course.teacher}")

# 3.3 Додаємо студента ще на один курс
extra_course = session.query(Course).filter_by(title="SQL та бази даних").first()
student.courses.append(extra_course)
session.commit()
print(f"\nКурси після додавання: {[c.title for c in student.courses]}")

# 3.4 Видалення студента з курсу (але студент залишається в базі)
student.courses.remove(extra_course)
session.commit()
print(f"Курси після видалення одного: {[c.title for c in student.courses]}")

# 3.5 Видалення студента з бази даних
print(f"\nВсього студентів до видалення: {session.query(Student).count()}")
session.delete(student)
session.commit()
print(f"Всього студентів після видалення: {session.query(Student).count()}")

session.close()
