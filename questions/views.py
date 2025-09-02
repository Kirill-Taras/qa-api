from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    CRUD для вопросов.
    GET/POST/PUT/DELETE /api/questions/
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """
    CRUD для ответов.
    GET/POST/PUT/DELETE /api/answers/
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
