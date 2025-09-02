# Используем официальный Python образ
FROM python:3.13-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Экспортируем переменные окружения
ENV PYTHONUNBUFFERED=1

# Команда запуска Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
