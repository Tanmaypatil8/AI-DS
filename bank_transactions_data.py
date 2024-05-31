import pandas as pd
# import sweetviz as sv
# from ydata_profiling import ProfileReport
# import numpy as np



df = pd.read_csv("C:/Users/tanma/PycharmProjects/dataset/bank_transactions.csv")

print(df)
df.head()
df.info()
print(df.shape)

'''
# Generate a Sweetviz report
report = sv.analyze(df)

# Display the report in a web browser
report.show_html('sweetviz_report.html')
'''
'''
# Generating profile report
profile = ProfileReport(df)
profile.to_file(output_file="output.html")
'''
print(df.isnull().sum())

# Fill missing values in 'CustomerDOB' with mode (most frequent date of birth)
mode_dob = df['CustomerDOB'].mode()[0]
df['CustomerDOB'].fillna(mode_dob, inplace=True)

# Fill missing values in 'CustGender' with mode (most frequent gender)
mode_gender = df['CustGender'].mode()[0]
df['CustGender'].fillna(mode_gender, inplace=True)

# Fill missing values in 'CustLocation' with mode (most frequent location)
mode_location = df['CustLocation'].mode()[0]
df['CustLocation'].fillna(mode_location, inplace=True)

# Fill missing values in 'CustAccountBalance' with mean (average account balance)
mean_balance = df['CustAccountBalance'].mean()
df['CustAccountBalance'].fillna(mean_balance, inplace=True)

# Verify the updated columns
print(df[['CustomerDOB', 'CustGender', 'CustLocation', 'CustAccountBalance']].isnull().sum())
# Convert CustomerDOB to datetime
df['CustomerDOB'].fillna(df['CustomerDOB'].mode()[0], inplace=True)




# # Specify the date format explicitly
# date_format = '%d/%m/%y'
# df['CustomerDOB'] = pd.to_datetime(df['CustomerDOB'], format=date_format, errors='coerce')

# # Calculate age based on CustomerDOB
# df['Age'] = (pd.Timestamp.now() - df['CustomerDOB']).astype('<m8[Y]')

# Filter based on age, balance, and transaction amount criteria
eligible_people = df[(df['CustomerDOB'] > '1983-01-01') &
                     (df['CustomerDOB'] > '2008-01-01') &
                     (df['CustAccountBalance'] > 30000) &
                     (df['TransactionAmount (INR)'] > 5000)]

# Count the number of eligible individuals
num_eligible_people = len(eligible_people)

print(f"Number of people eligible to buy the watch: {num_eligible_people}")