#######################################################
#                                                     #
#                  Modulos utiles                     #
#                                                     #
#######################################################
from django.shortcuts import render
from django.views.generic import View, TemplateView
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
        try:
            # Filtrar los cuestionarios
            cuestionario = Cuestionario.objects.get(pk=cuestionario_pk)
            # Verificar la pregunta
            pregunta = cuestionario.preguntas.get(pk=pregunta_pk)
            # Filtrar las opciones de la pregunta
            opciones = pregunta.opciones.all()
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
    
