
# Iris Species Classification


This project aims to classify Iris flower species using various machine learning algorithms. The dataset used in this project is the famous Iris dataset, which contains samples of three species of Iris flowers.

## Overview

This project implements several machine learning classifiers to predict the species of Iris flowers based on their features. The classifiers used include Gradient Boosting, Random Forest, Logistic Regression, Naive Bayes, and Decision Tree classifiers.

## Installation
To run this project, you need to have Python 3.x installed along with the following libraries:

- scikit-learn
- pandas

You can install the required libraries using pip:
```
pip install scikit-learn pandas

```

## Usage
1 Clone this repository to your local machine:
```
git clone https://github.com/your-tanmaypatil8/iris-classification.git

```
2 Navigate to the project directory:
```
cd iris-classification

```
3 Run the Python script:
```
python iris_classification.py

```
The script will train the classifiers on the Iris dataset and print the accuracy scores, confusion matrices, and classification reports for each classifier.


## Dataset

The Iris dataset used in this project can be found at 
https://archive.ics.uci.edu/dataset/53/iris

## Results
The following are the accuracy scores, confusion matrices, and classification reports for each classifier:

### Gradient Boosting Classifier
- Accuracy Score: 0.967
- Confusion Matrix

```
[[11  0  0]
 [ 0 12  1]
 [ 0  0  6]]

```
- Classification Report:

```
                   precision    recall  f1-score   support

    Iris-setosa       1.00      1.00      1.00        11
Iris-versicolor       1.00      0.92      0.96        13
 Iris-virginica       0.86      1.00      0.92         6

       accuracy                           0.97        30
      macro avg       0.95      0.97      0.96        30
   weighted avg       0.97      0.97      0.97        30

```
### (Include similar sections for other classifiers)

## Contributing
Contributions to this project are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

## Contact
For any questions or feedback, feel free to contact the project maintainer at your- tanmaypatil7426@gmail.com

