from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("C:/Users/tanma/PycharmProjects/dataset/Boston-house-price-data.csv")

print(df)

# Handling missing values
print(df.isnull().sum())

def handle_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df[column] = np.where(df[column] > upper_bound, upper_bound, df[column])
    df[column] = np.where(df[column] < lower_bound, lower_bound, df[column])

columns_to_handle_outliers = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'TAX', 'PTRATIO', 'B', 'LSTAT']
for column in columns_to_handle_outliers:
    handle_outliers(df, column)

# Additional step: handle outliers in target variable (MEDV)
handle_outliers(df, 'MEDV')

# Visualization after handling outliers
for column in columns_to_handle_outliers:
    sns.boxplot(y=column, data=df)
    plt.show()

reg = LinearRegression()

x = df.drop('MEDV', axis=1)
y = df['MEDV']

X_train, X_test, Y_train, Y_test = train_test_split(x, y, random_state=1, test_size=0.2)

train = reg.fit(X_train, Y_train)
y_pred = reg.predict(X_test)

score = mean_squared_error(Y_test, y_pred)
print("Mean Squared Error:", score)
