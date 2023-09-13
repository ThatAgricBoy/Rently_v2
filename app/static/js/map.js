document.addEventListener('DOMContentLoaded', function() {
    // Get all elements with the class "search"
    const searchInputs = document.querySelectorAll('.search');
    const geocoder = new google.maps.Geocoder();
    const mapElement = document.getElementById('map');

    const mapOptions = {
        center: { lat: 0, lng: 0 }, // Default center
        zoom: 10, // Default zoom level
    };

    const map = new google.maps.Map(mapElement, mapOptions);

    // Add event listeners to all search input fields
    searchInputs.forEach(function(searchInput) {
        searchInput.addEventListener('keypress', function(event) {
            if (event.key === 'Enter') {
                const inputValue = searchInput.value;
                console.log('Input value:', inputValue);
                geocodeAddress(inputValue, map);
            }
        });
    });

    function geocodeAddress(address, map) {
    console.log('Geocoding address:', address);
    geocoder.geocode({ 'address': address }, function(results, status) {
        console.log('Geocoding status:', status); // Log the status
        if (status === 'OK') {
            // ... Rest of your code
        } else {
            console.error('Geocode was not successful for the following reason: ' + status);
        }
    });
}
else {
                console.error('Geocode was not successful for the following reason: ' + status);
            }
        });
    }
});
