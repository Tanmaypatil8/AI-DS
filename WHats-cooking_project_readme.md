
# What's Cooking Cuisine Prediction using Random Forest Classifier

This project is a machine learning application that predicts the type of cuisine based on ingredients used in recipes. The dataset is preprocessed, and then a Random Forest Classifier is trained to make the predictions.

## Overview

The project reads a dataset in JSON format, performs data preprocessing, and uses a Random Forest Classifier to predict the cuisine of a recipe based on its ingredients. The classifier's performance is evaluated using accuracy score.

## Dataset

The dataset (`train-whats-cooking.json`) contains information about recipes, including:
- `id`: Unique identifier for each recipe.
- `cuisine`: Type of cuisine (target variable).
- `ingredients`: List of ingredients used in the recipe.

## Data Preprocessing

### One-Hot Encoding

- The `cuisine` column is one-hot encoded to convert the categorical variable into a numerical format. This creates new columns for each cuisine type with binary values (0 or 1).

### Feature and Target Variable Separation

- **Features (X)**: All columns except `id`, `ingredients`, and the original `cuisine` column.
- **Target Variable (y)**: One-hot encoded columns representing the cuisine types.

## Model Training and Evaluation

### Random Forest Classifier

- **Initialization**: A Random Forest Classifier is initialized with 100 trees (`n_estimators=100`) and a maximum depth of 5 (`max_depth=5`) to prevent overfitting.
- **Training**: The classifier is trained on the training set.
- **Prediction**: The classifier makes predictions on the test set.
- **Evaluation**: The accuracy score is calculated to evaluate the model's performance.

## Results

The script produces the following evaluation result:

- **Accuracy**: 0.7757

The accuracy of the Random Forest Classifier on the test set is 77.57%.

## Running the Script

To run the script:

1. Ensure Python is installed on your system.
2. Install the required libraries (`pandas`, `scikit-learn`) using pip if not already installed.
3. Place the `train-whats-cooking.json` dataset in the specified path (`C:/Users/tanma/PycharmProjects/dataset/train-whats-cooking.json`).
4. Run the script (`<script_name>.py`) using the Python interpreter.


python <script_name>.py

# Next Steps

- Experiment with different models (e.g., Gradient Boosting, XGBoost) for comparison.
- Explore additional feature engineering techniques to enhance model performance.
- Implement cross-validation for more robust model evaluation.
- Fine-tune model hyperparameters to optimize performance.

# Acknowledgments

- pandas: For data manipulation and analysis.
- scikit-learn: For machine learning tools and techniques.