# Titanic Dataset Analysis and Random Forest Classifier

This Python script analyzes the Titanic dataset using a Random Forest Classifier to predict the Embarked variable. The analysis includes data preprocessing steps, outlier handling, model training, and evaluation.

## Overview

The purpose of this script is to demonstrate a machine learning workflow using the Titanic dataset. It employs a Random Forest Classifier to predict the port of embarkation (Embarked) based on other attributes.

## Dataset

The dataset used (`train.csv`) contains information about passengers aboard the Titanic, including attributes like Sex, Age, Pclass, Fare, SibSp, Parch, Ticket, Cabin, Embarked, and Survived.

## Data Preprocessing

### Handling Missing Values:

Missing values in Age are filled with the mean age.
Missing values in Embarked are replaced with a placeholder ("nun").
Missing values in Cabin are replaced with a placeholder ("nun").

### Encoding Categorical Variables:

- Sex and Ticket columns are encoded using LabelEncoder to convert categorical variables into numerical format.

## Outlier Handling

Outliers in numerical columns (Age, SibSp, Parch, Fare) are handled using the Interquartile Range (IQR) method to cap extreme values.

## Model Training and Evaluation

### Feature Selection:

Feature selection process is not implemented in this version.

### Model Training:

The script utilizes a RandomForestClassifier to train the model.

### Splitting Data:

The dataset is split into training and testing sets (80% training, 20% testing).

### Evaluation Metrics:

- Mean Squared Error (MSE) and Accuracy score are used to evaluate the model's performance.

## Results

The script provides the following evaluation results:

- **Mean Squared Error (MSE):** 0.346
  The MSE indicates the average squared difference between predicted and actual values of the target variable (Embarked).

- **Accuracy of Random Forest:** 0.888
  The accuracy score represents the proportion of correctly predicted Embarked labels out of all samples in the test set.

These metrics suggest that the Random Forest Classifier performs well in predicting the port of embarkation based on the provided attributes.

## Running the Script

To run the script:

1. Ensure Python is installed on your system.
2. Install the required libraries (`pandas`, `matplotlib`, `seaborn`, `scikit-learn`) using pip if not already installed.
3. Place the `train.csv` dataset in the specified path (`C:/Users/tanma/PycharmProjects/dataset/train.csv`).
4. Run the script (`Titanic_dataSet.py`) using the Python interpreter.

## Next Steps

- Explore feature engineering techniques to improve model performance.
- Implement cross-validation for robust model evaluation.
- Experiment with hyperparameter tuning to optimize model parameters.
