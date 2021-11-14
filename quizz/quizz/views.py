from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import Test, Question, Choice, GradedTest


@require_GET
def index(request):
    tests = Test.objects.all()
    return render(request, 'quizz/index.html', context={'tests': tests})


@require_GET
def tests_list(request):
    tests = Test.objects.all()
    data = [
            {
             'id': test.id,
             'title': test.title,
             'datetime': test.datetime,
            } for test in tests]
    return JsonResponse({'tests': data})


@require_GET
def tests_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = [
                 {'id': question.id,
                  'question': question.title,
                  'order': question.order,
                  'choices': [{'id': choice.id,
                               'title': choice.title} for choice in question.choices.all()],
                  'answer': {'id': question.answer.id,
                             'title': question.answer.title}}
                 for question in test.questions.all()]
    data = [
        {
            'id': test.id,
            'title': test.title,
            'description': test.description,
            'datetime': test.datetime,
            'questions': questions,
        }
    ]
    return JsonResponse({'test': data})


@require_POST
def tests_create(request):
    pass


@require_GET
def tests_delete(request):
    pass


@require_GET
def questions_list(request):
    questions = Question.objects.all()
    data = [
        {
            'id': question.id,
            'title': question.title,
        } for question in questions]
    return JsonResponse({'questions': data})


@require_GET
def questions_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choices = [{'id': choice.id} for choice in question.choices.all()]
    data = [
        {
            'id': question.id,
            'title': question.title,
            'test': question.test.id,
            'order': question.order,
            'choices': choices,
        }
    ]
    return JsonResponse({'test': data})


@require_POST
def questions_create(request):
    pass


def questions_delete(request):
    pass


@require_GET
def choices_list(request):
    choices = Choice.objects.all()
    data = [
        {
            'id': choice.id,
            'title': choice.title,
        } for choice in choices]
    return JsonResponse({'questions': data})


@require_GET
def choices_detail(request, choice_id):
    choice = get_object_or_404(Choice, id=choice_id)
    questions = [{'id': question.id} for question in choice.questions.all()]
    data = [
        {
            'id': choice.id,
            'title': choice.title,
            'questions': questions,
        }
    ]
    return JsonResponse({'test': data})


def choices_create(request):
    pass


def choices_delete(request):
    pass


@require_GET
def gradedtests_list(request):
    gdtests = Choice.objects.all()
    data = [
        {
            'id': gdtest.id,
            'test_id': gdtest.test.id,
            'test_title': gdtest.test.title,
        } for gdtest in gdtests]
    return JsonResponse({'questions': data})


@require_GET
def gradedtests_detail(request, gdtest_id):
    gdtest = get_object_or_404(GradedTest, id=gdtest_id)
    data = [
        {
            'id': gdtest.id,
            'test_id': gdtest.test.id,
            'test_title': gdtest.test.title,
            'grade': gdtest.grade,
            'datetime': gdtest.datetime
        }
    ]
    return JsonResponse({'test': data})


def gradedtests_create(request):
    pass


def gradedtests_delete(request):
    pass






