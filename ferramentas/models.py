from django.db import models
from accounts.models import CustomUser
from datetime import datetime as Datetime
from datetime import datetime, time
from django.utils import timezone

def default_created_at():
    return datetime.combine(timezone.now().date(), time(8, 0))


class Formulario(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,default=1)
    nome = models.CharField(max_length=100)
    cuca = models.CharField(max_length=100)
    data_atual = models.CharField(max_length=100)
    periodo = models.CharField(max_length=100)
    atividades_realizadas = models.TextField()
    problemas_enfrentados = models.TextField()
    curiosidade_aprendizado = models.TextField()
    pontos_forts = models.TextField()
    imagem1 = models.ImageField(upload_to='images/')
    txt_img1 = models.TextField()
    imagem2 = models.ImageField(upload_to='images/')
    txt_img2 = models.TextField()
    imagem3 = models.ImageField(upload_to='images/')
    txt_img3 = models.TextField()
    imagem4 = models.ImageField(upload_to='images/')
    txt_img4 = models.TextField()
    imagem5 = models.ImageField(upload_to='images/', blank=True, null=True)
    txt_img5 = models.TextField(blank=True, null=True)
    imagem6 = models.ImageField(upload_to='images/', blank=True, null=True)
    txt_img6 = models.TextField(blank=True, null=True)
    link_relatorio = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    