from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Traiteur
from .forms import TraiteurForm

def index(request):
    return render(request, 'services/index.html')


def liste_traiteurs(request):
    traiteurs = Traiteur.objects.filter(est_actif=True)
    for t in traiteurs:
        t.specialites_list = [sp.strip() for sp in t.specialites.split(",")]
    return render(request, 'services/liste_traiteurs.html', {'traiteurs': traiteurs})


def detail_traiteur(request, id):
    traiteur = get_object_or_404(Traiteur, id=id)
    langues_list = [l.strip() for l in traiteur.langues.split(",")]
    specialites_list = [sp.strip() for sp in traiteur.specialites.split(",")]
    return render(request, 'services/detail_traiteur.html', {
        'traiteur': traiteur,
        'langues_list': langues_list,
        'specialites_list': specialites_list
        })
    

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


    
