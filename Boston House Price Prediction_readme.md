# Boston House Price Prediction

This project is a comprehensive analysis and prediction of Boston house prices using Linear Regression. The dataset used is from the Boston House Price dataset, which includes various attributes that affect house prices.

## Overview

The project aims to predict the median value of owner-occupied homes (MEDV) in the Boston area. It involves data preprocessing, handling missing values, outlier detection and removal, visualization, and applying a Linear Regression model to predict house prices.

## Dataset

The dataset (Boston-house-price-data.csv) contains information about various attributes of houses in Boston, including:

- CRIM: Per capita crime rate by town
- ZN: Proportion of residential land zoned for lots over 25,000 sq. ft.
- INDUS: Proportion of non-retail business acres per town
- CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- NOX: Nitric oxides concentration (parts per 10 million)
- RM: Average number of rooms per dwelling
- AGE: Proportion of owner-occupied units built prior to 1940
- DIS: Weighted distances to five Boston employment centers
- RAD: Index of accessibility to radial highways
- TAX: Full-value property tax rate per $10,000
- PTRATIO: Pupil-teacher ratio by town
- B: 1000(Bk - 0.63)^2 where Bk is the proportion of Black residents by town
- LSTAT: Percentage of lower status of the population
- MEDV: Median value of owner-occupied homes in $1000s

## Data Preprocessing

### Handling Missing Values

- All missing values in the dataset are checked and handled.
- The dataset did not have any missing values as indicated by `df.isnull().sum()`.

### Outlier Detection and Removal

Outliers in the dataset are handled using the Interquartile Range (IQR) method. The following steps are taken:

1. **Calculate IQR for each numerical column.**
2. **Define the lower and upper bounds for outliers.**
3. **Cap the outliers to the lower and upper bounds.**

The following columns had outliers handled: `CRIM`, `ZN`, `INDUS`, `CHAS`, `NOX`, `TAX`, `PTRATIO`, `B`, `LSTAT`, and `MEDV`.

## Visualization

Boxplots are generated for each column after handling outliers to visualize the distribution and detect any remaining anomalies.

## Model Training and Evaluation

### Linear Regression

- The Linear Regression model is used for predicting house prices.
- The dataset is split into training and testing sets using an 80-20 split.
- The model is trained on the training set and evaluated on the test set.

### Performance Metrics

- **Mean Squared Error (MSE)** is used to evaluate the model's performance.
- The calculated MSE for the model is `13.470545957415728`.

## Results

The Linear Regression model's performance on the test set is evaluated using Mean Squared Error (MSE), which indicates the average squared difference between the predicted and actual values.

**Mean Squared Error: 13.470545957415728**

## Running the Script

To run the script:

1. Ensure Python is installed on your system.
2. Install the required libraries (`pandas`, `seaborn`, `numpy`, `scikit-learn`) using `pip` if not already installed.
3. Place the `Boston-house-price-data.csv` dataset in the specified path (`C:/Users/tanma/PycharmProjects/dataset/Boston-house-price-data.csv`).
4. Run the script (`<script_name>.py`) using the Python interpreter.
python <script_name>.py

## Next Steps

- **Experiment with different models** (e.g., Decision Trees, Random Forests, XGBoost) for comparison.
- **Explore additional feature engineering techniques** to enhance model performance.
- **Implement cross-validation** for more robust model evaluation.
- **Fine-tune model hyperparameters** to optimize performance.

## Acknowledgments

- **pandas**: For data manipulation and analysis.
- **seaborn**: For data visualization.
- **numpy**: For numerical computations.
- **scikit-learn**: For machine learning tools and techniques.

