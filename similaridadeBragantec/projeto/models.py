from django.db import models


class Projeto(models.Model):
    codigo = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=255)
    resumo = models.CharField(max_length=8000)
    ano = models.CharField(max_length=5)
    autores = models.CharField(max_length=1000)
    orientador = models.CharField(max_length=1000)
    coorientador = models.CharField(db_column='coOrientador', max_length=100)  # Field name made lowercase.
    proj2 = models.CharField(max_length=255)
    valors = models.CharField(db_column='valorS', max_length=30)  # Field name made lowercase.

    class Meta:
        db_table = 'projeto'

    def __str__(self):
        return self.titulo
