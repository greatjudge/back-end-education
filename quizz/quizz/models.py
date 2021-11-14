from django.db import models
from django.urls import reverse


# class Category(models.Model):


class Test(models.Model):
    # creator = on delete set null
    title = models.CharField(max_length=50, verbose_name='Название')
    complexity = models.PositiveSmallIntegerField(blank=True, null=True,
                                                  verbose_name='Сложность')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание теста')
    datetime = models.DateTimeField(auto_now=True, blank=True)

    def get_absolute_url(self):
        return reverse('tests_detail', kwargs={'test_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class GradedTest(models.Model):
    # student = models.ForeignKey()
    test = models.ForeignKey(Test, related_name='grades',
                             on_delete=models.CASCADE, verbose_name='тест')
    # user_answers = models.ManyToManyField(Choice, on_delete=models.CASCADE,
    #                                       verbose_name='ответы пользователя')
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
    # COMING SOON question_type

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос в тесте'
        verbose_name_plural = 'Вопросы в тесте'
        ordering = ('order',)
        unique_together = ['test', 'order']
