What K-Means Does:
Input Data:

Each device has two attributes:
Daily Usage (Normalized): Represents how much energy the device uses daily.
Idle Time (Normalized): Represents how long the device remains idle.
Clustering:

The K-Means algorithm groups devices into k clusters based on these two attributes.
The clustering is done by minimizing the distance between data points (devices) and the centroids (mean points) of each cluster.
Iterative Process:

Step 1: Randomly initialize k centroids (in your project, k = 3).
Step 2: Assign each device to the nearest centroid (cluster).
Step 3: Update the centroids based on the mean position of all points in the cluster.
Step 4: Repeat until the centroids stabilize (convergence).
What Clusters Mean in the Project:
Cluster 1 (High Energy Usage Devices):

Devices that consume a lot of electricity daily.
Cluster 2 (Energy-Efficient Idle Devices):

Devices that are idle most of the time and consume minimal energy.
Cluster 3 (Constantly Running Devices):

Devices that remain operational continuously with moderate energy usage.
Why K-Means is Useful Here:
Insightful Grouping: Helps you identify energy consumption patterns in devices.
Data Analysis: Makes it easier to optimize power usage by targeting specific clusters.
Visualization: The plot shows distinct clusters so users can visually understand how devices behave.
Visualization Enhancement:
The updated chart provides meaningful labels and descriptions for the clusters, making it easier to interpret.
Devices plotted in "Cluster 1" are flagged as heavy users, while those in "Cluster 2" might be idle-efficient ones.
