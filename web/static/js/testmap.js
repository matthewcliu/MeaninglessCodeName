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

    var location = new google.maps.LatLng(latitude, longitude);

    var marker = new google.maps.Marker({
        position: location,
        map: map
    });

    var infowindow = new google.maps.InfoWindow({
        content: name + time_instance,
        size: new google.maps.Size(50,50)
    });

    attachInfoWindows(marker, infowindow);

}

function attachInfoWindows(marker, infowindow){
    google.maps.event.addListener(marker, 'click', function(){
        infowindow.open(map, marker); 
    });
}

google.maps.event.addDomListener(window, 'load', initialize);
