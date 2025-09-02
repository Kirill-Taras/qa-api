from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вопросов.
    """

    class Meta:
        model = Question
        fields = ("id", "text", "created_at")

    def validate_text(self, value):
        """
        Проверяем, что текст вопроса не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Текст вопроса не может быть пустым.")
        return value


class AnswerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для ответов.
    """

    class Meta:
        model = Answer
        fields = ("id", "question", "user", "text", "created_at")

    def validate_text(self, value):
        """
        Проверяем, что текст ответа не пустой.
        """
        if not value.strip():
            raise serializers.ValidationError("Текст ответа не может быть пустым.")
        return value

    def validate_user(self, value):
        """
        Проверяем, что user не пустой.
        """
        if value is None:
            raise serializers.ValidationError("Ответ должен быть привязан к пользователю.")
        return value

