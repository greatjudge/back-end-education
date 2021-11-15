from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Test(models.Model):
    # creator = models.ForeignKey(User, verbose_name='создатель',
    #                             on_delete=models.SET_NULL, related_name='answers')
    title = models.CharField(max_length=50, verbose_name='Название')
    categories = models.ManyToManyField(Category, related_name='tests',
                                        verbose_name='категории теста')
    complexity = models.PositiveSmallIntegerField(blank=True, null=True,
                                                  verbose_name='Сложность')
    description = models.TextField(blank=True, null=True,
                                   verbose_name='Описание теста')
    datetime = models.DateTimeField(auto_now=True, blank=True,
                                    verbose_name='дата и время создания')

    def get_absolute_url(self):
        return reverse('tests_detail', kwargs={'test_id': self.id})

    def to_json_detail(self):
        return {'id': self.id,
                'title': self.title,
                'complexity': self.complexity,
                'description': self.description,
                'datetime': self.datetime,
                'categories': [cat.title for cat in self.categories.all()],
                'questions': [question.to_json_detail() for question in self.questions.all()]}

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    order = models.PositiveSmallIntegerField(verbose_name='порядок вопроса в тесте')
    title = models.CharField(max_length=200, verbose_name='вопрос')
    test = models.ForeignKey(Test, related_name='questions',
                             on_delete=models.CASCADE, verbose_name='тест')
    is_active = models.BooleanField(blank=True, default=True)
    # question_type

    def __str__(self):
        return self.title

    def to_json_detail(self):
        return {'id': self.id,
                'title': self.title,
                'order': self.order,
                'test': self.test.id,
                'is_active': self.is_active,
                'choices': [choice.to_json_detail() for choice in self.choices.all()]}

    class Meta:
        verbose_name = 'Вопрос в тесте'
        verbose_name_plural = 'Вопросы в тесте'
        ordering = ('order',)
        unique_together = ['test', 'order']


class Choice(models.Model):
    title = models.CharField(max_length=100, verbose_name='содержание')
    question = models.ForeignKey(Question, related_name='choices', default=5,
                                 on_delete=models.CASCADE, verbose_name='вариант ответа')
    is_right = models.BooleanField(blank=True, default=False,
                                   verbose_name='правильный ответ')

    def __str__(self):
        return self.title

    def to_json_detail(self):
        return {'id': self.id,
                'title': self.title,
                'question': self.question.id,
                'is_right': self.is_right}

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответов'


class UserAnswers(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE,
    #                          related_name='answers', verbose_name='пользователь')
    question = models.ForeignKey(Question, related_name='users_answer',
                                 on_delete=models.CASCADE, verbose_name='вопрос')
    choice_id = models.ForeignKey(Choice, related_name='users_answer',
                                  on_delete=models.CASCADE, verbose_name='вариант ответа')
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ответ пользователя на вопрос'
        verbose_name_plural = 'Ответы пользователя на вопросы'


class UserTest(models.Model):
    # user = models.ForeignKey(User, verbose_name='пользователь',
    #                             on_delete=models.CASCADE, related_name='passed_tests')
    test = models.ForeignKey(Test, related_name='grades',
                             on_delete=models.CASCADE, verbose_name='тест')
    grade = models.FloatField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.test)

    class Meta:
        verbose_name = 'Пройденный тест'
        verbose_name_plural = 'Пройденные тесты'


