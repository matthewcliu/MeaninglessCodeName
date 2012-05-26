from meaninglesscodename.core.models import *
from meaninglesscodename.core.data_request import *

import datetime

def handle_request(data_request):

    query_start_time = find_starting_time(data_request.time, data_request.time_range)
    query_entities_ids_list = find_entities_ids_list(data_request.categories_list, data_request.entities_list)
        
    #entity_instances = EntityInstance.objects.raw("SELECT * FROM entityinstance WHERE entitynode_id IN (%s) AND time_instance >= '%s' AND (((latitude - %s)^2 + (longitude - %s)^2)^2 < %s^2)" % (",".join(query_entities_ids_list), query_start_time, data_request.latitude, data_request.longitude, data_request.distance_range))
    
    #query = "SELECT * FROM entityinstance WHERE entitynode_id IN (%s) AND time_instance >= '%s' AND (((latitude - %s)^2 + (longitude - %s)^2)^2 < %s^2)"
    #params = [",".join(query_entities_ids_list), query_start_time, data_request.latitude, data_request.longitude, data_request.distance_range]
    
    num_ids = len(query_entities_ids_list)
    format_params_str = ','.join(('%d',) * num_ids)
    query = "SELECT * FROM entityinstance WHERE entitynode_id IN (%s)" % format_params_str
    # "SELECT * FROM entityinstance WHERE entitynode_id IN (%d, %d, %d, %d, %d, %d);"
    params = query_entities_ids_list

    matching_entity_instances = EntityInstance.objects.raw(query, *params)
    
    #Lookup names for all entities - for loop to create an array of entity_ids, then grab all the names from Entity table to form an id-name pair, and then re-assign them to new object
                
    data_response_obj = DataResponse()
    data_response_obj.entity_instance_list = matching_entity_instances
        
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
            #query_entities_ids_list.append(str(matching_entity.id)) 
            query_entities_ids_list.append(matching_entity.id)
        
    elif categories_list:
        matching_categories = CategoryNode.objects.filter(name__in = categories_list)
        categories_ids_list = []
        for matching_category in matching_categories:
            #categories_ids_list.append(str(matching_category.id))
            categories_ids_list.append(matching_category.id)
        matching_entities = EntityNode.objects.filter(categorynode__in = categories_ids_list)
        entities_ids_list = []
        for matching_entity in matching_entities:
            #entities_ids_list.append(str(matching_entity.id))
            entities_ids_list.append(matching_entity.id)
         
    else:
        #Need a better error condition here
        entities_ids_list = ['0']
    
    return entities_ids_list