from django.contrib import admin
from .models import Test, Question, Choice


class TestAdmin(admin.ModelAdmin):
    # Кастомизируем отображение модели в админке
    list_display = ('id', 'title')
    # list_filter =


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'order', 'title')
    list_filter = ('test',)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('question',)


# Register your models here.

# Подключаем модель к админке
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
