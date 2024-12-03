from django.db import models

# Create your models here.
class Ventas(models.Model):
    id_venta=models.PositiveIntegerField(primary_key=True)
    id_cliente=models.PositiveIntegerField()
    id_trabajador=models.PositiveIntegerField()
    id_troca=models.PositiveIntegerField()
    cantidad=models.PositiveIntegerField()
    fecha_venta=models.DateField(null=False,blank=False)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.id_venta