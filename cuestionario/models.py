from django.db import models
from ajustes_servidor.models import usuario
#
from ckeditor.fields import RichTextField
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
# Modelo relacionados       #
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
from .models_secundarios import Tags

#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
# Modelo cuestionario       #
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
class Cuestionario(models.Model):
    # ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○#
    #         Niveles de dificultad
    dificultad = (

        ('Nivel 1', (
            ('Facil', 'Facil'),
        )),
        ('Nivel 2', (
            ('Normal', 'Normal'),
        )),
        ('Nivel 3', (
            ('Intermedio', 'Intermedio'),
        )),
        ('Nivel 4', (
            ('Avanzado', 'Avanzado'),
        )),
        ('Nivel 5', (
            ('Expertiz', 'Expertiz'),
        )),

        ('Sin nivel', 'Sin nivel'),
    )

    titulo = models.CharField(max_length=255, unique=True)
    descripcion = RichTextField()
    # Relaciones llaves foreneas
    profesor = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='cuestionarios', related_query_name="RELACION_FK_%(app_label)s_%(class)s")
    # Relaciones muchos a muchos
    preguntas = models.ManyToManyField("Pregunta", help_text="Preguntas", blank=True, verbose_name="Pregunta",
                                    related_name="RELACION_%(app_label)s_%(class)s", related_query_name="RELACION_MM_%(app_label)s_%(class)s")
    
    tag =  models.ManyToManyField(Tags, help_text="Tags", verbose_name="Tag",
                                     related_name="RELACION_CUESTIONARIO_TAGS", related_query_name="RELACION_MM_CUESTIONARIO_TAGS", through='cuestionario_tag', blank=True)
    # Campos date time
    fecha_ingreso = models.DateTimeField(auto_now=True)
    # Dificultad
    dificultad = models.CharField(max_length=300, blank=True, choices=(dificultad), default="Facil")
    imagen = models.URLField(blank=True, null=True, default="https://via.placeholder.com/150")

    class Meta:
        ordering = ["-id"]

        verbose_name = "Cuestionario"

        verbose_name_plural = "Cuestionarios"

        db_table = "Cuestionario"
    
    def __str__(self):
        return self.titulo
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
# Modelo pregunta       #
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
class Pregunta(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    texto = RichTextField()
    opciones = models.ManyToManyField("Opcion", help_text="Opciones", blank=True, verbose_name="Opcion",
                                    related_name="RELACION_%(app_label)s_%(class)s", related_query_name="RELACION_MM_%(app_label)s_%(class)s")
    def __str__(self):
        return self.texto
    class Meta:
        ordering = ["-id"]

        verbose_name = "Pregunta"

        verbose_name_plural = "Preguntas"

        db_table = "Pregunta"
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
# Modelo Opcion       #
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
class Opcion(models.Model):
    texto = models.TextField()
    es_correcta = models.BooleanField(default=False)
    class Meta:
        ordering = ["-id"]

        verbose_name = "Opcion"

        verbose_name_plural = "Opciones"

        db_table = "Opcion"
    def __str__(self):
        return self.texto
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
# Modelo Respuesta          #
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
class Respuesta(models.Model):
    estudiante = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='respuestas')
    opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE, related_name='respuestas')
    fecha_respuesta = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-id"]

        verbose_name = "Respuesta"

        verbose_name_plural = "Respuestas"

        db_table = "Respuesta"
    def __str__(self):
        return f"Respuesta de {self.estudiante} a la pregunta {self.opcion.texto}"
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
# Modelo Resultado       #
#♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣#
class Resultado(models.Model):
    estudiante = models.ForeignKey(usuario, on_delete=models.CASCADE, related_name='resultados')
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE, related_name='resultados')
    puntaje = models.IntegerField()
    fecha_completado = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-id"]

        verbose_name = "Resultado"

        verbose_name_plural = "Resultados"

        db_table = "Resultado"
    def __str__(self):
        return f"Resultado de {self.estudiante} en {self.cuestionario} con puntaje {self.puntaje}"
    
# ••••••••••• CUESTIONARIO - TAG ••••••••••••••••••••#
class cuestionario_tag(models.Model):
    cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    class Meta:
        ordering = ["-id"]

        verbose_name = "Relacion MM - Cuestionario - Tag"

        verbose_name_plural = "Relaciones MM - Cuestionarios - Tags"

        db_table = "Relacion M-M cuestionario - tag"
