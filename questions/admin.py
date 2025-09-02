from django.contrib import admin

from .models import Answer, Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "created_at")
    list_filter = ("created_at",)
    search_fields = ("text",)
    ordering = ("-created_at",)
    verbose_name = "Вопрос"
    verbose_name_plural = "Вопросы"


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "question", "user", "text", "created_at")
    list_filter = ("created_at",)
    search_fields = ("text", "user__email")
    ordering = ("-created_at",)
    verbose_name = "Ответ"
    verbose_name_plural = "Ответы"
