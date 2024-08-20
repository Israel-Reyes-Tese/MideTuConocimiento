from django.contrib import admin
from .models import Cuestionario
# Register your models here.
@admin.register(Cuestionario)
class Cuestionario_admin(admin.ModelAdmin):
    list_display = ('id','titulo','descripcion','profesor')
    search_fields = ('id','titulo','profesor',)
    list_filter = ('titulo',)
    ordering = ('id','titulo',)
    date_hierarchy = 'fecha_ingreso'
    verbose_name = "Cuestionario"
    verbose_name_plural = "Cuestionarios"