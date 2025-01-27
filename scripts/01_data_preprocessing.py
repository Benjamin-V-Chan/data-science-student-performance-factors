import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Load the dataset
data = pd.read_csv('data/StudentPerformanceFactors.csv')

# Handle missing values
data.fillna(data.median(numeric_only=True), inplace=True)

# Encode categorical variables
categorical_cols = data.select_dtypes(include=['object']).columns
data_encoded = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Normalize numerical variables
scaler = StandardScaler()
numeric_cols = data_encoded.select_dtypes(include=['float64', 'int64']).columns
data_encoded[numeric_cols] = scaler.fit_transform(data_encoded[numeric_cols])

# Save the cleaned dataset
data_encoded.to_csv('data/cleaned_data.csv', index=False)