import os

# Налаштування БД беруться з оточення — саме через них контейнер з додатком
# знаходить контейнер з Postgres (DB_HOST = ім'я контейнера у мережі Docker).
DB_NAME = os.getenv("DB_NAME", "test_db")
DB_USER = os.getenv("DB_USER", "test_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "test_password")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# Скільки чекати, поки Postgres у сусідньому контейнері підніметься
DB_STARTUP_TIMEOUT = int(os.getenv("DB_STARTUP_TIMEOUT", "30"))

TABLE_NAME = "calculations"


def db_params() -> dict:
    return {
        "dbname": DB_NAME,
        "user": DB_USER,
        "password": DB_PASSWORD,
        "host": DB_HOST,
        "port": DB_PORT,
    }
