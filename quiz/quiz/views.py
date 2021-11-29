from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .models import Test, Question, Choice
from .serializers import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@require_GET
def index(request):
    tests = Test.objects.all()
    return render(request, 'quizz/index.html', context={'tests': tests})


class TestList(APIView):
    """
    List all tests
    """
    def get(self, request, format=None):
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestDetail(APIView):
    """
    Retrieve, update or delete a test instance.
    """
    def get_object(self, pk):
        try:
            return Test.objects.get(pk=pk)
        except Test.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        test = self.get_object(pk)
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        test = self.get_object(pk)
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuestionList(APIView):
    """
    List all questions
    """
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    """
    Retrieve, update or delete a question instance.
    """
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ChoiceList(APIView):
    """
    List all choices
    """
    def get(self, request, format=None):
        choices = Choice.objects.all()
        serializer = ChoiceSerializer(choices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChoiceDetail(APIView):
    """
    Retrieve, update or delete a choice instance.
    """
    def get_object(self, pk):
        try:
            return Choice.objects.get(pk=pk)
        except Choice.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        choice = self.get_object(pk)
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        choice = self.get_object(pk)
        serializer = ChoiceSerializer(choice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        choice = self.get_object(pk)
        choice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    """
    List all categories
    """
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """
    Retrieve, update or delete a category instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserTestList(APIView):
    """
    List all user_tests
    """
    def get(self, request, format=None):
        user_tests = UserTest.objects.all()
        serializer = UserTestSerializer(user_tests, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTestDetail(APIView):
    """
    Retrieve, update or delete a user_test instance.
    """
    def get_object(self, pk):
        try:
            return UserTest.objects.get(pk=pk)
        except UserTest.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_test = self.get_object(pk)
        serializer = UserTestSerializer(user_test)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        user_test = self.get_object(pk)
        user_test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserAnswersList(APIView):
    """
    List all user_answers
    """
    def get(self, request, format=None):
        user_answers = UserAnswers.objects.all()
        serializer = UserAnswersSerializer(user_answers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserAnswersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAnswersDetail(APIView):
    """
    Retrieve, update or delete a user_answer instance.
    """
    def get_object(self, pk):
        try:
            return UserAnswers.objects.get(pk=pk)
        except UserAnswers.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_answer = self.get_object(pk)
        serializer = UserAnswersSerializer(user_answer)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        user_answer = self.get_object(pk)
        user_answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)