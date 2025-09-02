from django.db import models
from django.conf import settings


class Question(models.Model):
    """
    Модель вопроса.
    Каждый вопрос имеет текст и дату создания.
    """

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text[:50]  # показываем первые 50 символов


class Answer(models.Model):
    """
    Модель ответа.
    Ответ привязан к конкретному вопросу и пользователю.
    """

    question = models.ForeignKey(
        Question,
        related_name="answers",
        on_delete=models.CASCADE  # при удалении вопроса удаляются ответы
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="answers",
        on_delete=models.CASCADE  # при удалении юзера удаляются его ответы
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return f"{self.user.email}: {self.text[:30]}"  # email + первые 30 символов
