import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Schema(models.Model):

    id = models.IntegerField(primary_key=True, null=False)
    schema = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField( default=timezone.now)
    name = models.TextField()
    updated = models.DateTimeField(default=None, null=True)
    
    
class Transaction(models.Model):
    id = models.IntegerField(primary_key=True,null=False)
    status = models.TextField(max_length=60)
    product_id = models.IntegerField()
    created = models.DateTimeField( default=timezone.now)

