# Triage Data Cleaning and Prediction

This project analyzes a patient triage dataset and demonstrates how to prepare data for a machine learning model using scikit-learn pipelines.

## Project goal

The notebook builds a preprocessing workflow for predicting patient priority based on clinical and symptom information. It focuses on:

- handling missing values in the `age` column
- scaling numeric features
- encoding categorical data such as `symptom_type`
- combining all preprocessing steps into a `ColumnTransformer`
- training a `LogisticRegression` model inside a single pipeline
- evaluating the final model on a test set

## Dataset

The dataset is stored in `patient_data.csv` and contains the following columns:

- `age`
- `body_temp`
- `symptom_type`
- `priority`

### Dataset summary

- Total rows: 1000
- Missing age values: 100
- Priority classes:
  - Standard: 643
  - Urgent: 357
- Symptom categories:
  - Chest Pain
  - Fever
  - Fracture
  - Headache
  - Other

## Notebook workflow

The notebook follows this structure:

1. Load the dataset
2. Split into training and testing data
3. Train an imputer for missing age values
4. Scale numeric variables
5. One-hot encode categorical symptom data
6. Combine preprocessing steps with `ColumnTransformer`
7. Train a full `Pipeline` with a logistic regression model
8. Measure test accuracy

## Key technical concepts used

- `train_test_split`
- `SimpleImputer`
- `StandardScaler`
- `OneHotEncoder`
- `Pipeline`
- `ColumnTransformer`
- `LogisticRegression`

## Setup

Install the required Python libraries:

```bash
pip install pandas scikit-learn notebook
```

Open the notebook in Jupyter:

```bash
jupyter notebook
```

## Important note

The notebook uses a path similar to `data/patient_data.csv`, but in this workspace the CSV file is located at the project root as `patient_data.csv`. If the notebook fails to load the data, update the path to match the actual file location.

## Project status

This is an educational data-preprocessing and machine-learning notebook. It demonstrates a clean, professional workflow for preparing tabular healthcare data before model training.
