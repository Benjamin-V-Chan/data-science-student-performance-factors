# data-science-student-performance-factors

## Project Overview
This project analyzes factors affecting student performance and builds a regression model to predict exam scores based on various parameters. It includes data preprocessing, exploratory data analysis, visualization, model training, and evaluation.

## Folder Structure
```
project-root/
├── data/
│   ├── StudentPerformanceFactors.csv  # Raw dataset
│   ├── cleaned_data.csv               # Preprocessed dataset
├── scripts/
│   ├── 01_data_preprocessing.py       # Data preprocessing script
│   ├── 02_eda_visualization.py        # Exploratory data analysis and visualization
│   ├── 03_model_training.py           # Model training script
│   ├── 04_evaluation_results.py       # Model evaluation script
├── outputs/
│   ├── visualizations/                # Saved visualizations
│   ├── models/                        # Saved models
│   ├── evaluation/                    # Evaluation reports
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```

## Usage

### 1. Setup the Project:
- Clone the repository.
- Ensure you have Python installed.
- Install required dependencies using the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```

### 2. Run the Scripts:

#### Step 1: Data Preprocessing
Preprocess the raw dataset by running:
```bash
python scripts/01_data_preprocessing.py
```
This script will clean the data and save the processed dataset to `data/cleaned_data.csv`.

#### Step 2: Exploratory Data Analysis and Visualization
Generate descriptive statistics and visualizations:
```bash
python scripts/02_eda_visualization.py
```
The visualizations will be saved in the `outputs/visualizations/` folder.

#### Step 3: Model Training
Train the regression model using:
```bash
python scripts/03_model_training.py
```
The trained model will be saved in the `outputs/models/` folder.

#### Step 4: Model Evaluation
Evaluate the model’s performance with:
```bash
python scripts/04_evaluation_results.py
```
The evaluation report will be saved in the `outputs/evaluation/` folder.

## Requirements
- Python 3.8 or higher
- Required Python packages (install via `pip install -r requirements.txt`):
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - joblib

## Acknowledgments
- **Dataset Name:** Student Performance Factors
- **Dataset Author:** Practice Data Analysis With Me
- **Dataset Source:** [Kaggle](https://www.kaggle.com/datasets/lainguyn123/student-performance-factors)