from django.urls import path

from news import views

urlpatterns = [
    path('', views.news_index, name='news_index'),
]