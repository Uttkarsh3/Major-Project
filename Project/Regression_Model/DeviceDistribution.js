// Device type percentages
const devicePercentages = {
  AC: 0.1,
  TV: 0.1,
  LightBulb: 0.4,
  Fan: 0.2,
  Refrigerator: 0.1,
  WashingMachine: 0.1,
};

// Colors for each device type
const deviceColors = {
  AC: "#006064", 
  TV: "#00838f",
  LightBulb: "#0097a7", 
  Fan: "#00bcd4", 
  Refrigerator: "#4dd0e1", 
  WashingMachine: "#b2ebf2",
};

// Fetch predictions from JSON file
async function fetchPredictions() {
  const response = await fetch("predictions.json");
  return await response.json();
}

// Categorize household sizes
function categorizeHouseholdSize(size) {
  if (size >= 1 && size <= 4) return "Low";
  if (size >= 5 && size <= 7) return "Medium";
  if (size >= 8 && size <= 10) return "High";
  return null;
}

// Calculate averages for each category
function calculateAverages(predictions) {
  const categories = {
    Low: { totalDevices: 0, count: 0 },
    Medium: { totalDevices: 0, count: 0 },
    High: { totalDevices: 0, count: 0 },
  };

  // Group data by category
  predictions.forEach((entry) => {
    const category = categorizeHouseholdSize(entry["Household Size"]);
    if (category) {
      categories[category].totalDevices += entry["Predicted Number of Devices"];
      categories[category].count += 1;
    }
  });

  // Calculate averages
  for (let category in categories) {
    const { totalDevices, count } = categories[category];
    categories[category].averageDevices = count > 0 ? Math.floor(totalDevices / count) : 0;
  }

  return categories;
}

// Distribute devices based on percentages
function distributeDevices(averages) {
  const distribution = {};

  for (let category in averages) {
    const averageDevices = averages[category].averageDevices;
    const devices = {};

    for (let device in devicePercentages) {
      devices[device] = Math.floor(averageDevices * devicePercentages[device]);
    }

    distribution[category] = devices;
  }

  return distribution;
}

// Render the stacked bar chart
function renderChart(distribution) {
  const categories = ["Low", "Medium", "High"];
  const deviceTypes = Object.keys(devicePercentages);

  const datasets = deviceTypes.map((device) => ({
    label: device,
    data: categories.map((category) => distribution[category][device] || 0),
    backgroundColor: deviceColors[device],
  }));

  const ctx = document.getElementById("deviceDistributionChart").getContext("2d");
  new Chart(ctx, {
    type: "bar",
    data: {
      labels: categories,
      datasets: datasets,
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: "top",
        },
        title: {
          display: true,
          text: "Device Distribution Across Household Sizes",
        },
      },
      scales: {
        x: {
          stacked: true,
        },
        y: {
          stacked: true,
          ticks: {
            beginAtZero: true,
          },
        },
      },
    },
  });
}

// Main function
async function main() {
  const predictions = await fetchPredictions();
  const averages = calculateAverages(predictions);
  const distribution = distributeDevices(averages);
  renderChart(distribution);
}

// Execute main function
main();
