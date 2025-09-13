from django import forms
from .models import Musica
import certifi
class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = ['titulo', 'artista']

    def save(self, commit=True):
        musica = super().save(commit=False)
        import requests
        response = requests.get(f"https://api.lyrics.ovh/v1/{musica.artista.nome}/{musica.titulo}",verify=certifi.where())
        if response.status_code == 200:
            musica.letra = response.json().get('lyrics', 'Letra não encontrada.')
        else:
            musica.letra = 'Letra não encontrada.'
        if commit:
            musica.save()
        return musica