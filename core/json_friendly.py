from datetime import *

def flatten_objects(obj):
    d = obj
    if hasattr(obj, '__dict__'):
        d = obj.__dict__
    if isinstance(d, dict):
        return dict((key, flatten_objects(value)) for key, value in d.iteritems())
    if isinstance(obj, list):
        return [flatten_objects(value) for value in obj]
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    return obj
        