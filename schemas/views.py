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

# Create your views here.
@api_view(['GET', 'POST'])
def schema_list(request, format=None):
    if request.method == 'GET':
        schemas = Schema.objects.all()
        serializer = SchemaSerializer(schemas, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SchemaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET', 'POST','DELETE'])
def schema_details(request,pk,format=None):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): Id for the schema we are trying to update
    """
    
    try:
        schema = Schema.objects.get(pk=pk)
    except Schema.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = SchemaSerializer(schema)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SchemaSerializer(schema,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        schema.delete()
        return Response(status=204)
    
class SchemaList(generics.ListCreateAPIView):
    
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer
    # def get(self, request, format=None):
    #     schemas = Schema.objects.all()
    #     serializer = SchemaSerializer(schemas, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request, format=None):
    #     data = JSONParser().parse(request)
    #     serializer = SchemaSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class SchemaDetail(generics.ListCreateAPIView):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer
    
    # def get_object(self,pk):
    #     try:
    #         return Schema.objects.get(pk=pk)
    #     except Schema.DoesNotExist:
    #         return Http404
        
        
    # def get(self, request, pk, format=None):
    #     schema = self.get_object(pk)
    #     serializer = SchemaSerializer(schema)
    #     return Response(serializer.data)
    
    # def put(self,request,pk,format=None):
    #     schema = self.get_object(pk)
    #     data = JSONParser().parse(request)
    #     serializer = SchemaSerializer(schema,data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    # def delete(self,request,pk, format=None):
    #       schema = self.get_object(pk)
    #       schema.delete()
    #       return Response(status=status.HTTP_204_NO_CONTENT)

        
        