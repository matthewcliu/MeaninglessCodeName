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
    time_instance = models.DateTimeField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    class Meta:
        db_table = 'entityinstance'
        
class SocialNetwork(models.Model):
    
    social_network = models.CharField(max_length=256)
    
    class Meta:
        db_table = 'socialnetwork'
    
class SocialNetworkData(models.Model):
    
    entitynode = models.ForeignKey('EntityNode')    
    social_network_node = models.ForeignKey('SocialNetwork')
    network_id = models.CharField(max_length=256)
    handle = models.CharField(max_length=256)
    
    class Meta:
        db_table = 'socialnetworkdata'