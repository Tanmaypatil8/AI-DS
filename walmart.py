import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
# Read the dataset
df = pd.read_csv("C:/Users/tanma/PycharmProjects/dataset/walmart.csv")
data = df.to_numpy()
# Display the dataset
print(df)
reg=LinearRegression()

# Initialize LabelEncoder
le = LabelEncoder()



# Optionally drop the original 'Date' column

# Dealing with Missing Values
print(df.isnull().sum())
'''
#Dealing with outliers
sns.boxplot(df['Store'])
plt.show()
sns.boxplot(df['Dept'])
plt.show()
sns.boxplot(df['Date'])
plt.show()
sns.boxplot(df['Weekly_Sales'])
plt.show()
sns.boxplot(df['IsHoliday'])
plt.show()'''
# Define a function to handle outliers
'''def handle_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR

    df[column] = df[column].apply(lambda x: upper_bound if x > upper_bound else (lower_bound if x < lower_bound else x))
    return df

# Call the function to handle outliers for the 'Weekly_Sales' column
df = handle_outliers(df, 'Weekly_Sales')'''

# Visualize boxplot after handling outliers
'''sns.boxplot(df['Weekly_Sales'])
plt.show()'''


# Generate example data
true_values = np.array([1, 2, 3, 4, 5])
predicted_values = np.array([1.2, 1.8, 2.9, 3.7, 5.2])

# Fit and transform 'Date' column
df['Date'] = le.fit_transform(df['Date'])
# One-hot encode 'Date' column
encoded_df = pd.get_dummies(df, columns=['Date'])

x = df.drop(columns=['Weekly_Sales', 'Date'])
y = df['Weekly_Sales']

X_train, X_test, Y_train, Y_test = train_test_split(x, y, random_state=1, test_size=0.2)

train = reg.fit(X_train, Y_train)
y_pred = reg.predict(X_test)

mse = mean_squared_error(true_values, predicted_values)
print("Mean Squared Error:", mse)
