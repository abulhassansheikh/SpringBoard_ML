# Simple Linear Regression

'''
This model predicts the salary of the employ based on experience using simple linear regression model.
'''

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json

# Importing the dataset
path = "C:/Users/abulh/Sync/O4_P1_SpringBoardMLCourse/Unit17/flask-salary-predictor-master/Salary_Data.csv"
dataset = pd.read_csv(path)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Saving model using pickle
pickle.dump(regressor, open("C:/Users/abulh/Sync/O4_P1_SpringBoardMLCourse/Unit17/flask-salary-predictor-master/model.pkl",'wb'))

# Loading model to compare the results
model = pickle.load( open("C:/Users/abulh/Sync/O4_P1_SpringBoardMLCourse/Unit17/flask-salary-predictor-master/model.pkl",'rb'))
print(model.predict([[1.8]]))
