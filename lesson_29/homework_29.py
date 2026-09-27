"""Додаток ДЗ 29: обчислює факторіал і зберігає результат у Postgres."""

from core import db

OPERATION = "factorial"
DEFAULT_NUMBERS = [0, 1, 5, 10, 15]


def factorial(number: int) -> int:
    """Факторіал числа. Від'ємні числа не визначені."""
    if number < 0:
        raise ValueError("Факторіал визначений тільки для невід'ємних чисел")
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


def calculate_and_save(number: int) -> int:
    """Порахувати факторіал і зберегти результат у БД. Повертає id запису."""
    return db.insert(number, OPERATION, factorial(number))


def main(numbers=None):
    numbers = DEFAULT_NUMBERS if numbers is None else numbers

    db.wait_for_db()
    db.create_table()

    print(f"Підключено до Postgres. Рахуємо факторіали: {numbers}\n")
    for number in numbers:
        record_id = calculate_and_save(number)
        print(f"  {number}! = {factorial(number)}  -> збережено з id={record_id}")

    print(f"\nУсього записів у таблиці '{db.TABLE_NAME}': {db.count()}")
    return db.select_all()


if __name__ == "__main__":
    main()
