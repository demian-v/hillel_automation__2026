import pytest

from core import db


@pytest.fixture(scope="session", autouse=True)
def prepared_database():
    """Один раз на сесію: дочекатись Postgres і створити таблицю.

    Таблицю після тестів НЕ видаляємо: ізоляцію забезпечує фікстура
    clean_table перед кожним тестом, а drop на виході знищував би й дані,
    записані самим додатком.
    """
    db.wait_for_db()
    db.create_table()


@pytest.fixture
def clean_table():
    """Порожня таблиця перед кожним тестом — щоб тести не залежали один від одного."""
    db.drop_table()
    db.create_table()
    return db


@pytest.fixture
def saved_record(clean_table):
    """Один готовий запис у таблиці: 5! = 120."""
    record_id = clean_table.insert(5, "factorial", 120)
    return record_id
