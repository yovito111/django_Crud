from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, verbose_name="Imagen")
    categoría = models.CharField(max_length=50, verbose_name="categoria")
    codigo = models.CharField(max_length=50, unique=True, verbose_name="código")
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    descripcion = models.TextField(null=True, verbose_name="Descripción")
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        fila = " Nombre:  " + self.nombre + " --- " + " Descripción:  " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
