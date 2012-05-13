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
        self.entity_instance_list = []
        self.message = None      


    
    
