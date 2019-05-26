from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from categories.models import Category


def show_categories(request):
    categories = Category.objects.all()
    result = render_to_string('show_categories.html', {
        'categories': categories,
    })

    return HttpResponse(result)

def show_category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    games = category.games.all

    result = render_to_string('show_category_detail.html', {
        'category': category,
        'games': games,
    })
    return HttpResponse(result)
