from django.contrib import admin
from .models import Traiteur

@admin.register(Traiteur)
class TraiteurAdmin(admin.ModelAdmin):
    list_display = ('nomcomplet', 'specialites', 'annees_experience', 'telephone', 'email', 'est_actif', 'date_de_creation')
    list_filter = ('est_actif', 'specialites')
    search_fields = ('nomcomplet', 'specialites', 'email')
