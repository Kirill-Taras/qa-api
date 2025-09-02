import pytest
from rest_framework import status
from rest_framework.test import APIClient

from users.models import User

from .models import Answer, Question


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def question():
    return Question.objects.create(text="Тестовый вопрос")


@pytest.fixture
def user():
    return User.objects.create_user(email="testuser@test.com", password="password123")


@pytest.mark.django_db
def test_create_question(api_client):
    """Тест создания вопроса"""
    url = "/questions/"
    data = {"text": "Новый вопрос"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Question.objects.filter(text="Новый вопрос").exists()


@pytest.mark.django_db
def test_add_answer(api_client, question, user):
    """Тест добавления ответа"""
    url = f"/questions/{question.id}/answers/"
    data = {"user": user.id, "text": "Ответ на вопрос"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    answer = Answer.objects.get(text="Ответ на вопрос")
    assert answer.question == question
    assert answer.user.id == user.id


@pytest.mark.django_db
def test_add_answer_to_nonexistent_question(api_client, user):
    """Тест добавления ответа к несуществующему вопросу"""
    url = "/questions/999/answers/"
    data = {"user": user.id, "text": "Ответ"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_cascade_delete(api_client, question, user):
    """Тест каскадного удаления"""
    # создаём несколько ответов
    Answer.objects.create(question=question, user=user, text="Ответ 1")
    Answer.objects.create(question=question, user=user, text="Ответ 2")
    assert Answer.objects.filter(question=question).count() == 2

    # удаляем вопрос
    url = f"/questions/{question.id}/"
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    # проверяем, что ответы удалились каскадно
    assert Answer.objects.filter(question=question).count() == 0


@pytest.mark.django_db
def test_multiple_answers_same_user(api_client, question, user):
    """Тест: один пользователь может оставлять несколько ответов"""
    url = f"/questions/{question.id}/answers/"
    data1 = {"user": user.id, "text": "Ответ 1"}
    data2 = {"user": user.id, "text": "Ответ 2"}
    api_client.post(url, data1, format="json")
    api_client.post(url, data2, format="json")
    assert Answer.objects.filter(question=question, user=user).count() == 2
