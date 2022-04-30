from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.urls import reverse
from .models import Players
from .models import Reviews

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def player_profile(request):
    x = request.GET['nickname']
    if(Players.objects.filter(nickname=x).exists()):
        player = Players.objects.get(nickname=x)
        player_id_1 = player.id
        reviews = Reviews.objects.filter(player_id=player_id_1)
        template = loader.get_template('player_profile.html')
        context = {
            'player': player,
            'reviews': reviews,
        }
        return HttpResponse(template.render(context, request))
    else:
        player = Players(nickname=x)
        player.save()
        template = loader.get_template('viewplayer.html')
        context = {
            'player': player,
            'reviews': [],
        }
        return HttpResponse(template.render(context, request))
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
