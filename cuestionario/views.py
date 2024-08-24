                                                        # ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
                                                        #                 VIEW INICIO                  #
                                                        # ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
# MODELOS PRINCIPALES UTILIZADOS
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
from .models import Cuestionario
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
# MODELOS SECUNDARIOS UTILIZADOS
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
from .models_secundarios import Tags
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
# MODELOS SECUNDARIOS UTILIZADOS
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
from ajustes_servidor.models import usuario
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
from django.shortcuts import render
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
# LIBRERIAS NECESARIAS PARA CREAR LAS VIEWS GENERICAS              
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
from django.views.generic import ListView, DetailView
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
# DECORADOR PARA REQUERIR ESTAR LOGEADO
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
from django.contrib.auth.mixins import LoginRequiredMixin
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
#  CLASES PARA GESTIONAR LA INFORMACION 
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
from django.views import View
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
#  CLASSS INICIO
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
class Inicio(LoginRequiredMixin, ListView):
    model = Cuestionario
    template_name = 'inicio.html'
    context_object_name = 'registros'
    def get_context_data(self, **kwargs):
        model = Cuestionario
        context = super().get_context_data(**kwargs)
        context["cuestionarios"] = Cuestionario.objects.all()
        # Data usuario
        context["usuario_nombre"] = usuario.objects.get(username=self.request.user.username)
        # Data tags #1 
        context["tag_1"] = Tags.objects.all().first()
        context["tag_2"] = Tags.objects.all().last()
        # Registros del tags 1
        context["regisros_tag_1"] = context["tag_1"].RELACION_CUESTIONARIO_TAGS.all()
        # Registros del tags 2
        context["regisros_tag_2"] = context["tag_2"].RELACION_CUESTIONARIO_TAGS.all()
        
        return context
        
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
#  CLASSS CUESTIONARIO
# ♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣ #
class Cuestionario_DetailView(LoginRequiredMixin, DetailView):
    model = Cuestionario
    template_name = 'cuestionario.html'
    context_object_name = 'registro'
    id_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        model = Cuestionario
        context = super().get_context_data(**kwargs)
        # Cuestionario 
        context["cuestionarios"] = Cuestionario.objects.get(id=self.kwargs['pk'])
        # Data usuario
        context["usuario_nombre"] = usuario.objects.get(username=self.request.user.username)
        # Primer pregunta cuestionario
        context["primera_pregunta"] = context["cuestionarios"].preguntas.all().first()
        # lista de ID de las preguntas
        lista_id = [pregunta.id for pregunta in context["cuestionarios"].preguntas.all()]
        # Elimina el id de la primera pregunta de la lista - lista_id
        context["id_segunda_pregunta"] = lista_id[1]
        # Opciones de la primera pregunta
        context["opciones"] = context["primera_pregunta"].opciones.all() # Obtener todas las opciones relacionadas con la pregunta
        print("id de la primera pregunta", context["primera_pregunta"].id , "id de la segunda pregunta", context["id_segunda_pregunta"])
        return context