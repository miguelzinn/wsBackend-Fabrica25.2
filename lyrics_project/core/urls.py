from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArtistaListView.as_view(), name='home'),
    path('artistas/', views.ArtistaListView.as_view(), name='artista-list'),
    path('artistas/novo/', views.ArtistaCreateView.as_view(), name='artista-create'),
    path('artistas/<int:pk>/editar/', views.ArtistaUpdateView.as_view(), name='artista-update'),
    path('artistas/<int:pk>/deletar/', views.ArtistaDeleteView.as_view(), name='artista-delete'),

    path('musicas/', views.MusicaListView.as_view(), name='musica-list'),
    path('musicas/nova/', views.MusicaCreateView.as_view(), name='musica-create'),
    path('musicas/<int:pk>/', views.MusicaDetailView.as_view(), name='musica-detail'),
    path('musicas/<int:pk>/editar/', views.MusicaUpdateView.as_view(), name='musica-update'),
    path('musicas/<int:pk>/deletar/', views.MusicaDeleteView.as_view(), name='musica-delete'),
]