from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player_profile/<str:nickname>', views.player_profile, name='player_profile'),
    # path('viewplayer/', views.viewplayer, name='viewplayer'),
    # path('viewplayer/addreview/', views.addreview, name='addreview'),
]