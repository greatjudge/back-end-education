from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.id})


class Test(models.Model):
    creator = models.ForeignKey(User, verbose_name='создатель',
                                on_delete=models.CASCADE, related_name='tests')
    title = models.CharField(max_length=50, verbose_name='Название')
    categories = models.ManyToManyField(Category, related_name='tests',
                                        blank=True, verbose_name='категории теста')
    complexity = models.PositiveSmallIntegerField(blank=True,
                                                  null=True,
                                                  verbose_name='Сложность')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание теста')
    datetime = models.DateTimeField(auto_now=True,
                                    blank=True,
                                    verbose_name='дата и время создания')

    def get_absolute_url(self):
        return reverse('test_detail', kwargs={'pk': self.id})

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['-datetime']


class Question(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name='порядок вопроса в тесте')
    title = models.CharField(max_length=200, verbose_name='вопрос')
    test = models.ForeignKey(Test, related_name='questions',
                             on_delete=models.CASCADE, verbose_name='тест')
    is_active = models.BooleanField(blank=True, default=True)
    # question_type

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Вопрос в тесте'
        verbose_name_plural = 'Вопросы в тесте'
        ordering = ('order',)
        unique_together = ['test', 'order']


class Choice(models.Model):
    title = models.CharField(max_length=100, verbose_name='содержание')
    question = models.ForeignKey(Question, related_name='choices',
                                 on_delete=models.CASCADE, verbose_name='вопрос')
    is_right = models.BooleanField(blank=True,
                                   default=False,
                                   verbose_name='правильный ответ')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('choice_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'


class UserTest(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь',
                             on_delete=models.CASCADE, related_name='passed_tests')
    test = models.ForeignKey(Test, related_name='grades',
                             on_delete=models.CASCADE, verbose_name='тест')
    grade = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True,
                                    verbose_name='время и дата прохождения теста')

    def __str__(self):
        return str(self.test)

    def get_absolute_url(self):
        return reverse('user_test_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Пройденный тест'
        verbose_name_plural = 'Пройденные тесты'


class UserAnswers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='answers', verbose_name='пользователь')
    question = models.ForeignKey(Question, related_name='users_answer',
                                 on_delete=models.CASCADE, verbose_name='вопрос')
    choice = models.ForeignKey(Choice, related_name='users_answer',
                               on_delete=models.CASCADE, verbose_name='вариант ответа')
    user_test = models.ForeignKey(UserTest, related_name='answers',
                                  on_delete=models.CASCADE, verbose_name='пройденный тест')

    def __str__(self):
        return str(self.choice)

    def get_absolute_url(self):
        return reverse('user_answer_detail', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Ответ пользователя на вопрос'
        verbose_name_plural = 'Ответы пользователя на вопросы'
