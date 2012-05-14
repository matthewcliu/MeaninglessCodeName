var meaninglesscodename = meaninglesscodename || {};
meaninglesscodename.testmap = meaninglesscodename.testmap || {};

function initialize() {

    var myLatlng = new google.maps.LatLng(37.7750,-122.4183);
    var myOptions = {
    zoom: 8,
    center: myLatlng,
    mapTypeId: google.maps.MapTypeId.HYBRID
    }

    var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);

    for (var i = 0; i < json_object_for_map.locations.length; i++) {

        latitude = json_object_for_map.locations[i].fields.latitude/10000;
        longitude = json_object_for_map.locations[i].fields.longitude/10000;
        entity_node = json_object_for_map.locations[i].fields.entitynode;
        time_instance = json_object_for_map.locations[i].fields.time_instance;

        var location = new google.maps.LatLng(latitude, longitude);

        var marker = new google.maps.Marker({
            position: location,
            map: map
        });
                        
        var infowindow = new google.maps.InfoWindow({
            content: entity_node + " " + time_instance,
            size: new google.maps.Size(50,50)
        });
        
        attachInfoWindows(map, marker, infowindow);        
    } 
}

function attachInfoWindows(map, marker, infowindow){
    google.maps.event.addListener(marker, 'click', function(){
        infowindow.open(map, marker); 
    });
}

google.maps.event.addDomListener(window, 'load', initialize);