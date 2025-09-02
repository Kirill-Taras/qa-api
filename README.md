# QA API

Простой REST API для работы с вопросами и ответами.

## Стек технологий

- Python 3.13
- Django 5.2
- Django REST Framework
- PostgreSQL 15
- Docker & Docker Compose

## Установка и запуск через Docker

1. **Клонируем репозиторий:**

```bash
git clone git@github.com:Kirill-Taras/qa-api.git
cd qa-api
```

2. **Создаём .env файл**

```bash
POSTGRES_USER=***
POSTGRES_PASSWORD***
POSTGRES_DB=***
POSTGRES_HOST=***
POSTGRES_PORT=***
DEBUG=True
SECRET_KEY=django-insecure-testkey
```

3. **Собираем контейнеры**

```bash
docker-compose build
```

4. **Запускаем контейнеры**

```bash
docker-compose up -d
```

5. **Применяем миграции**

```bash
docker-compose exec web python manage.py migrate
```

6. **Создаём суперпользователя**

```bash
docker-compose exec web python manage.py createsuperuser
```

Проект доступен по адресу: http://localhost:8000

**Реализованные эндпоинты**

### 📋 Вопросы (Questions)

| Метод | URL                | Описание |
|-------|--------------------|----------|
| `GET` | `/questions/`      | Получить список всех вопросов |
| `POST` | `/questions/`      | Создать новый вопрос |
| `GET` | `/questions/{id}/` | Получить детальную информацию о вопросе с ответами |
| `DELETE` | `/questions/{id}/` | Удалить вопрос (каскадно удаляются все ответы) |

### 💬 Ответы (Answers)

| Метод | URL                | Описание |
|-------|--------------------|----------|
| `POST` | `/questions/{id}/answers/` | Добавить ответ к конкретному вопросу |
| `GET` | `/answers/{id}/`   | Получить детальную информацию об ответе |
| `DELETE` | `/answers/{id}/`   | Удалить ответ |


**Автор проекта:**
Разработчик Кирилл Тарасов