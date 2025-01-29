import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the dataset
data = pd.read_json("household_devices_dataset.json")

# Define Features (X) and Target (y)
X = data[['Household Size']]
y = data['Number of Devices']

# Split the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model on the training set
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model on the testing set
y_pred = model.predict(X_test)
print("Model Evaluation:")
print("R² Score:", r2_score(y_test, y_pred))
print("Mean Absolute Error (MAE):", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))

# Save the evaluation metrics to a JSON file
evaluation_metrics = {
    'r2': r2_score(y_test, y_pred),
    'mae': mean_absolute_error(y_test, y_pred),
    'mse': mean_squared_error(y_test, y_pred)
}

# Save the evaluation metrics to 'model_evaluation.json'
with open('model_evaluation.json', 'w') as f:
    json.dump(evaluation_metrics, f)

print("Model Evaluation Metrics saved as model_evaluation.json")




# Create input as a DataFrame with the same column name
household_sizes = pd.DataFrame({'Household Size': np.arange(1, 11)})
predictions = model.predict(household_sizes)


# Create a DataFrame with predictions
predictions_df = pd.DataFrame({
    'Household Size': range(1, 11),
    'Predicted Number of Devices': predictions.round().astype(int)
})

# Save the predictions to a JSON file
predictions_df.to_json("predictions.json", orient="records")

print("Predictions saved as predictions.json")



#R² Score: 0.5152402348010932
#This means that the model explains about 51.5% of the variance in the target variable, which is moderate performance.

#Mean Absolute Error (MAE): 3.8368210036213135
#On average, the model's predictions are approximately 3.84 devices off from the actual values.

#Mean Squared Error (MSE): 20.91253627068084
#This is the average squared difference between predicted and actual values (higher values indicate more error).