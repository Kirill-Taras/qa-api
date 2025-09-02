from rest_framework import generics

from .models import User
from .serializers import UserRegistrationSerializer


class UserRegistrationView(generics.CreateAPIView):
    """
    Эндпоинт для регистрации нового пользователя.
    POST /api/users/register/
    """

    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
