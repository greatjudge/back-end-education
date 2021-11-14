from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Test(models.Model):
    # creator = models.ForeignKey(User, verbose_name='создатель',
    #                             on_delete=models.SET_NULL, related_name='answers')
    title = models.CharField(max_length=50, verbose_name='Название')
    category = models.ManyToManyField(Category, related_name='tests',
                                      verbose_name='категории теста')
    complexity = models.PositiveSmallIntegerField(blank=True, null=True,
                                                  verbose_name='Сложность')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание теста')
    datetime = models.DateTimeField(auto_now=True, blank=True,
                                    verbose_name='дата и время создания')

    def get_absolute_url(self):
        return reverse('tests_detail', kwargs={'test_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class GradedTest(models.Model):
    # student = models.ForeignKey(User, verbose_name='пользователь',
    #                             on_delete=models.CASCADE, related_name='answers')
    test = models.ForeignKey(Test, related_name='grades',
                             on_delete=models.CASCADE, verbose_name='тест')
    grade = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.test)

    class Meta:
        verbose_name = 'Пройденный тест'
        verbose_name_plural = 'Пройденные тесты'


class Choice(models.Model):
    title = models.CharField(max_length=100, verbose_name='содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'


class Question(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name='порядок вопроса в тесте')
    title = models.CharField(max_length=200, verbose_name='вопрос')
    choices = models.ManyToManyField(Choice, verbose_name='варианты ответов',
                                     related_name='questions')
    answer = models.ForeignKey(Choice, related_name='question',
                               on_delete=models.CASCADE, blank=True,
                               verbose_name='ответ')
    test = models.ForeignKey(Test, related_name='questions',
                             on_delete=models.CASCADE, verbose_name='тест')
    # question_type

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос в тесте'
        verbose_name_plural = 'Вопросы в тесте'
        ordering = ('order',)
        unique_together = ['test', 'order']
