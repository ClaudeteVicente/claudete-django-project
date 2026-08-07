from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Linguagem (models.Model):
   nome = models.CharField(max_length = 200)
   introducao = models.TextField()
   potencias = models.TextField()
   impactos = models.TextField()
   def __str__(self):
     return self.nome

PROVINCIA_CHOICES =[
 ('MAP','Maputo Cidade'),
 ('MPA','Maputo Provincia'),
 ('GAZ','Gaza'),
 ('INH','Inhambane'),
 ('SOF','Sofala'),
 ('MAN','Manica'),
 ('TET','Tete'),
 ('ZAM','Zambezia'),
 ('NMP','Nampula'),
 ('CAB', 'Cabo Delgado'),
 ('NIA','Niassa')
    ]

class Crianca(models.Model):
    nome = models.CharField(max_length = 200)
    idade = models.IntegerField(
        validators=[MinValueValidator(10),MaxValueValidator(17)]
    )
    provincia = models.CharField(max_length = 3,choices=PROVINCIA_CHOICES)
    localidade = models.CharField(max_length = 200)
    finalidade = models.CharField(max_length = 200)
    linguagem = models.ForeignKey(Linguagem,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.nome

RESPOSTA_CHOICES=[
 ('A','Opcao A'),
 ('B','Opcao B'),
 ('C','Opcao C'),
 ('D','Opcao D'),
    ]

class Exercicio(models.Model):
    linguagem = models.ForeignKey(Linguagem,on_delete=models.CASCADE)
    enuncaido = models.TextField()
    opcao_a = models.CharField(max_length= 200)
    opcao_b = models.CharField(max_length= 200)
    opcao_c = models.CharField(max_length= 200)
    opcao_d = models.CharField(max_length= 200)
    def __str__(self):
        return self.enuncaido

    resposta_correta = models.CharField(max_length= 4,choices=RESPOSTA_CHOICES)