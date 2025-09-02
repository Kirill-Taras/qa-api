from typing import Any

from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from .models import Answer, Question
from .serializers import AnswerSerializer, QuestionSerializer


class QuestionListCreateView(generics.ListCreateAPIView):
    """GET: список вопросов, POST: создать вопрос"""

    queryset = Question.objects.all().order_by("-created_at")
    serializer_class: type = QuestionSerializer


class QuestionDetailView(generics.RetrieveDestroyAPIView):
    """GET: получить вопрос с ответами, DELETE: удалить вопрос"""

    queryset = Question.objects.all()
    serializer_class: type = QuestionSerializer

    def retrieve(self, request, *args: Any, **kwargs: Any) -> Response:
        """Добавляем ответы в вывод"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        answers = Answer.objects.filter(question=instance).order_by("-created_at")
        answers_serializer = AnswerSerializer(answers, many=True)
        data: dict[str, Any] = serializer.data
        data["answers"] = answers_serializer.data
        return Response(data)


class AnswerCreateView(generics.CreateAPIView):
    """POST: добавить ответ к вопросу"""

    serializer_class: type = AnswerSerializer

    def perform_create(self, serializer)-> None:
        question = get_object_or_404(Question, pk=self.kwargs.get("pk"))
        serializer.save(question=question)


class AnswerDetailView(generics.RetrieveDestroyAPIView):
    """GET: получить ответ, DELETE: удалить ответ"""

    queryset = Answer.objects.all()
    serializer_class: type = AnswerSerializer
