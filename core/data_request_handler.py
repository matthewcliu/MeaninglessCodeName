from meaninglesscodename.core.models import *
import datetime

def handle_request(data_request):

    query_time = process_time(data_request.time, data_request.time_range)
    query_entities = entity_lookup(data_request.categories, data_request.entities)
    entity_instances = EntityInstance.objects.raw("SELECT * FROM entityinstance WHERE entitynode_id IN (%s) AND time_instance >= '%s' AND (((latitude - %s)^2 + (longitude - %s)^2)^2 < %s^2)" % (",".join(query_entities), query_time, data_request.latitude, data_request.longitude, data_request.distance_range))
    
    return entity_instances

def process_time(current_time, time_range):
    past_time = current_time - datetime.timedelta(seconds = time_range)
    return past_time

def entity_lookup(categories_list, entities_list):
    
    if entities_list and categories_list:
        #Need to write this use case later
        entities_ids = ['0']
        
    elif entities_list:
        matching_entities = EntityNode.objects.filter(name__in = entities_list)
        entities_ids = []
        for matching_entity in matching_entities:
            entities_ids.append(str(matching_entity.id))
        
    elif categories_list:
        matching_categories = CategoryNode.objects.filter(name__in = categories_list)
        categories_ids = []
        for matching_category in matching_categories:
            categories_ids.append(str(matching_category.id))
        matching_entities = EntityNode.objects.filter(categorynode__in = categories_ids)
        entities_ids = []
        for matching_entity in matching_entities:
            entities_ids.append(str(matching_entity.id))
         
    else:
        #Need a better error condition here
        entities_ids = ['0']
    
    return entities_ids