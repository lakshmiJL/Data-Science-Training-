
# Data Preprocessing Tools

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')

#info
print(dataset.info())

#split into features(input) and target(output)
X = dataset.iloc[:, :-1]#.values
y = dataset.iloc[:, -1]#.values
print("Features:\n",X)
print("Target:\n",y)

# Taking care of missing data
#Univariate imputer for completing missing values with simple strategies.
#Replace missing values using a descriptive statistic (e.g. mean, median, or most frequent) along each column, 
#or using a constant value.
# pip install scikit-learn
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean') #pd.NA np.nan
#imputer.fit(X.iloc[:, 1:3])
X.iloc[:, 1:3] = imputer.fit_transform(X.iloc[:, 1:3])
print("After imputing:\n",X)

# Encoding categorical data
#One hot encoding is a technique that we use to represent categorical variables as numerical values in a machine learning model.
# Encoding the Independent Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X_encoded = pd.DataFrame(ct.fit_transform(X))
print("One hot encoding\n",X_encoded)

#Alternate 
dummies_df = pd.get_dummies(X, columns = ['Country']) 
print("Dummies:\n",dummies_df)

# Encoding the Dependent Variable
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print("Label Encoder:\n",y)
#y = y.replace({"Yes":1, "No":0})

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dummies_df, y, test_size = 0.2, random_state = 42)
print("X_train:\n",X_train)
print("X_test:\n",X_test)
print("y_train:\n",y_train)
print("y_test:\n",y_test)

#Scaling the data can help to balance the impact of all variables on the distance 
# calculation and can help to improve the performance of the algorithm.
# in many machine learning algorithms, to bring all features in the same standing, 
#we need to do scaling so that one significant number doesn't impact the model just 
# because of their large magnitude.
# Feature Scaling
#The formula of StandardScaler is (Xi-Xmean)/Xstd, so it adjusts the mean as a 0 with unit standard deviation.
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train.iloc[:, 0:2] = sc.fit_transform(X_train.iloc[:, 0:2])
X_test.iloc[:, 0:2] = sc.fit_transform(X_test.iloc[:, 0:2])
print("Scaled")
print(X_train)
print(X_test)