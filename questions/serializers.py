from rest_framework import serializers

from users.models import User

from .models import Answer, Question


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

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Answer
        fields = ("id", "question", "user", "text", "created_at")
        read_only_fields = ["id", "question", "created_at"]

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
            raise serializers.ValidationError(
                "Ответ должен быть привязан к пользователю."
            )
        return value
