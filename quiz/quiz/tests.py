from django.test import TestCase
from quiz.serializers import TestSerializer, QuestionSerializer, ChoiceSerializer
from quiz.models import Test, Question, Choice
# Create your tests here.
"""
>>> from quiz.serializers import TestSerializer
>>> test_ser = TestSerializer(data={'title': 'kkl', 'creator': 1})
>>> test_ser = TestSerializer(data={'title': 'wrong_test', 'creator': 1, 'questions': [{'title': 'wrong question'}]})
>>> test_ser.is_valid()
True
>>> test_ser.save()
"""
