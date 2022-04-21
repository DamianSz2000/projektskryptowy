from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('viewplayer/', views.viewplayer, name='viewplayer'),
    path('viewplayer/addreview/', views.addreview, name='addreview'),
]