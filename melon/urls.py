from django.urls import path

from . import views

app_name = 'melon'

urlpatterns = [
    path('', views.index),
    path('get_melon_play_list/', views.get_melon_play_list),  # 1. 멜론 플레이 리스트 조회
]