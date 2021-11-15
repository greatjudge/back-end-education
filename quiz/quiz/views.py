from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import Test, Question, Choice


@require_GET
def index(request):
    tests = Test.objects.all()
    return render(request, 'quizz/index.html', context={'tests': tests})


@require_GET
def tests_list(request):
    tests = Test.objects.all()
    data = [{'id': test.id,
             'title': test.title}
            for test in tests]
    return JsonResponse({'tests': data})


@require_GET
def tests_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return JsonResponse({'test': test.to_json_detail()})


@require_POST
def tests_create(request):
    try:
        test = Test.objects.create(title=request.POST.get('title'),
                                   complexity=request.POST.get('complexity'),
                                   description=request.POST.get('description'))
        return JsonResponse({'status': 'ok',
                             'id': test.id})
    except TypeError:
        return JsonResponse({'status': 'error'})


def tests_delete(request):
    pass


@require_GET
def questions_list(request):
    questions = Question.objects.all()
    data = [{'id': question.id,
            'title': question.title}
            for question in questions]
    return JsonResponse({'questions': data})


@require_GET
def questions_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return JsonResponse({'test': question.to_json_detail()})


@require_POST
def questions_create(request):
    try:
        # question = Question.objects.create(title=request.POST.get('title')[0],
        #                                    order=request.POST.get('order')[0])
        return JsonResponse({'status': 'ok',
                             'id': 1})
    except TypeError as ex:
        print(ex)
        return JsonResponse({'status': 'error'})


def questions_delete(request):
    pass


@require_GET
def choices_list(request):
    choices = Choice.objects.all()
    data = [{'id': choice.id,
             'title': choice.title}
            for choice in choices]
    return JsonResponse({'questions': data})


@require_GET
def choices_detail(request, choice_id):
    choice = get_object_or_404(Choice, id=choice_id)
    return JsonResponse({'test': choice.to_json_detail()})


@require_POST
def choices_create(request):
    try:
        question = Question.objects.get(id=3)
        choice = Choice.objects.create(title=request.POST.get('title')[0],
                                       question=question)
        return JsonResponse({'status': 'ok',
                             'id': choice.id})
    except TypeError:
        return JsonResponse({'status': 'error'})


def choices_delete(request):
    pass
