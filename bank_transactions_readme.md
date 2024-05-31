# Smart Trendy Watch Sales Analysis

## Introduction

This Python script analyzes bank transaction data to identify potential customers for selling a smart trendy watch. The primary target audience for this watch are individuals aged 18 to 35 years old. The analysis focuses on filtering bank customers based on age, account balance, and transaction amount criteria to identify eligible individuals who are likely to be interested in purchasing the watch.

## Code Overview

### Data Loading and Inspection

- The script loads bank transaction data from the CSV file `bank_transactions.csv` using pandas.
- It inspects the dataset by displaying the first few rows, general information, and shape of the DataFrame.

### Data Preprocessing

- Missing Values Handling:
  - Missing values in columns `CustomerDOB`, `CustGender`, `CustLocation`, and `CustAccountBalance` are filled using appropriate strategies such as mode and mean.
  - The script ensures data integrity by verifying the absence of missing values after handling.

### Eligibility Criteria

- Age Filtering:
  - Individuals with a birth date after January 1, 1983, and before January 1, 2008, are considered within the target age range of 18 to 35 years.
- Account Balance and Transaction Amount Criteria:
  - Customers with an account balance greater than 30,000 INR and transaction amounts exceeding 5,000 INR are identified as potential candidates.

### Results

- The script calculates the number of eligible individuals meeting the specified criteria for purchasing the smart trendy watch.
- According to the output, there are 15,224 people eligible to buy the watch.

## Justification

The code is designed to identify potential customers who are likely to be interested in purchasing the smart trendy watch based on their age, financial status, and transaction behavior. By targeting individuals aged 18 to 35 years with sufficient account balances and high transaction amounts, the sales team can focus their efforts on a specific segment of the customer base, thereby increasing the effectiveness of marketing campaigns and sales initiatives.

## Next Steps

- Experiment with different eligibility criteria to optimize target audience selection.
- Incorporate additional demographic and behavioral factors for more precise customer segmentation.
- Implement advanced analytics techniques such as machine learning models to predict customer preferences and personalize marketing strategies.

## Acknowledgments

- **pandas**: For data manipulation and analysis.
- **seaborn**: For data visualization.
- **numpy**: For numerical computations.
- **ydata_profiling**: For generating comprehensive profile reports of the dataset.
