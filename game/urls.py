from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.show_games),
    path('games/<int:game_id>/',
        views.show_game_detail)
]
