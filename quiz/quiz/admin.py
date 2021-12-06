from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Test, Question, Choice, Category, UserAnswers, UserTest


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    # Кастомизируем отображение модели в админке
    list_display = ('id', 'title', 'creator')
    list_filter = ('categories',)
    search_fields = ('title', 'creator__username')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'test', 'order', 'title')
    list_filter = ('test',)
    search_fields = ('title', 'test__title')


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_right')
    list_filter = ('question',)
    search_fields = ('title', 'question_title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(UserAnswers)
class UserAnswersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question', 'choice')
    search_fields = ('user__name', 'question__title', 'choice__title')


@admin.register(UserTest)
class UserTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'test', 'grade')
    search_fields = ('user__name', 'test_title')
