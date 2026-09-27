from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# З'єднання з базою даних PostgreSQL
DATABASE_URL = "postgresql://demianvyrozub@localhost:5432/university"
engine = create_engine(DATABASE_URL)

# Базовий клас для визначення моделей даних
Base = declarative_base()

# Проміжна таблиця для відношення "багато до багатьох"
student_course = Table(
    "student_course",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer)

    # Один студент може бути зареєстрований на декілька курсів
    courses = relationship("Course", secondary=student_course, back_populates="students")

    def __repr__(self):
        return f"<Student {self.id}: {self.name}>"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    teacher = Column(String(100))

    # На один курс може бути зареєстровано декілька студентів
    students = relationship("Student", secondary=student_course, back_populates="courses")

    def __repr__(self):
        return f"<Course {self.id}: {self.title}>"


# Фабрика сесій
Session = sessionmaker(bind=engine)


def create_tables():
    """Створює таблиці у базі даних."""
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
    print("Таблиці створено")
