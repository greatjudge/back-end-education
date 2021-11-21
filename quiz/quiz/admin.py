from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Test, Question, Choice, Category


User = get_user_model()


class TestUser(admin.ModelAdmin):
    list_display = ('id', 'username')


class TestAdmin(admin.ModelAdmin):
    # Кастомизируем отображение модели в админке
    list_display = ('id', 'title')
    list_filter = ('categories',)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'order', 'title')
    list_filter = ('test',)


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_right')
    list_filter = ('question',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


# Register your models here.

# Подключаем модель к админке
admin.site.register(User, TestUser)
admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Category, CategoryAdmin)
