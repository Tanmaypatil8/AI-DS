import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Read the CSV file into a DataFrame
df = pd.read_csv("C:/Users/tanma/PycharmProjects/dataset/loan.csv")

# Fill missing values in categorical columns with mode
categorical_columns = ['Gender', 'Married', 'Dependents', 'Self_Employed']
for column in categorical_columns:
    mode_value = df[column].mode()[0]
    df[column] = df[column].fillna(mode_value)

# Fill missing values in numerical columns with mean
numerical_columns = ['LoanAmount', 'Loan_Amount_Term', 'Credit_History']
for column in numerical_columns:
    mean_value = df[column].mean()
    df[column] = df[column].fillna(mean_value)

# Define a function to remove outliers using the IQR method
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    df_filtered = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df_filtered

# Specify the numerical columns to handle outliers
numerical_columns = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

# Remove outliers from each numerical column
for column in numerical_columns:
    df = remove_outliers_iqr(df, column)

# Separate features and target variable
X = df.drop(columns=['Loan_Status'])  # Features
y = df['Loan_Status']  # Target variable

# Apply one-hot encoding to categorical features
X_encoded = pd.get_dummies(X)

# Display class distribution before oversampling and undersampling
print("Class distribution before resampling:")
print(y.value_counts())

# Apply RandomOverSampler for oversampling
oversampler = RandomOverSampler(random_state=42)
X_over, y_over = oversampler.fit_resample(X_encoded, y)
# Display class distribution after oversampling
print("\nClass distribution after oversampling:")
print(y_over.value_counts())

# Apply RandomUnderSampler for undersampling
undersampler = RandomUnderSampler(random_state=42)
X_under, y_under = undersampler.fit_resample(X_encoded, y)

# Display class distribution after undersampling
print("\nClass distribution after undersampling:")
print(y_under.value_counts())

# Check for remaining string values in the DataFrame after one-hot encoding
print(X_over.info())

# Check for missing values in the DataFrame
print(X_over.isnull().sum())

# Inspect a sample of the data
print(X_over.head())

# Verify encoding by examining the columns
print(X_over.columns)

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_over, y_over, test_size=0.2, random_state=42)

# Initialize Random Forest classifier
rf_classifier = RandomForestClassifier(random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Calculate accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)
