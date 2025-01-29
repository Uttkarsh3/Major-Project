// Function to fetch and display the model evaluation metrics
document.getElementById('evaluateButton').addEventListener('click', function() {
    // Fetch the evaluation metrics from the 'model_evaluation.json' file
    fetch('model_evaluation.json')
      .then(response => response.json())
      .then(data => {
        // Display the metrics in an alert box
        const r2 = data.r2;
        const mae = data.mae;
        const mse = data.mse;
  
        alert(`Model Evaluation Metrics:\n
        R² Score: ${r2}\n
        Mean Absolute Error (MAE): ${mae}\n
        Mean Squared Error (MSE): ${mse}`);
      })
      .catch(error => {
        console.error('Error fetching model evaluation data:', error);
        alert('Error fetching evaluation metrics.');
      });
  });
  