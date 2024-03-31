import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score


# Read the dataset
df = pd.read_csv("C:/Users/tanma/PycharmProjects/dataset/train.csv")
rf=RandomForestClassifier()
# print(df)


#Converting Input Attributes
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
df['Ticket'] = le.fit_transform(df['Ticket'])

# Split the data into features (X) and target variable
X = df.drop(['PassengerId','Name','Cabin'],axis=1)
X = X.drop('Embarked',axis=1)
y = df['Embarked']
# print(y)
le=LabelEncoder()
le.fit(y)
y=le.transform(y)
print(y)

#Dealing with Missing Values
print(df.isnull().sum())
df['Age']=df['Age'].fillna((df['Age'].mean()))
df['Embarked'] = df['Embarked'].fillna('nun')
# pd.set_option('display.max_rows', None)  # Show all rows
# pd.set_option('display.max_columns', None)
# print(df['Embarked'])
df['Cabin'] = df['Cabin'].fillna('nun')
print(df.isnull().sum())


#Dealing with outliers
'''
sns.boxplot(df['Survived'])
plt.show()
sns.boxplot(df['Pclass'])
plt.show()
sns.boxplot(df['Name'])
plt.show()
sns.boxplot(df['Sex'])
plt.show()
sns.boxplot(df['Age'])
plt.show()
sns.boxplot(df['SibSp'])
plt.show()
sns.boxplot(df['Parch'])
plt.show()
sns.boxplot(df['Ticket'])
plt.show()
sns.boxplot(df['Fare'])
plt.show()
sns.boxplot(df['Cabin'])
plt.show()
sns.boxplot(df['Embarked'])
plt.show()
'''

def handle_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    upper_bound = Q3 + 1.5 * IQR
    lower_bound = Q1 - 1.5 * IQR

    df[column] = df[column].apply(lambda x: upper_bound if x > upper_bound else (lower_bound if x < lower_bound else x))
    return df

# Call the function for each column
df = handle_outliers(df, 'Age')
df = handle_outliers(df, 'SibSp')
df = handle_outliers(df, 'Parch')
df = handle_outliers(df, 'Fare')
'''
for column in ['Age', 'SibSp', 'Parch', 'Fare']:
    sns.boxplot(df[column])
    plt.title(column)
    plt.show()
'''

#Feature selection (Not Done)


# Split the data into features (X) and target variable (y) ..... done

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train the model
rf.fit(X_train,y_train)

# Predict on the test set
y_pred=rf.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy of Random Tree:",accuracy)