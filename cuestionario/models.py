from django.db import models
from ajustes_servidor.models import usuario
#
from ckeditor.fields import RichTextField
# Create your models here.
class Cuestionario(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = RichTextField()
    profesor = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='cuestionarios', related_query_name="RELACION_FK_%(app_label)s_%(class)s")
    fecha_ingreso = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
