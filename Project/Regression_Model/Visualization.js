// Fetch the grouped dataset from the JSON file
fetch('grouped_household_size_devices.json')
  .then(response => response.json())
  .then(data => {
    // Prepare the data for Chart.js
    const labels = data.map(row => `Size ${row["Household Size"]}`); // Household sizes
    const avgDevices = data.map(row => row["Average Number of Devices"]); // Average number of devices

    // Create a bar chart
    const ctx1 = document.getElementById('devicesChart').getContext('2d');
    new Chart(ctx1, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Average Number of Devices',
          data: avgDevices,
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1,
          barThickness: 15
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: true },
          tooltip: { enabled: true }
        },
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Average Number of Devices'
            }
          },
          x: {
            title: {
              display: true,
              text: 'Household Size'
            }
          }
        }
      }
    });
  })
  .catch(error => console.error('Error loading the dataset:', error));
