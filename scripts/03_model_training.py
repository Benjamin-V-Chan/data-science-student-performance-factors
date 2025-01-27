import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load the cleaned dataset
data = pd.read_csv('data/cleaned_data.csv')

# Define features and target
X = data.drop(columns='Exam_Score')
y = data['Exam_Score']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'outputs/models/linear_regression_model.pkl')