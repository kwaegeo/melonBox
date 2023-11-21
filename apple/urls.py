from django.urls import path

from . import views
app_name = 'apple'

urlpatterns = [
    path('', views.index),
]