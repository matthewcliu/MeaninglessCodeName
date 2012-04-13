from django.db import models
from django.contrib.auth.models import User

class EntityNode(models.Model):
    
    name = models.CharField(max_length=256)
    categorynode = models.ForeignKey('CategoryNode')
    
    class Meta:
        db_table = 'entity'
        
class CategoryNode(models.Model):
    
    name = models.CharField(max_length=256)
    
    class Meta:
        db_table = 'category'
        
class EntityInstance(models.Model):
    
    entitynode = models.ForeignKey('EntityNode')
    time_instance = models.IntegerField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    class Meta:
        db_table = 'entityinstance'