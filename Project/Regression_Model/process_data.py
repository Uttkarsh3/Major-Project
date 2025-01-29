import pandas as pd

# Load the dataset
data = pd.read_json("household_devices_dataset.json")

# Convert Household Size to integer (removing any decimal values)
data['Household Size'] = data['Household Size'].round().astype(int)

# Group by Household Size and calculate the average number of devices
grouped_data = data.groupby("Household Size")["Number of Devices"].mean().reset_index()

# Round off the average number of devices to the nearest integer
grouped_data["Number of Devices"] = grouped_data["Number of Devices"].round().astype(int)

# Rename columns
grouped_data.columns = ["Household Size", "Average Number of Devices"]

# Save the grouped data as a JSON file
grouped_data.to_json("grouped_household_size_devices.json", orient="records")

print("Grouped data with rounded values (no decimals) saved as grouped_household_size_devices.json")
