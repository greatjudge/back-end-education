from django.urls import path
from .views import index, test_list, test_detail


urlpatterns = [
    path('', index, name='index'),
    path('test/', test_list, name='test_list'),
    path('test/<slug:slug>/', test_detail, name='test_detail'),
]