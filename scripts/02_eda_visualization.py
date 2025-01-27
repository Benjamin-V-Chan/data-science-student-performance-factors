import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
data = pd.read_csv('data/cleaned_data.csv')

# Descriptive statistics
print(data.describe())

# Visualization: Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('outputs/visualizations/correlation_heatmap.png')

# Visualization: Target variable distribution
sns.histplot(data['Exam_Score'], kde=True, bins=20)
plt.title('Distribution of Exam Scores')
plt.savefig('outputs/visualizations/exam_score_distribution.png')