import json
import random

# Load the device configuration from the JSON file
def load_device_config(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Generate static and dynamic attributes for devices
def generate_dataset(device_config):
    dataset = []
    household_sizes = ["Low", "Medium", "High"]
    peak_times = ["Morning", "Afternoon", "Evening"]

    # Static attributes for devices
    device_attributes = {
        "AC": {"Type": "Luxury", "Power": 2000, "Idle Power": 10},
        "Fan": {"Type": "Essential", "Power": 75, "Idle Power": 5},
        "LightBulb": {"Type": "Essential", "Power": 60, "Idle Power": 0},
        "Refrigerator": {"Type": "Essential", "Power": 150, "Idle Power": 20},
        "WashingMachine": {"Type": "Luxury", "Power": 500, "Idle Power": 10},
        "TV": {"Type": "Entertainment", "Power": 100, "Idle Power": 5},
    }

    # Generate data for each household size
    for household_size in household_sizes:
        for device_name, count in device_config[household_size].items():
            for _ in range(count):
                daily_usage = round(random.uniform(1, 8), 2)  # Active use (1–8 hours)
                idle_time = round(24 - daily_usage, 2)  # Idle time
                power = device_attributes[device_name]["Power"]
                idle_power = device_attributes[device_name]["Idle Power"]

                # Calculate daily energy consumption
                daily_energy_consumption = round(
                    ((power * daily_usage) + (idle_power * idle_time)) / 1000, 2
                )

                # Generate a device entry
                device_entry = {
                    "Device Name": device_name,
                    "Type": device_attributes[device_name]["Type"],
                    "Voltage": 230,
                    "Power": power,
                    "Idle Power": idle_power,
                    "Daily Usage": daily_usage,
                    "Idle Time": idle_time,
                    "Daily Energy Consumption (kWh)": daily_energy_consumption,
                    "Peak Time": random.choice(peak_times),
                    "Usage Frequency (days/week)": random.randint(1, 7),
                    "Household Size": household_size,
                }

                dataset.append(device_entry)

    return dataset

# Save dataset to a JSON file
def save_dataset(dataset, output_file):
    with open(output_file, 'w') as file:
        json.dump(dataset, file, indent=4)

# Main function
def main():
    device_config_file = "deviceConfig.json"
    output_file = "householdDeviceDataset.json"

    # Load device configuration
    device_config = load_device_config(device_config_file)

    # Generate dataset
    dataset = generate_dataset(device_config)

    # Save the dataset to a JSON file
    save_dataset(dataset, output_file)
    print(f"Dataset saved to {output_file}")

# Run the script
if __name__ == "__main__":
    main()
