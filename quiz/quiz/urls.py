from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('tests/list/', tests_list, name='tests_list'),
    path('tests/create/', tests_create, name='tests_create'),
    path('tests/<int:test_id>/detail/', tests_detail, name='tests_detail'),
    path('tests/<int:test_id>/delete/', tests_delete, name='tests_delete'),

    path('questions/list/', questions_list, name='questions_list'),
    path('questions/create/', questions_create, name='questions_create'),
    path('questions/<int:question_id>/detail/', questions_detail, name='questions_detail'),
    path('questions/<int:question_id>/delete/', questions_delete, name='questions_delete'),

    path('choices/list/', choices_list, name='choices_list'),
    path('choices/create/', choices_create, name='choices_create'),
    path('choices/<int:choice_id>/detail/', choices_detail, name='choices_detail'),
    path('choices/<int:choice_id>/delete/', choices_delete, name='choices_delete'),
]
