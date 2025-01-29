# Device Clustering using K-Means

This project uses the **K-Means clustering algorithm** to group devices based on their energy usage patterns. The clusters are visualized using **Plotly.js**, providing a clear understanding of the device categories.

---

## 🔧 **How It Works**

The K-Means algorithm is applied to cluster devices using the following parameters:
- **Daily Usage (Normalized)**: How much energy a device uses daily.
- **Idle Time (Normalized)**: How long the device remains idle.

The devices are grouped into **3 clusters**:
1. **Cluster 1 - High Energy Usage Devices:**  
   Devices that consume a lot of electricity daily.
   
2. **Cluster 2 - Energy-Efficient Idle Devices:**  
   Devices that are idle most of the time and consume minimal energy.

3. **Cluster 3 - Constantly Running Devices:**  
   Devices that remain operational continuously with moderate energy usage.

---

## 🧮 **Key Steps in K-Means Clustering**

1. **Initialize Centroids:**  
   Randomly select `k` data points (centroids) from the dataset.

2. **Assign Clusters:**  
   Assign each device to the nearest centroid based on its Daily Usage and Idle Time.

3. **Update Centroids:**  
   Calculate new centroids as the mean of all devices in each cluster.

4. **Convergence:**  
   Repeat until centroids stabilize or a maximum number of iterations is reached.

---

## 📊 **Visualization**
The clusters are plotted using Plotly.js with color-coded markers:
- **Red:** High energy usage devices.
- **Blue:** Idle-efficient devices.
- **Green:** Constantly running devices.

**Sample Plot:**  
Each point in the plot represents a device, and hovering over it displays the device name, daily usage, and idle time.

```javascript
{
  x: clusterPoints.map(item => item.dailyUsage),
  y: clusterPoints.map(item => item.idleTime),
  mode: "markers",
  type: "scatter",
  name: "Cluster 1 (High Energy Usage)",
  marker: { size: 12, color: "red" },
  text: clusterPoints.map(item => 
      `Device: ${item.deviceName}<br>Daily Usage: ${item.dailyUsage.toFixed(2)}<br>Idle Time: ${item.idleTime.toFixed(2)}`)
}
