# Образ додатку з тестами (ДЗ 29)
FROM python:3.12-slim

# Робоча директорія всередині контейнера
WORKDIR /app

# Спершу тільки залежності — цей шар кешується і не перезбирається,
# поки requirements.txt не зміниться
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Потім код додатку
COPY . .

# За замовчуванням контейнер запускає тести
CMD ["pytest"]
