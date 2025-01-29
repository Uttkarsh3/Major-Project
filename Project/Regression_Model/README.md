# ⚡ Device Energy Usage Prediction using Regression Model

This project implements a **Regression Model** to predict device energy consumption based on various factors such as daily usage and idle time. The model provides insights into expected energy consumption patterns, aiding in better power management.

---

## 🔧 **How It Works**

The regression model is trained to predict the **Daily Energy Usage** of devices based on the following input features:
- **Device Type:** Category or function of the device.
- **Idle Time:** Duration the device remains idle.
- **Operational Time:** Duration the device remains active.

---

## 🧮 **Key Steps in the Regression Process**

1. **Data Preprocessing:**  
   - Normalization of input data to bring values to a common scale.  
   - Handling missing or invalid values.

2. **Model Training:**  
   - A regression algorithm (like **Linear Regression**) is trained on the dataset to learn the relationship between input features and energy consumption.

3. **Prediction:**  
   - Based on new input data, the model predicts the device's daily energy usage.

4. **Evaluation:**  
   - Performance evaluation using metrics like **Mean Absolute Error (MAE)** and **R-squared (R²)**.

---

## 📊 **Visualization**

The model's predictions are visualized on an interactive chart using **Plotly.js**, comparing actual and predicted values.

**Sample Plot:**  
Each point represents a device with its predicted and actual energy consumption.

```javascript
{
  x: deviceData.map(item => item.deviceName),
  y: predictions.map(pred => pred.value),
  type: "bar",
  name: "Predicted Usage"
},
{
  x: deviceData.map(item => item.deviceName),
  y: actualValues.map(val => val),
  type: "bar",
  name: "Actual Usage"
}
