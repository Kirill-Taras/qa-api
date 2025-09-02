from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """
    Кастомный менеджер пользователей.
    Управляет созданием обычных юзеров и суперпользователей.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Внутренний метод: создаёт и сохраняет пользователя с email и паролем.
        """
        if not email:
            raise ValueError("Email обязателен для регистрации")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # хэшируем пароль
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Создаёт обычного пользователя.
        По умолчанию без прав администратора.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Создаёт суперпользователя (админ).
        Обязательно с правами staff и superuser.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    Кастомная модель пользователя.
    Вместо username используем email.
    """

    username = None  # убираем стандартное поле username
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"  # поле для авторизации
    REQUIRED_FIELDS = []  # дополнительные обязательные поля (пусто)

    objects = UserManager()

    def __str__(self):
        return self.email
