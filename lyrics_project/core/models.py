from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    letra = models.TextField(blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.artista.nome}"