# Fitness Premium Membership Prediction

A Jupyter notebook demonstrating a scikit-learn machine-learning pipeline that predicts whether a fitness app user has premium membership from basic profile and workout data. The example focuses on handling missing values and categorical features consistently during training and prediction.

## Project Contents

- `Project (2).ipynb` - data inspection, missing-value visualization, preprocessing pipeline, model training, and a sample prediction.
- `fitness_data.csv` - fitness user dataset with 2,000 records.

## Dataset

The CSV contains 2,000 user records and the following columns:

| Column | Description |
| --- | --- |
| `is_premium` | Binary target indicating premium membership (0 or 1). |
| `age` | User age. |
| `weekly_mins` | User's weekly workout minutes. |
| `avg_hr` | Average heart rate; 200 values are missing. |
| `workout_type` | Workout category, such as HIIT, Running, Yoga, Strength Training, or Cycling. |
| `region` | User region: North, South, East, or West. |

## Workflow

1. Load and inspect the dataset, including duplicate and missing-value checks.
2. Split the data into training and test sets (75% training, 25% test).
3. Visualize missing values in the input features.
4. Build a preprocessing pipeline that imputes numeric missing values with the median, standardizes numeric columns, and one-hot encodes categorical columns.
5. Combine preprocessing with logistic regression in a single scikit-learn pipeline and fit it on the training data.
6. Pass a sample user with a missing average heart rate through the trained pipeline to produce a premium-membership prediction.

The notebook demonstrates pipeline-based preprocessing to keep transformations consistent between training and prediction and to fit preprocessing steps using training data only.

## Requirements

- Python 3.9 or later
- Jupyter Notebook or JupyterLab
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- joblib

Install the Python packages with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn joblib jupyter
```

## Run the Notebook

1. Clone or download this repository.
2. Install the requirements above.
3. Open `Project (2).ipynb` in Jupyter Notebook, JupyterLab, or VS Code.
4. Run the cells from top to bottom.

**Dataset path note:** The notebook currently loads `data/fitness_data.csv`, while the CSV in this repository is at the project root. Either create a `data` directory and move the CSV into it, or change the notebook's `pd.read_csv` path to `fitness_data.csv` before running.

## Scope and Limitations

This is an instructional example, not a production-ready model. Although the notebook creates a test split, it does not calculate test-set metrics or compare predictions against held-out labels. It also does not save the trained pipeline; `joblib` is imported but no model-export step is implemented. The sample prediction should not be interpreted as evidence of model accuracy or as a real membership decision.
