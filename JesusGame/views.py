from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from game.models import Game


def show_main_page(request):
    games = Game.objects.order_by('-id')[:5]

    result = render_to_string('index.html', {
        'games': games,
    })

    return HttpResponse(result)
