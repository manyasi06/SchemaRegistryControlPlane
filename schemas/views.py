from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework import generics


from schemas.models import Schema
from schemas.serializers import SchemaSerializer
    
class SchemaList(generics.ListCreateAPIView):
    
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer

    
class SchemaDetail(generics.ListCreateAPIView):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer
    
   
        
        