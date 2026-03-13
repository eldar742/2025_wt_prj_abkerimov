from django import forms
from .models import Playlist

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'is_public'] # Uživatel zadává jen název a jestli je veřejný
        labels = {
            'name': 'Název playlistu',
            'is_public': 'Veřejný playlist (uvidí ho i ostatní)',
        }
        # Přidáme Bootstrap CSS třídy, aby to vypadalo dobře v našem tmavém vzhledu
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-dark text-light border-secondary'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input bg-dark border-secondary'}),
        }