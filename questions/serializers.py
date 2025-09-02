from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вопросов.
    """

    class Meta:
        model = Question
        fields = ("id", "text", "created_at")


class AnswerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для ответов.
    """

    class Meta:
        model = Answer
        fields = ("id", "question", "user", "text", "created_at")
