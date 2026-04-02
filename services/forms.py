from django import forms
from .models import Traiteur
class TraiteurForm(forms.ModelForm):
    class Meta:
        model = Traiteur
        fields = [
            'nomcomplet',
            'specialites',
            'description',
            'adresse',
            'email',
            'telephone',
            'annees_experience',
            'image',
            'langues'
        ]
        widgets = {
            'nomcomplet': forms.TextInput(attrs={'placeholder': 'Binta Diop'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Bintadmin@gmail.com'}),
            'specialites': forms.TextInput(attrs={'placeholder': 'Cuisine française, Buffet'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Parlez-nous de vos services…'}),
            'adresse': forms.TextInput(attrs={'placeholder': '123 Rue Exemple, Dakar'}),
            'telephone': forms.TextInput(attrs={'placeholder': '+221 77 123 45 67'}),
            'annees_experience': forms.NumberInput(attrs={'placeholder': '5'}),
            'image': forms.ClearableFileInput(),
            'langues': forms.TextInput(attrs={'placeholder': 'Français, Anglais, Arabe...'}),
        }



