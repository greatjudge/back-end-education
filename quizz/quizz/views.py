from django.shortcuts import render
from .models import Test


def index(request):
    tests = Test.objects.all()
    return render(request, 'quizz/index.html', context={'tests': tests})


def test_list(request):
    if request.method == 'GET':
        tests = Test.objects.all()
        return render(request, 'quizz/test_list.html', context={'tests': tests})


def  test_detail(request, slug):
    if request.method == 'GET':
        try:
            test = Test.objects.get(slug__iexact=slug)
            return render(request, 'quizz/test_detail.html',
                          context={'test': test})
        except ValueError:
            pass


def assignment_create(request):
    pass
