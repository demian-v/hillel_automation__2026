import psycopg2

# Параметри підключення
# База даних повинна існувати на зазначеному хості, та юзер повинен мати право на читання цього запису
dbname = 'shop'
user = 'demianvyrozub'
password = ''            # trust-автентифікація
host = 'localhost'
port = '5432'

connection = None

# Спроба підключитись до бази даних
try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database successfully!")

    # Для виконання запитів ви можете створити курсор
    cursor = connection.cursor()

    # Для виконання SQL запитів ви можете викликати метод execute() курсора
    # Тут можна виконати будь який запит на мові SQL, і він виконається в БД
    cursor.execute("SELECT * FROM products p JOIN categories c ON p.category_id = c.id")

    # Отримання результатів запиту
    record = cursor.fetchone()
    print(record)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # Закриваємо підключення
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")