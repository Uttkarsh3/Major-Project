import pandas as pd

# Load the dataset
data = pd.read_csv("household_devices_dataset.csv")

# Save the dataset as a JSON file
data.to_json("household_devices_dataset.json", orient="records")

print("Dataset saved as household_devices_dataset.json")