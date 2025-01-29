// Fetch data for predictions (Ensure predictions.json exists and is correctly formatted)
fetch('predictions.json')
    .then(response => response.json())
    .then(predictions => {
        // Extract labels and data from the JSON
        const labels = predictions.map(p => p['Household Size']);
        const data = predictions.map(p => p['Predicted Number of Devices']);

        // Get the canvas element
        const ctx = document.getElementById('predictionChart').getContext('2d');

        // Create the bar chart
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Predicted Number of Devices',
                    data: predictions.map(p => p['Predicted Number of Devices']),
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                    barThickness: 15

                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
    .catch(error => {
        console.error('Error fetching prediction data:', error);
    });
