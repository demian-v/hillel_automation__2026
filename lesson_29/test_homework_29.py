import psycopg2
import pytest

import homework_29
from core import db
from core.config import TABLE_NAME


# --------------------------------------------------------------------------
# Підключення до бази даних
# --------------------------------------------------------------------------

@pytest.mark.db
def test_database_connection():
    """З'єднання з Postgres встановлюється і є робочим."""
    conn = db.connect()
    assert conn.closed == 0

    with conn.cursor() as cursor:
        cursor.execute("SELECT 1")
        assert cursor.fetchone()[0] == 1
    conn.close()


@pytest.mark.db
def test_table_exists():
    """Таблиця, з якою працює додаток, створена."""
    with db.connect() as conn, conn.cursor() as cursor:
        cursor.execute("SELECT to_regclass(%s)", (TABLE_NAME,))
        assert cursor.fetchone()[0] == TABLE_NAME


# --------------------------------------------------------------------------
# Вставка записів
# --------------------------------------------------------------------------

@pytest.mark.db
def test_insert_record(clean_table):
    """INSERT додає рядок і повертає його id."""
    record_id = clean_table.insert(5, "factorial", 120)

    assert record_id is not None
    assert clean_table.count() == 1
    assert clean_table.select_by_id(record_id) == (record_id, 5, "factorial", 120)


@pytest.mark.db
def test_insert_several_records(clean_table):
    """Кілька INSERT підряд дають кілька рядків."""
    for number, result in [(0, 1), (1, 1), (5, 120)]:
        clean_table.insert(number, "factorial", result)

    assert clean_table.count() == 3


@pytest.mark.db
def test_insert_negative_number_is_rejected(clean_table):
    """CHECK-обмеження не дає зберегти від'ємне число."""
    with pytest.raises(psycopg2.errors.CheckViolation):
        clean_table.insert(-5, "factorial", 1)


# --------------------------------------------------------------------------
# Оновлення записів
# --------------------------------------------------------------------------

@pytest.mark.db
def test_update_record(saved_record):
    """UPDATE змінює значення існуючого рядка."""
    rows_changed = db.update_result(saved_record, 999)

    assert rows_changed == 1
    assert db.select_by_id(saved_record)[3] == 999


@pytest.mark.db
def test_update_missing_record_changes_nothing(clean_table):
    """UPDATE неіснуючого id не змінює жодного рядка."""
    assert clean_table.update_result(99999, 1) == 0


# --------------------------------------------------------------------------
# Видалення записів
# --------------------------------------------------------------------------

@pytest.mark.db
def test_delete_record(saved_record):
    """DELETE прибирає рядок із таблиці."""
    rows_deleted = db.delete(saved_record)

    assert rows_deleted == 1
    assert db.select_by_id(saved_record) is None
    assert db.count() == 0


@pytest.mark.db
def test_delete_missing_record_changes_nothing(clean_table):
    """DELETE неіснуючого id не видаляє нічого."""
    assert clean_table.delete(99999) == 0


# --------------------------------------------------------------------------
# Вибірка даних
# --------------------------------------------------------------------------

@pytest.mark.db
def test_select_all_returns_everything(clean_table):
    """SELECT повертає всі збережені рядки у порядку id."""
    clean_table.insert(3, "factorial", 6)
    clean_table.insert(4, "factorial", 24)

    rows = clean_table.select_all()

    assert len(rows) == 2
    assert [row[1] for row in rows] == [3, 4]
    assert [row[3] for row in rows] == [6, 24]


@pytest.mark.db
def test_select_from_empty_table(clean_table):
    """Порожня таблиця повертає порожній список."""
    assert clean_table.select_all() == []
    assert clean_table.count() == 0


# --------------------------------------------------------------------------
# Логіка додатку
# --------------------------------------------------------------------------

@pytest.mark.app
@pytest.mark.parametrize(
    "number, expected",
    [(0, 1), (1, 1), (5, 120), (10, 3628800)],
    ids=["zero", "one", "five", "ten"],
)
def test_factorial(number, expected):
    """Факторіал рахується правильно."""
    assert homework_29.factorial(number) == expected


@pytest.mark.app
def test_factorial_of_negative_raises():
    """Від'ємне число — помилка, а не мовчазний результат."""
    with pytest.raises(ValueError):
        homework_29.factorial(-1)


@pytest.mark.app
def test_app_saves_calculation_to_database(clean_table):
    """Головний сценарій: додаток рахує і зберігає результат у Postgres."""
    record_id = homework_29.calculate_and_save(6)

    assert clean_table.select_by_id(record_id) == (record_id, 6, "factorial", 720)


@pytest.mark.app
def test_app_main_saves_all_numbers(clean_table):
    """main() зберігає результат для кожного переданого числа."""
    rows = homework_29.main([3, 4])

    assert len(rows) == 2
    assert [row[3] for row in rows] == [6, 24]
