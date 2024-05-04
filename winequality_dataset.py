import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Read the dataset
df = pd.read_csv("C:/Users/tanma/PycharmProjects/dataset/winequalityN.csv")

# Drop the 'type' column if it exists
if 'type' in df.columns:
    df.drop(columns=['type'], inplace=True)

# Handling missing values
mean_fixed_acidity = df['fixed acidity'].mean()
df.fillna({'fixed acidity': mean_fixed_acidity}, inplace=True)

mean_volatile_acidity = df['volatile acidity'].mean()
df.fillna({'volatile acidity': mean_volatile_acidity}, inplace=True)

mean_citric_acid = df['citric acid'].mean()
df.fillna({'citric acid': mean_citric_acid}, inplace=True)

mean_residual_sugar = df['residual sugar'].mean()
df.fillna({'residual sugar': mean_residual_sugar}, inplace=True)

mean_chlorides = df['chlorides'].mean()
df.fillna({'chlorides': mean_chlorides}, inplace=True)

mean_pH = df['pH'].mean()
df.fillna({'pH': mean_pH}, inplace=True)

mean_sulphates = df['sulphates'].mean()
df.fillna({'sulphates': mean_sulphates}, inplace=True)

# One-hot encoding for 'type' column if it exists
if 'type' in df.columns:
    df = pd.get_dummies(df, columns=['type'])

# Handling outliers
def handle_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR
    df[column] = df[column].apply(lambda x: upper_bound if x > upper_bound else (lower_bound if x < lower_bound else x))
    return df

# Call the function for each column
columns_to_handle_outliers = df.columns.tolist()  # Handle outliers for all numerical columns
columns_to_handle_outliers.remove('quality')  # Remove 'quality' column
for column in columns_to_handle_outliers:
    df = handle_outliers(df, column)

# Define features and target variable
x = df.drop('quality',axis=1)
y = df['quality']

# Initialize Linear Regression model
reg = LinearRegression()

# Split data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Train the model
reg.fit(x_train, y_train)

# Predict on the test set
y_pred = reg.predict(x_test)

# Evaluate the model using Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
