from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Test, Question, Choice, Category, UserAnswers, UserTest


User = get_user_model()


@admin.register(User)
class TestUser(admin.ModelAdmin):
    list_display = ('id', 'username')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    # Кастомизируем отображение модели в админке
    list_display = ('id', 'title')
    list_filter = ('categories',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'order', 'title')
    list_filter = ('test',)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_right')
    list_filter = ('question',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(UserAnswers)
class UserAnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'choice')


@admin.register(UserTest)
class UserTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'test', 'grade')
