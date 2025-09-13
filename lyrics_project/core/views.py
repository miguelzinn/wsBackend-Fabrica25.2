from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Artista, Musica
from .forms import MusicaForm

class ArtistaListView(ListView):
    model = Artista
    template_name = 'core/artista_list.html'

class ArtistaCreateView(CreateView):
    model = Artista
    fields = ['nome', 'nacionalidade']
    template_name = 'core/artista_form.html'
    success_url = reverse_lazy('artista-list')

class ArtistaUpdateView(UpdateView):
    model = Artista
    fields = ['nome', 'nacionalidade']
    template_name = 'core/artista_form.html'
    success_url = reverse_lazy('artista-list')

class ArtistaDeleteView(DeleteView):
    model = Artista
    template_name = 'core/artista_confirm_delete.html'
    success_url = reverse_lazy('artista-list')

class MusicaListView(ListView):
    model = Musica
    template_name = 'core/musica_list.html'

class MusicaCreateView(CreateView):
    model = Musica
    form_class = MusicaForm
    template_name = 'core/musica_form.html'
    success_url = reverse_lazy('musica-list')

class MusicaDetailView(DetailView):
    model = Musica
    template_name = 'core/musica_detail.html'

class MusicaUpdateView(UpdateView):
    model = Musica
    form_class = MusicaForm
    template_name = 'core/musica_form.html'
    success_url = reverse_lazy('musica-list')

class MusicaDeleteView(DeleteView):
    model = Musica
    template_name = 'core/musica_confirm_delete.html'
    success_url = reverse_lazy('musica-list')