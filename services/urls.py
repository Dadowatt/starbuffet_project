from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('traiteurs/', views.liste_traiteurs, name='liste_traiteurs'),
    path('traiteurs/<int:id>/detail/', views.detail_traiteur, name='detail_traiteur'),
    path('traiteurs/ajouter/', views.ajouter_traiteur, name='ajouter_traiteur'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
