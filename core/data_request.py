class DataRequest(object):

    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.distance_range = None
        self.time = None
        self.time_range = 3600
        self.categories_list = []
        self.entities_list = []
        
class DataResponse(object):
    
    def __init__(self):
        self.entity_map_display_data_list = []
        self.message = None      

#Create new object class in place of entity_instance_list
    
class EntityMapDisplayData(object):
    
    def __init__(self):
        self.entity_name = None
        self.entity_latitude = None
        self.entity_longitude = None
        self.entity_time = None
        