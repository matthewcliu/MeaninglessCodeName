var meaninglesscodename = meaninglesscodename || {};
meaninglesscodename.listing = meaninglesscodename.listing || {};

function initialize() {

    var myLatlng = new google.maps.LatLng(37.7750,-122.4183);
    var myOptions = {
    zoom: 12,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.HYBRID
    }

    var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

    for (var i = 0; i < locations_list.length; i++) {

        latitude = locations_list[i].entity_latitude/10000;
        longitude = locations_list[i].entity_longitude/10000;
        name = locations_list[i].entity_name;
        time_instance = locations_list[i].entity_time;
        
        var location = new google.maps.LatLng(latitude, longitude);

        var marker = createMarker(map, location);
        var marker_description = createMarkerDescription(name, time_instance);
        attachDescriptionToMarker(map, marker, marker_description);        
    } 
}

function createMarker(map, location){
    var created_marker = new google.maps.Marker({
        position: location,
        map: map
    });
    
    return created_marker;
}

function createMarkerDescription(name, time_instance){
    var created_marker_description = new google.maps.InfoWindow({
        content: name + " " + time_instance,
        size: new google.maps.Size(50,50)
    });
    
    return created_marker_description;
}

function attachDescriptionToMarker(map, marker, marker_description){
    google.maps.event.addListener(marker, 'click', function(){
        marker_description.open(map, marker); 
    });
}

google.maps.event.addDomListener(window, 'load', initialize);