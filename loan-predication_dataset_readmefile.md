
# Loan Status Prediction using Random Forest Classifier

This project is a machine learning application that predicts the loan status of applicants based on their information. The dataset is preprocessed, balanced using oversampling and undersampling techniques, and then a Random Forest Classifier is trained to make the predictions.

## Overview

The Loan Status Prediction system is implemented in Python and utilizes various libraries for data manipulation, handling imbalanced datasets, and machine learning. The primary objective is to classify whether a loan will be approved or not.

## Features

- **Data Preprocessing**: Handles missing values and removes outliers.
- **Resampling Techniques**: Balances the dataset using Random OverSampling and Random UnderSampling.
- **Model Training**: Trains a Random Forest Classifier on the processed data.
- **Model Evaluation**: Evaluates the model using accuracy score.

## Technologies Used

- **Python**: The main programming language used for the application.
- **pandas**: A library for data manipulation and analysis.
- **imbalanced-learn (imblearn)**: A library to handle imbalanced datasets, used for oversampling and undersampling.
- **scikit-learn**: A library for machine learning, used for model building and evaluation.

## Installation

To run this project, ensure you have Python installed on your system. Then, install the required libraries using pip:

```bash
pip install pandas imbalanced-learn scikit-learn

# Loan Status Prediction using Random Forest Classifier

This project is a machine learning application that predicts the loan status of applicants based on their information. The dataset is preprocessed, balanced using oversampling and undersampling techniques, and then a Random Forest Classifier is trained to make the predictions.

## Dataset

The dataset (`loan.csv`) contains information about loan applicants, including attributes such as:
- Gender
- Married
- Dependents
- Self_Employed
- ApplicantIncome
- CoapplicantIncome
- LoanAmount
- Loan_Amount_Term
- Credit_History
- Loan_Status

## Data Preprocessing

### Handling Missing Values

- **Categorical Columns**: Missing values in 'Gender', 'Married', 'Dependents', and 'Self_Employed' are filled with their respective mode values.
- **Numerical Columns**: Missing values in 'LoanAmount', 'Loan_Amount_Term', and 'Credit_History' are filled with their respective mean values.

### Outlier Removal

- **Interquartile Range (IQR) Method**: Outliers in 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', and 'Loan_Amount_Term' are removed using the IQR method.

### One-Hot Encoding

- **Categorical Features**: Categorical features are converted into numerical format using one-hot encoding.

## Resampling Techniques

### Oversampling

- **Random OverSampling**: Balances the dataset by increasing the number of instances in the minority class.

### Undersampling

- **Random UnderSampling**: Balances the dataset by reducing the number of instances in the majority class.

## Model Training and Evaluation

### Random Forest Classifier

- **Initialization**: The Random Forest Classifier is initialized with a random state for reproducibility.
- **Training**: The classifier is trained on the training set.
- **Prediction**: The classifier makes predictions on the test set.
- **Evaluation**: The accuracy score is calculated to evaluate the model's performance.

## Results

The script produces the following evaluation result:

- **Accuracy**: The accuracy of the Random Forest Classifier on the test set is displayed.

# Acknowledgments

pandas: For data manipulation and analysis.
imbalanced-learn: For handling imbalanced datasets.
scikit-learn: For machine learning tools and techniques