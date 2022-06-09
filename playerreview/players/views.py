from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader, RequestContext
from django.urls import reverse
from .models import Players
from .models import Reviews
import datetime
def index(request):
    players = Players.objects.all()
    #sort players by amount of reviews
    players = sorted(players, key=lambda x: x.number_of_reviews, reverse=True)
    context = {
        'players': players
    }
    return render(request, 'index.html', context)
def player_profile(request, nickname=None):
    if request.POST:
        x = request.POST['nickname']
        if(Players.objects.filter(nickname=x).exists()):
            player = Players.objects.get(nickname=x)
            reviews = Reviews.objects.filter(player=player)
            context = {
                'player': player,
                'reviews': reviews,
                'nickname': player.nickname
            }
            return redirect(reverse('player_profile', kwargs={'nickname': player.nickname}))
        else:
            player = Players(nickname=x, number_of_reviews=0)
            player.save()
            context = {
                'player': player,
                'nickname': player.nickname,
                'reviews': []
            }
            return redirect(reverse('player_profile', kwargs={'nickname': player.nickname}))

    else:
        x = nickname
        if(Players.objects.filter(nickname=x).exists()):
            player = Players.objects.get(nickname=x)
            reviews = Reviews.objects.filter(player=player)
            context = {
                'player': player,
                'reviews': reviews,
                'nickname': player.nickname
            }
            return render(request, 'player_profile.html', context)
        else:
            player = Players(nickname=x, number_of_reviews=0)
            player.save()
            context = {
                'player': player,
                'nickname': player.nickname,
                'reviews': []
            }
            return render(request, 'player_profile.html', context)
def login_form(request):
    return render(request, 'login_form.html')
def add_review(request, nickname=None):
    player = Players.objects.get(nickname=nickname)
    context = {
        'player': player,
        'nickname': player.nickname
    }
    return render(request, 'add_review.html', context)
def submit_review(request, nickname=None):
    player = Players.objects.get(nickname=nickname)
    if request.POST:
        x = request.POST['review']
        y = request.POST['screenshot']
        z = request.POST['author']
        review = Reviews(player=player, review=x, image_link=y, author = z, accepted = 0, date_of_submit = datetime.datetime.now())
        review.save()
        player.number_of_reviews += 1
        player.save()
    return redirect(reverse('player_profile', kwargs={'nickname': player.nickname}))
def admin_panel(request):
    players = Players.objects.all()
    reviews = Reviews.objects.all()
    context = {
        'players': players,
        'reviews': reviews
    }
    return render(request, 'admin_panel.html', context)
def accept_review(request, id):
    review = Reviews.objects.get(id=id)
    review.accepted = 1
    review.save()
    return redirect(reverse('admin_panel'))
def reject_review(request, id):
    review = Reviews.objects.get(id=id)
    review.delete()
    return redirect(reverse('admin_panel'))
