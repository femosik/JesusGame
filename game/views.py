from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from game.models import Game


def show_games(request):
    games = Game.objects.all()
    result = render_to_string('show_games.html',{
        'games': games,
    })

    return HttpResponse(result)

def show_game_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    result = render_to_string('show_game_detail.html', {
        'game': game,
        'reviews': game.reviews.all()
    })

    return HttpResponse(result)
