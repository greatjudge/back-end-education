from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', index, name='index'),

    path('tests/', TestList.as_view(), name='test_list'),
    path('tests/<int:pk>/', TestDetail.as_view(), name='test_detail'),

    path('questions/', QuestionList.as_view(), name='question_list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question_detail'),

    path('choices/', ChoiceList.as_view(), name='choice_list'),
    path('choices/<int:pk>/', ChoiceDetail.as_view(), name='choice_detail'),

    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),

    path('user_tests/', UserTestList.as_view(), name='user_test_list'),
    path('user_tests/<int:pk>/', UserTestDetail.as_view(), name='user_test_detail'),

    path('user_answers/', UserAnswersList.as_view(), name='user_answer_list'),
    path('user_answers/<int:pk>/', UserAnswersDetail.as_view(), name='user_answer_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
