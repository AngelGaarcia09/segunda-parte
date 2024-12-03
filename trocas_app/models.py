from django.db import models

# Create your models here.
class Troca(models.Model):
    id_troca=models.PositiveIntegerField(primary_key=True)
    año=models.PositiveIntegerField()
    modelo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    precio=models.DecimalField(max_digits=10, decimal_places=2)
    date=models.DateField()
    tipo_llantas=models.CharField(max_length=50)

    def __str__(self):
        return self.modelo