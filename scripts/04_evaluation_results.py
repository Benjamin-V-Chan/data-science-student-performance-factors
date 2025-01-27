import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load the test dataset and model
data = pd.read_csv('data/cleaned_data.csv')
model = joblib.load('outputs/models/linear_regression_model.pkl')

# Define features and target
X = data.drop(columns='Exam_Score')
y = data['Exam_Score']

# Predict
y_pred = model.predict(X)

# Evaluate
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Save results
with open('outputs/evaluation/evaluation_report.txt', 'w') as f:
    f.write(f'MAE: {mae}\nMSE: {mse}\nR2 Score: {r2}\n')