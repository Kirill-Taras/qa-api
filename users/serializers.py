from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации пользователей.
    """

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "email", "password")

    def create(self, validated_data):
        """
        Создаём пользователя через кастомный менеджер.
        """
        return User.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )
