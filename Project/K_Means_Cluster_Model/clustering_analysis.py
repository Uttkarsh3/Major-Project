import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Step 1: Load the dataset
df = pd.read_csv("preprocessed_dataset.csv")

# Step 2: Select features for clustering
features = df[["Daily Usage", "Idle Time", "Daily Energy Consumption (kWh)"]]

# Step 3: Standardize the data
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Step 4: Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)  # Use 3 clusters
df["Cluster"] = kmeans.fit_predict(scaled_features)

# Step 5: Save the clustered data for further analysis
df.to_csv("clustered_devices.csv", index=False)
print("Clustered data saved to 'clustered_devices.csv'")
