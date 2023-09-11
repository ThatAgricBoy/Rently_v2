document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.querySelector('.search');
    const geocoder = new google.maps.Geocoder();
    const mapElement = document.getElementById('map');

    const mapOptions = {
        center: desiredLocation, // Use the desiredLocation variable as the center
        zoom: 10,
    };

    const map = new google.maps.Map(mapElement, mapOptions);

    searchInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            geocodeAddress(searchInput.value, map);
        }
    });

    function geocodeAddress(address, map) {
        geocoder.geocode({ 'address': address }, function(results, status) {
            if (status === 'OK') {
                const location = results[0].geometry.location;
                map.setCenter(location);
                // You can add a marker if you want
                new google.maps.Marker({
                    position: location,
                    map: map,
                });
            } else {
                console.error('Geocode was not successful for the following reason: ' + status);
            }
        });
    }
});
