# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m2N6RGElKsGo3jLt2CEITTNowzBZgNZp
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

#load the data
df = pd.read_csv('train.csv')
df.head()

#fill missing values
df.isnull().sum()

df["Age"].fillna(df["Age"].mode()[0], inplace=True)
df["Cabin"].fillna(df["Cabin"].mode()[0], inplace = True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace = True)
df.isnull().sum()

#drop unneeded columns
df.drop(columns = ['Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'], inplace = True)

#scale the data
std_scaler = StandardScaler()

df_scaled = std_scaler.fit_transform(df.to_numpy())
df_scaled = pd.DataFram(df_scaled, columns = ['PassengerId', 'Survived'])

#splitting the data into training and test set
x_train, x_test, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

#loop over possible K values
for i, k in enumerate(neighbors):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)