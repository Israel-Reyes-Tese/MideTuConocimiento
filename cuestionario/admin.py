from django.contrib import admin
from .models import *
from .models_secundarios import *
##################################################
    # MODELO INLINE CUESTIONARIO - TAGS #
##################################################
class cuestiomario_TagsInline(admin.StackedInline):
    model = cuestionario_tag
    extra = 0
    autocomplete_fields = ['cuestionario', 'tag']

@admin.register(Cuestionario)
class Cuestionario_admin(admin.ModelAdmin):
    list_display = ('id','titulo','descripcion','profesor')
    search_fields = ('id','titulo','profesor',)
    list_filter = ('titulo',)
    ordering = ('id','titulo',)
    date_hierarchy = 'fecha_ingreso'
    verbose_name = "Cuestionario"
    verbose_name_plural = "Cuestionarios"
    inlines = [cuestiomario_TagsInline,]

@admin.register(Tags)
class Tag_admin(admin.ModelAdmin):
    list_display = ('id','titulo')
    search_fields = ('id','titulo')
    list_filter = ('titulo',)
    ordering = ('id','titulo',)
    verbose_name = "Tag"
    verbose_name_plural = "Tags"

# Modelos principales
admin.site.register(Pregunta)
admin.site.register(Opcion)
admin.site.register(Respuesta)
admin.site.register(Resultado)
# Modelos secundarios
