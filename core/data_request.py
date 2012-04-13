class DataRequest(Object):

    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.distance_range = None
        self.time = None
        self.time_range = 3600
        self.categories = []
        self.entities = []        

    def handle_request(self, data_request):

        #Throw exceptions if lat, long, range, time are not given
        if not data_request.latitude or not data_request.longitude or not data_request.time:
            raise Exception, e:
        #For simplicity do not allow search and categories browse at the same time
        elif data_request.entities & data_request.categories:
            raise Exception, e:
        else:
            query_time = process_time(data_request.time, data_request.time_range)    
            query_entities = entity_lookup(data_request.categories, data_request.entities)
    
            if entities_list:
                entity_instances = EntityInstance.objects.raw("SELECT * FROM entityinstance WHERE 
                entitynode_id IN %s AND time_instance >= %d AND (latitude - %d)**2 + (longitude - %d)**2)**2 < %d" % (",".join(query_entities), query_time, data_request.latitude, data_request.longitude, data_request.distance_range**2))
            else:
                entity_instances = EntityInstance.objects.raw("SELECT * FROM entityinstance WHERE 
                time_instance >= %d AND (latitude - %d)**2 + (longitude - %d)**2)**2 < %d" % (entities_object_list, query_time, data_request.latitude, data_request.longitude, data_request.distance_range**2))
                
            return entity_instances

    def process_time(current_time, range):
        past_time = current_time - range
        return past_time
    
    def entity_lookup(categories_list, entities_list):
        if entities_list:
            matching_entities = EntityNode.objects.filter(name__in = entities_list)
            entities_ids = []
            for matching_entity in matching_entities:
                entities_ids.append(matching_entity.id)
            
        elif categories_list:
            matching_categories = CategoryNode.objects.filter(name__in = categories_list)
            categories_ids = []
            for matching_category in matching_categories:
                categories_ids.append(matching_category.id)
            matching_entities = EntityNode.objects.filter(categorynode_id__in = categories.ids)
            entities_ids = []
            for matching_entity in matching_entities:
                entities_ids.append(matching_entity.id)
             
        else:
            entities_ids = []
        
        return entities_ids
    
    
