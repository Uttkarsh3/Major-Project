// Function to fetch and parse the CSV data
async function fetchAndParseCSV(url) {
    try {
        const response = await fetch(url);
        const csvText = await response.text();
        const rows = csvText.split("\n").map(row => row.trim()).filter(row => row); // Remove empty rows
        const header = rows[0].split(","); // Get the header row

        // Parse data rows into an array of objects
        const data = rows.slice(1).map(row => {
            const columns = row.split(",");
            return {
                deviceName: columns[0], // Device Name
                dailyUsage: parseFloat(columns[1]), // Daily Usage (Normalized)
                idleTime: parseFloat(columns[2]), // Idle Time (Normalized)
            };
        });

        return data.filter(row => !isNaN(row.dailyUsage) && !isNaN(row.idleTime)); // Filter valid rows
    } catch (error) {
        console.error("Error fetching the CSV data:", error);
    }
}

// Function to initialize random centroids
function initializeCentroids(data, k) {
    const centroids = [];
    for (let i = 0; i < k; i++) {
        const randomIndex = Math.floor(Math.random() * data.length);
        centroids.push({ ...data[randomIndex] });
    }
    return centroids;
}

// Function to assign data points to clusters
function assignToClusters(data, centroids) {
    const clusters = centroids.map(() => []); // Create empty clusters

    data.forEach(item => {
        let minDistance = Infinity;
        let clusterIndex = 0;

        centroids.forEach((centroid, index) => {
            const distance = Math.sqrt(
                Math.pow(item.dailyUsage - centroid.dailyUsage, 2) +
                Math.pow(item.idleTime - centroid.idleTime, 2)
            );
            if (distance < minDistance) {
                minDistance = distance;
                clusterIndex = index;
            }
        });

        clusters[clusterIndex].push(item);
        item.cluster = clusterIndex; // Assign cluster index to the item
    });

    return clusters;
}

// Function to calculate new centroids
function updateCentroids(clusters) {
    return clusters.map(cluster => {
        const totalUsage = cluster.reduce((sum, item) => sum + item.dailyUsage, 0);
        const totalIdleTime = cluster.reduce((sum, item) => sum + item.idleTime, 0);
        const clusterSize = cluster.length;

        return {
            dailyUsage: clusterSize ? totalUsage / clusterSize : 0,
            idleTime: clusterSize ? totalIdleTime / clusterSize : 0,
        };
    });
}

// K-Means clustering function
function performKMeansClustering(data, k = 3) {
    let centroids = initializeCentroids(data, k);
    let prevCentroids = [];
    let maxIterations = 100;

    for (let iteration = 0; iteration < maxIterations; iteration++) {
        const clusters = assignToClusters(data, centroids);
        const newCentroids = updateCentroids(clusters);

        // Check for convergence
        if (JSON.stringify(newCentroids) === JSON.stringify(prevCentroids)) break;

        prevCentroids = centroids;
        centroids = newCentroids;
    }

    return data; // Return data with cluster assignments
}

// Function to plot data using Plotly
function plotData(data, k) {
    const clusterColors = ["red", "blue", "green", "purple", "orange"]; // Add more colors if needed

    // Descriptive cluster names
    const clusterDescriptions = [
        "High Energy Usage Devices",       // Cluster 1
        "Energy-Efficient Idle Devices",  // Cluster 2
        "Constantly Running Devices"      // Cluster 3
    ];

    const scatterData = [];

    for (let i = 0; i < k; i++) {
        const clusterPoints = data.filter(item => item.cluster === i);

        scatterData.push({
            x: clusterPoints.map(item => item.dailyUsage),
            y: clusterPoints.map(item => item.idleTime),
            mode: "markers",
            type: "scatter",
            name: clusterDescriptions[i] || `Cluster ${i + 1}`, // Use description or fallback to Cluster #
            marker: {
                size: 12,
                color: clusterColors[i],
            },
            text: clusterPoints.map(
                item =>
                    `Device: ${item.deviceName}<br>Daily Usage: ${item.dailyUsage.toFixed(
                        2
                    )}<br>Idle Time: ${item.idleTime.toFixed(2)}`
            ), // Hover text with more details
        });
    }

    const layout = {
        title: "Device Clustering (K-Means)",
        xaxis: { title: "Daily Usage (Normalized)" },
        yaxis: { title: "Idle Time (Normalized)" },
        legend: { title: { text: "Clusters" } }, // Legend title
    };

    const config = { responsive: true };

    Plotly.newPlot("results", scatterData, layout, config);
}


// Main function to fetch data, perform clustering, and visualize
(async function main() {
    const csvUrl = "preprocessed_dataset.csv"; // Path to your CSV file
    const data = await fetchAndParseCSV(csvUrl);

    if (!data || data.length === 0) {
        console.error("No valid data found in the CSV file.");
        return;
    }

    const k = 3; // Number of clusters
    const clusteredData = performKMeansClustering(data, k); // Perform K-Means with 3 clusters
    plotData(clusteredData, k); // Plot the clustered data
})();
