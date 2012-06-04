from meaninglesscodename.core.models import *
from meaninglesscodename.core.data_request import *

import datetime

def handle_request(data_request):

    query_start_time = find_starting_time(data_request.time, data_request.time_range)
    query_entities_ids_list = find_entities_ids_list(data_request.categories_list, data_request.entities_list)
        
    query = "SELECT * FROM entityinstance WHERE entitynode_id IN (%s)"
    params = (",".join(query_entities_ids_list),)

    matching_entity_instances = EntityInstance.objects.raw(query % params)      
    
    #Need to make entity_instances unique
    
    matching_entity_ids = []
    matching_entity_ids = [matching_entity_instance.entitynode_id for matching_entity_instance in matching_entity_instances]

    matching_entities_list = EntityNode.objects.filter(id__in = matching_entity_ids)
    
    entity_id_to_entity_map = {}

    entity_id_to_entity_map = dict((matching_entity.id, matching_entity) for matching_entity in matching_entities_list)
    
    entities_to_display_list = []

    for matching_entity_instance in matching_entity_instances:
        entity_map_object = EntityMapDisplayData()
        entity_map_object.entity_name = entity_id_to_entity_map[matching_entity_instance.entitynode_id].name
        entity_map_object.entity_latitude = matching_entity_instance.latitude
        entity_map_object.entity_longitude = matching_entity_instance.longitude
        entity_map_object.entity_time = matching_entity_instance.time_instance
                
        entities_to_display_list.append(entity_map_object)

    data_response_obj = DataResponse()    
    data_response_obj.entity_map_display_data_list = entities_to_display_list
        
    return data_response_obj

def find_starting_time(current_time, time_range):
    starting_time = current_time - datetime.timedelta(seconds = time_range)
    return starting_time

def find_entities_ids_list(categories_list, entities_list):
    
    if entities_list and categories_list:
        #Need to write this use case later
        entities_ids_list = ['0']
        
    elif entities_list:
        matching_entities = EntityNode.objects.filter(name__in = entities_list)
        entities_ids_list = []
        for matching_entity in matching_entities:
            query_entities_ids_list.append(str(matching_entity.id))
        
    elif categories_list:
        matching_categories = CategoryNode.objects.filter(name__in = categories_list)
        categories_ids_list = []
        for matching_category in matching_categories:
            categories_ids_list.append(str(matching_category.id))
        matching_entities = EntityNode.objects.filter(categorynode__in = categories_ids_list)
        entities_ids_list = []
        for matching_entity in matching_entities:
            entities_ids_list.append(str(matching_entity.id))
         
    else:
        #Need a better error condition here
        entities_ids_list = ['0']
    
    return entities_ids_list
