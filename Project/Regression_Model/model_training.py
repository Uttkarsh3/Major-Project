import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_json("grouped_household_size_devices.json")

# Ensure no null values (if any) in the dataset
data = data.dropna()

# Features (Household Size) and Target (Number of Devices)
X = data['Household Size'].values.reshape(-1, 1)  # Features: Household Size
y = data['Average Number of Devices'].values  # Target: Average Number of Devices

# Step 1: Split the data into training and testing sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 3: Predict the values using the test set
y_pred = model.predict(X_test)

# Step 4: Evaluate the model
print(f"R² Score: {r2_score(y_test, y_pred)}")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred)}")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred)}")

# Step 5: Visualization of the results
plt.figure(figsize=(10, 6))

# Plot the actual data points
plt.scatter(X_test, y_test, color='blue', label='Actual Data')

# Plot the predicted values
plt.plot(X_test, y_pred, color='red', label='Predicted Data')

# Add titles and labels
plt.title("Actual vs Predicted: Household Devices vs Household Size")
plt.xlabel("Household Size")
plt.ylabel("Average Number of Devices")
plt.legend()

# Show the plot
plt.show()

# Create a residual plot (Optional: To check for anomalies)
residuals = y_test - y_pred
sns.residplot(X_test.flatten(), residuals, lowess=True, color="g", line_kws={'color': 'red', 'lw': 1})
plt.title("Residual Plot")
plt.xlabel("Household Size")
plt.ylabel("Residuals (Actual - Predicted)")
plt.show()
