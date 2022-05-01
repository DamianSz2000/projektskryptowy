from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader, RequestContext
from django.urls import reverse
from .models import Players
from .models import Reviews
from .forms import NickNameForm
def index(request):
  return render(request, 'index.html')
def player_profile(request):
    if request.POST:
        x = request.POST['nickname'] #x is the nickname
        if(Players.objects.filter(nickname=x).exists()):
            player = Players.objects.get(nickname=x)
            player_id_1 = player.id
            reviews = Reviews.objects.filter(player_id=player_id_1)
            context = {
                'player': player,
                'reviews': reviews,
            }
            return render(request, 'player_profile.html', context)
        else:
            player = Players(nickname=x)
            player.save()
            context = {
                'player': player,
                'reviews': [],
            }
            return render(request, 'player_profile.html', context)
    else:
        return render(reverse('index'))
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
