from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Traiteur
from .forms import TraiteurForm

def index(request):
    return render(request, 'services/index.html')

def liste_traiteurs(request):
    traiteurs = Traiteur.objects.all()
    return render(request, 'services/liste_traiteurs.html', {'traiteurs': traiteurs})

def detail_traiteur(request, id):
    traiteur = get_object_or_404(Traiteur, id=id)
    return render(request, 'services/detail_traiteur.html', {'traiteur': traiteur})


@login_required(login_url='login')
def ajouter_traiteur(request):
    if request.method == 'POST':
        form = TraiteurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Traiteur ajouté avec succès !")
            return redirect('liste_traiteurs')
    else:
        form = TraiteurForm()
    return render(request, 'services/ajouter_traiteur.html', {'form': form})


def login_view(request):
    next_url = request.GET.get('next', 'index')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.POST.get('next') or next_url)  
        else:
            return render(request, 'registration/login.html', {
                'error': 'Nom d’utilisateur ou mot de passe incorrect',
                'next': next_url
            })

    return render(request, 'registration/login.html', {'next': next_url})


def logout_view(request):
    logout(request)
    return redirect('login')
    
