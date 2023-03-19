from django.db import models

# Create your models here.

class Schema(models.Model):

    schema = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    name = models.TextField()
    updated = models.DateField(default=None, null=True)
    
    

