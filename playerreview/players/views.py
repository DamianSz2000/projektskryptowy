from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader, RequestContext
from django.urls import reverse
from .models import Players
from .models import Reviews
def index(request):
  return render(request, 'index.html')
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
# def addreview(request):
#     x = request.GET['nickname']
#     player = Players.objects.get(nickname=x)
#     player.number_of_reviews += 1
#     player.save()
#     player_id_1 = player.id
#     review = request.GET['review']
#     author = request.GET['author']
#     new_review = Reviews(player_id=player_id_1, review=review, author=author, accepted=False)
#     new_review.save()
#     return HttpResponseRedirect(reverse('index'))
