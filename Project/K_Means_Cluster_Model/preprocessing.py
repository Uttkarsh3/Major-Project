import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

# Function to preprocess the dataset
def preprocess_data(input_file, output_file):
    # Load the dataset
    df = pd.read_json(input_file)

    # Encode categorical columns
    label_encoder = LabelEncoder()
    df['Type'] = label_encoder.fit_transform(df['Type'])
    df['Peak Time'] = label_encoder.fit_transform(df['Peak Time'])
    df['Household Size'] = label_encoder.fit_transform(df['Household Size'])

    # Normalize numerical features
    scaler = MinMaxScaler()
    numerical_features = ['Voltage', 'Power', 'Idle Power', 'Daily Usage', 'Idle Time', 'Daily Energy Consumption (kWh)']
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    # Select relevant features, including the device name
    selected_features = ['Device Name', 'Daily Usage', 'Idle Time', 'Daily Energy Consumption (kWh)', 'Type', 'Peak Time', 'Household Size']
    df_selected = df[selected_features]

    # Save preprocessed data to a new file
    df_selected.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

# Run the preprocessing
if __name__ == "__main__":
    preprocess_data('householdDeviceDataset.json', 'preprocessed_dataset.csv')
