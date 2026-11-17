# Project 1: Triage Data Cleaning and Prediction

## Overview

This project demonstrates how to prepare healthcare triage data for machine learning. It focuses on data quality, preprocessing, and building a complete classification pipeline for predicting patient priority levels.

## Files

- `data_cleaning.ipynb` — notebook with the full workflow
- `patient_data.csv` — patient record dataset used for the model

## Dataset

The dataset contains patient information such as:

- `age`
- `body_temp`
- `symptom_type`
- `priority`

The target column is `priority`, which indicates whether a case is `Standard` or `Urgent`.

## Workflow

The notebook covers:

1. loading the dataset
2. splitting train/test data
3. imputing missing age values
4. scaling numerical features
5. encoding categorical data
6. combining steps with `ColumnTransformer`
7. training a `LogisticRegression` model in a full pipeline
8. measuring accuracy on the test set

## Objective

The goal is to build a clean, reusable preprocessing workflow that keeps training and test transformations consistent while training a predictive model.

## Technologies Used

- Python
- pandas
- scikit-learn
- Jupyter Notebook
