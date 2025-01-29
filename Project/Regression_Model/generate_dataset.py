import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
num_samples = 100  # Number of households

# Features
household_size = np.random.randint(1, 8, size=num_samples)  # Family size (1 to 7 members)
income = np.random.randint(20000, 150000, size=num_samples)  # Annual income ($20,000 to $150,000)
num_rooms = np.random.randint(2, 8, size=num_samples)  # Number of rooms in the house (2 to 7)

# Target variable (number of devices)
# Simulate a relationship: more family members, income, and rooms → more devices
base_devices = household_size * 2  # Base devices based on family size
income_effect = (income / 10000).astype(int)  # Additional devices based on income
room_effect = num_rooms  # Additional devices based on the number of rooms

# Add some random noise to make the data realistic
noise = np.random.randint(-3, 4, size=num_samples)

# Total devices
num_devices = base_devices + income_effect + room_effect + noise
num_devices = np.clip(num_devices, 1, None)  # Ensure no negative devices

# Create a DataFrame
data = pd.DataFrame({
    "Household Size": household_size,
    "Annual Income ($)": income,
    "Number of Rooms": num_rooms,
    "Number of Devices": num_devices
})

# Save the dataset to a CSV file
data.to_csv("household_devices_dataset.csv", index=False)

# Display the first 10 rows
print(data.head(10))
