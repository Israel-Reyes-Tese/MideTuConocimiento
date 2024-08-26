#######################################################
#                                                     #
#                  Modulos utiles                     #
#                                                     #
#######################################################
from django.shortcuts import render
from django.views.generic import View, TemplateView, DetailView
from django.core.serializers import serialize
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import request
import json
from cuestionario.models import *
#######################################################
#                                                     #
#                CSRF TOKEN                           #
#                                                     #
#######################################################
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻#
#                       VERIFICAR RESPUESTA
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻#
class VerificarRespuestaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        # Convertir la data html en texto plano
        opcion_texto = data.get('opcion_texto')
        opcion_texto = opcion_texto.strip()
        # Cuestionario 
        cuestionario_pk = data.get('cuestionario_id')
        # Pregunta
        pregunta_pk = data.get('pregunta_id')
        # Guardar la respuesta en la base de datos
        usuario_actual = request.user
        # Lista de preguntas respondidas
        try:
            # Filtrar los cuestionarios
            cuestionario = Cuestionario.objects.get(pk=cuestionario_pk)
            # Verificar la pregunta
            pregunta = cuestionario.preguntas.get(pk=pregunta_pk)
            # Filtrar las opciones de la pregunta
            opciones = pregunta.opciones.all()
            # Repuesta del usuario
            try:
                # Pregunta ya respondida
                respuesta = Respuesta.objects.get(estudiante=usuario_actual, opcion=Opcion.objects.get(texto=opcion_texto))
                # Actualizar la respuesta
                respuesta.save()
            except Respuesta.DoesNotExist:
                respuesta = Respuesta.objects.create(estudiante=usuario_actual, opcion=Opcion.objects.get(texto=opcion_texto))
                respuesta.save()
            # Verificar la opción en la lista de opciones
            lista_opciones = [opcion.texto for opcion in opciones]
            if opcion_texto in lista_opciones:
                opcion = Opcion.objects.get(texto=opcion_texto)
                if opcion.es_correcta:
                    return JsonResponse({'correcta': True})
                else:
                    return JsonResponse({'correcta': False})
            else:
                return JsonResponse({'error': 'Opción no encontrada'}, status=404)
        
        except Opcion.DoesNotExist:
            return JsonResponse({'error': 'Opción no encontrada'}, status=404)
    
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻#
#                     VERIFICAR SI EXISTE SIGUIENTE PREGUNTA
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻#
class VerificarSiguientePreguntaView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    def post(self, request, *args, **kwargs):
        print("Funcion Verificar-Siguiente-PreguntaView")
        data = json.loads(request.body)
        print(data)
        # Lista de preguntas respondidas
        lista_preguntas_respondidas = data.get('lista_preguntas')
        # Transformar la lista de preguntas respondidas en un conjunto
        lista_preguntas_respondidas = set(lista_preguntas_respondidas)
        # Preguntas faltantes
        cuestionario_pk = data.get('cuestionario_id')
        cuestionario = Cuestionario.objects.get(pk=cuestionario_pk)
        # Lista de preguntas
        preguntas = cuestionario.preguntas.all()
        # Eliminar las preguntas respondidas
        preguntas_faltantes = preguntas.exclude(id__in=lista_preguntas_respondidas)
        print("Preguntas faltantes",preguntas_faltantes)
        try:
            if preguntas_faltantes.exists():
                print("Siguiente pregunta", preguntas_faltantes.first().id)
                return JsonResponse({'siguiente': True, 'siguiente_pregunta_id': preguntas_faltantes.first().id}, status=200)
            else:
                print("No hay siguiente pregunta")
                return JsonResponse({'siguiente': False, 'siguiente_pregunta_id': False}, status=404)
        except Pregunta.DoesNotExist:
            return JsonResponse({'error': 'Pregunta no encontrada'}, status=404)

#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻#
#                      PREGUNTA DETAIL VIEW
#☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻☻#
class PreguntaDetailView(DetailView):
    model = Pregunta
    def get(self, request, *args, **kwargs):
        pregunta = self.get_object()  # Obtener la pregunta actual
        opciones = pregunta.opciones.all()  # Obtener todas las opciones relacionadas con la pregunta
        # Extraer el id del cuestionario de la url
        cuestionario_id = kwargs.get('cuestionario_id')
        # Extraer la lista de preguntas respondidas
        preguntas_respondidas = request.session.get('lista_preguntas_respondidas')
        # Validar la cantidad de preguntas en el cuestionario
        cuestionario = Cuestionario.objects.get(pk=cuestionario_id)
        preguntas = cuestionario.preguntas.all()
        data = {
            'pregunta': pregunta.texto,
            'pregunta_id': pregunta.id,
            'opciones': [
                {'texto': opcion.texto, 'id': opcion.id} for opcion in opciones
            ],
        }
        return JsonResponse(data)

