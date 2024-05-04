# Wine Quality Prediction using Linear Regression

## Overview

This Python script utilizes a Linear Regression model to predict the quality of wines based on various attributes from the dataset. The analysis involves data preprocessing, outlier handling, model training, and evaluation.

## Dataset

The dataset (`winequalityN.csv`) contains information about different attributes of wines, such as fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, pH, sulphates, and quality.

## Data Preprocessing

### Handling Missing Values

The script first addresses missing values by filling them with the mean values of respective columns (`fixed acidity`, `volatile acidity`, `citric acid`, `residual sugar`, `chlorides`, `pH`, and `sulphates`). This ensures that no data points are missing before training the model.

### One-Hot Encoding

If the dataset includes a categorical column (`type`), the script performs one-hot encoding to convert categorical variables into numerical format. This transformation is essential for machine learning algorithms that require numerical input.

## Outlier Handling

Outliers in numerical columns are handled using the Interquartile Range (IQR) method to cap extreme values. Outliers can negatively impact model performance, so this step helps in cleaning the data and reducing their influence.

## Model Training and Evaluation

### Linear Regression Model

The script defines features (`x`) and the target variable (`y`) based on the dataset. It then initializes a Linear Regression model and splits the data into training and testing sets. The model is trained using the training data (`x_train`, `y_train`).

After training, the model predicts the target variable (`y_pred`) for the test set (`x_test`). The performance of the model is evaluated using Mean Squared Error (MSE), which measures the average squared difference between predicted and actual wine quality values in the test set.

## Results

The script produces the following evaluation result:

- **Mean Squared Error (MSE):** 0.5297

The MSE value represents the average squared difference between predicted and actual wine quality values in the test set, indicating the accuracy of the Linear Regression model in predicting wine quality.


