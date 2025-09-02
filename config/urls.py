from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # API пользователей
    path("users/", include("users.urls")),

    # API вопросов и ответов
    path("", include("questions.urls")),
]
