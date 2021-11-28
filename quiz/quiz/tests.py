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

"""
test_ser = TestSerializer(data={'title': 'test 3', 'creator': 1, 'questions': [{'title': 'question 1', 'order': 1},
                                                                               {'title': 'question 2', 'order': 1}]})
{'questions': [ErrorDetail(string='Orders of questions should not be repeated', code='invalid')]}                                                                              
"""

"""
>>> from quiz.serializers import QuestionSerializer
>>> from quiz.models import Question
>>> q = Question.objects.get(id=1)
>>> q_ser = QuestionSerializer(q)
>>> data = q_ser.data
>>> data['choices'][1]['is_right'] = True
>>> data['choices'].append({'title': 'new_choice'})
>>> data['choices'].pop(2)
OrderedDict([('id', 3), ('title', 'Боромир'), ('is_right', False)])
>>> up_q_ser = QuestionSerializer(q, data)
>>> up_q_ser.is_valid()
True
>>> up_q_ser.save()
"""

"""
{'id': 1, 'choices': [OrderedDict([('id', 1), ('title', 'Эддард'), ('is_right', True)]), OrderedDict([('id', 2), ('title', 'Роберт'), ('is_right', True)]), {'title': 'new_choice'}], 'order': 1, 'title': 'Как звали главу дома Старков на момент начала книги/сериала?', 'is_active': True, 'test': 1}
"""