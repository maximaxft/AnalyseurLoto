from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index2/', views.index2, name='index2'),
    path('compute1/', views.compute1, name='compute1'),
    path('compute2/', views.compute2, name='compute2')
]