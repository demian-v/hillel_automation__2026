"""Шар роботи з Postgres: підключення та CRUD над таблицею calculations."""

import time

import psycopg2

from core.config import DB_STARTUP_TIMEOUT, TABLE_NAME, db_params


def connect():
    """Одне з'єднання з базою."""
    return psycopg2.connect(**db_params())


def wait_for_db(timeout: int = DB_STARTUP_TIMEOUT):
    """Дочекатись, поки Postgres прийматиме з'єднання.

    У Docker контейнер з додатком стартує швидше за базу, тому без очікування
    перший же connect падає з OperationalError.
    """
    deadline = time.monotonic() + timeout
    last_error = None
    while time.monotonic() < deadline:
        try:
            conn = connect()
            conn.close()
            return
        except psycopg2.OperationalError as error:
            last_error = error
            time.sleep(1)
    raise TimeoutError(f"Postgres не піднявся за {timeout} с: {last_error}")


def create_table():
    with connect() as conn, conn.cursor() as cursor:
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id         SERIAL PRIMARY KEY,
                number     INTEGER      NOT NULL CHECK (number >= 0),
                operation  VARCHAR(50)  NOT NULL,
                result     NUMERIC      NOT NULL,
                created_at TIMESTAMPTZ  NOT NULL DEFAULT now()
            )
            """
        )


def drop_table():
    with connect() as conn, conn.cursor() as cursor:
        cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")


def insert(number: int, operation: str, result: int) -> int:
    """Додати запис, повернути його id."""
    with connect() as conn, conn.cursor() as cursor:
        cursor.execute(
            f"INSERT INTO {TABLE_NAME} (number, operation, result) "
            f"VALUES (%s, %s, %s) RETURNING id",
            (number, operation, result),
        )
        return cursor.fetchone()[0]


def update_result(record_id: int, new_result: int) -> int:
    """Оновити результат, повернути кількість змінених рядків."""
    with connect() as conn, conn.cursor() as cursor:
        cursor.execute(
            f"UPDATE {TABLE_NAME} SET result = %s WHERE id = %s",
            (new_result, record_id),
        )
        return cursor.rowcount


def delete(record_id: int) -> int:
    """Видалити запис, повернути кількість видалених рядків."""
    with connect() as conn, conn.cursor() as cursor:
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = %s", (record_id,))
        return cursor.rowcount


def select_by_id(record_id: int):
    with connect() as conn, conn.cursor() as cursor:
        cursor.execute(
            f"SELECT id, number, operation, result FROM {TABLE_NAME} WHERE id = %s",
            (record_id,),
        )
        return cursor.fetchone()


def select_all():
    with connect() as conn, conn.cursor() as cursor:
        cursor.execute(
            f"SELECT id, number, operation, result FROM {TABLE_NAME} ORDER BY id"
        )
        return cursor.fetchall()


def count() -> int:
    with connect() as conn, conn.cursor() as cursor:
        cursor.execute(f"SELECT count(*) FROM {TABLE_NAME}")
        return cursor.fetchone()[0]
