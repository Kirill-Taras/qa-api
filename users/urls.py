from django.urls import path
from .views import UserRegistrationView

urlpatterns = [
    # Регистрация: POST {"email": "...", "password": "..."}
    path("register/", UserRegistrationView.as_view(), name="register"),
]
