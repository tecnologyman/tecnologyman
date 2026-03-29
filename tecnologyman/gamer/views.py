from django.shortcuts import render, get_object_or_404
from .models import Game, GameStat


def gamer_home(request):
    games = Game.objects.all()
    return render(request, 'gamer/home.html', {'games': games})


def game_detail(request, slug):
    game = get_object_or_404(Game, slug=slug)
    stats = GameStat.objects.filter(game=game)

    return render(request, 'gamer/detail.html', {
        'game': game,
        'stats': stats
    })