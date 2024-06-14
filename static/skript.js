document.addEventListener('DOMContentLoaded', function() {
    var addDestinationForm = document.getElementById('add-destination-form');

    addDestinationForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Spriječavamo slanje forme

        var name = document.getElementById('name').value;
        var description = document.getElementById('description').value;
        var location = document.getElementById('location').value;
        var date = document.getElementById('date').value;

        var newDestination = {
            name: name,
            description: description,
            location: location,
            date: date
        };

        var destinations = JSON.parse(localStorage.getItem('destinations')) || [];
        
        destinations.push(newDestination);
        localStorage.setItem('destinations', JSON.stringify(destinations));

        document.getElementById('add-destination-form').reset();
        window.location.href = "/destinations";
    });
});
