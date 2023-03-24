
from schemas.models import Schema
from rest_framework import serializers

class SchemaSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    schema = serializers.CharField()
    active = serializers.BooleanField(required=True)
    name = serializers.CharField()
    created = serializers.DateTimeField(required=False)
    updated = serializers.DateTimeField(required=False,allow_null=True)

    
    
    def create(self, validated_data):  
        return Schema.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        
        instance.schema = validated_data.get('schema',instance.schema)
        instance.active = validated_data.get('active',instance.active)
        instance.name = validated_data.get('name',instance.name)
        instance.created = validated_data.get('created',instance.created)
        instance.updated = validated_data.get('updated',instance.updated)
        instance.save()
        return instance