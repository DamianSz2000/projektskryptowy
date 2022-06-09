from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player_profile/<str:nickname>', views.player_profile, name='player_profile'),
    path('player_profile/', views.player_profile, name='player_profile'),
    path('login_form/', views.login_form, name='login_form'),
    path('add_review/<str:nickname>', views.add_review, name='add_review'),
    path('submit_review/<str:nickname>', views.submit_review, name='submit_review'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('accept_review/<int:id>', views.accept_review, name='accept_review'),
    path('reject_review/<int:id>', views.reject_review, name='reject_review'),
    # path('viewplayer/', views.viewplayer, name='viewplayer'),
    # path('viewplayer/addreview/', views.addreview, name='addreview'),
]