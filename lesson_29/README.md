# Lesson 29 — Dockerize everything

Python-додаток, що обчислює факторіал і зберігає результат у **PostgreSQL**,
разом із тестами. Усе працює у Docker-контейнерах, з'єднаних мережею Docker.

> **Примітка щодо умови.** У тексті завдання не вказано, що саме має обчислювати
> додаток — лише що він «зберігає результат у базу даних Postgres». Обрано
> факторіал як найпростішу детерміновану операцію; логіка обчислення винесена в
> `homework_29.factorial()` і легко замінюється.

## Структура

```
lesson_29/
├── homework_29.py          # додаток: рахує факторіал і пише в БД
├── test_homework_29.py     # 18 тестів
├── conftest.py             # фікстури: очікування БД, чиста таблиця, готовий запис
├── pytest.ini              # маркери db / app
├── requirements.txt        # psycopg2-binary, pytest
├── Dockerfile              # образ додатку з тестами
├── docker-compose.yaml     # альтернатива ручним docker run
└── core/
    ├── config.py           # параметри БД з env (DB_HOST та ін.)
    └── db.py               # підключення + CRUD
```

## Схема таблиці

```sql
CREATE TABLE calculations (
    id         SERIAL PRIMARY KEY,
    number     INTEGER      NOT NULL CHECK (number >= 0),
    operation  VARCHAR(50)  NOT NULL,
    result     NUMERIC      NOT NULL,
    created_at TIMESTAMPTZ  NOT NULL DEFAULT now()
);
```

---

## Запуск у Docker (як вимагає завдання)

### 1. Створити мережу

```bash
docker network create hw29_net
```

### 2. Підняти контейнер з Postgres

```bash
docker run -d \
  --name hw29_db \
  --network hw29_net \
  -e POSTGRES_USER=test_user \
  -e POSTGRES_PASSWORD=test_password \
  -e POSTGRES_DB=test_db \
  -p 5432:5432 \
  postgres:16
```

### 3. Зібрати образ додатку

```bash
docker build -t hw29_app .
```

### 4. Запустити тести в контейнері, підключеному до БД

```bash
docker run --rm \
  --name hw29_tests \
  --network hw29_net \
  -e DB_HOST=hw29_db \
  hw29_app
```

`DB_HOST=hw29_db` — це **ім'я контейнера з базою**. Усередині мережі Docker
воно працює як DNS-ім'я, тому додаток знаходить базу без IP-адрес.

Очікуваний результат: `18 passed`.

### 5. Запустити сам додаток (замість тестів)

```bash
docker run --rm \
  --network hw29_net \
  -e DB_HOST=hw29_db \
  hw29_app python homework_29.py
```

### 6. Перевірити дані в базі

```bash
docker exec -it hw29_db psql -U test_user -d test_db -c "SELECT * FROM calculations;"
```

### Прибрати за собою

```bash
docker rm -f hw29_db
docker network rm hw29_net
docker rmi hw29_app
```

---

## Альтернатива: Docker Compose

Те саме однією командою (`depends_on` + healthcheck самі дочекаються готовності БД):

```bash
docker compose up --build        # зібрати і прогнати тести
docker compose down -v           # зупинити і прибрати
```

---

## Запуск локально (без Docker)

Потрібен Postgres на `localhost:5432` з користувачем `test_user` / `test_password`
і базою `test_db`:

```bash
pip install -r requirements.txt
pytest
```

Параметри перевизначаються змінними оточення:
`DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`.

---

## Тести — 18 шт.

| Група | Тести | Що перевіряє |
|---|---|---|
| Підключення | `test_database_connection`, `test_table_exists` | з'єднання живе, таблиця створена |
| Вставка | `test_insert_record`, `test_insert_several_records`, `test_insert_negative_number_is_rejected` | INSERT, кілька рядків, CHECK-обмеження |
| Оновлення | `test_update_record`, `test_update_missing_record_changes_nothing` | UPDATE змінює рядок / не чіпає неіснуючий |
| Видалення | `test_delete_record`, `test_delete_missing_record_changes_nothing` | DELETE прибирає рядок / не чіпає неіснуючий |
| Вибірка | `test_select_all_returns_everything`, `test_select_from_empty_table` | SELECT усіх рядків, порожня таблиця |
| Логіка | `test_factorial` (×4), `test_factorial_of_negative_raises`, `test_app_saves_calculation_to_database`, `test_app_main_saves_all_numbers` | обчислення + збереження |

```bash
pytest -m db     # тільки робота з базою
pytest -m app    # тільки логіка додатку
```

## Скріншоти для здачі

Папка `screenshots/` — потрібні кадри:

1. `docker images` — зібраний образ `hw29_app` у списку
2. `docker ps` — запущений контейнер `hw29_db`
3. вивід `docker run ... hw29_app` з результатом `18 passed`
4. `docker exec ... psql ... SELECT * FROM calculations;` — дані в базі
