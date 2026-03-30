from django.urls import path
from . import views

urlpatterns = [
    path('traiteurs/', views.liste_traiteurs, name='liste_traiteurs'),
]
