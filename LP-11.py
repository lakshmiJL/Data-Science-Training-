# This is a student self to do project. The trainer has to just guide him with the steps.

import numpy as np
import pandas as pd 

import matplotlib.pyplot as plt 
import seaborn as sns 
from pandas.plotting import scatter_matrix


salary_dataset  = pd.read_csv('Datasets/adult.csv')


salary_dataset.columns = ['age', 'workclass', 'fnlwgt', 'education', 'educational-num',
       'marital-status', 'occupation', 'relationship', 'race', 'gender',
       'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
       'income']

salary_dataset.rename(columns={'capital-gain': 'capital gain', 'capital-loss': 'capital loss', 'native-country': 'country','hours-per-week': 'hours per week','marital-status': 'marital'}, inplace=True)

# describe the dataset 
print(salary_dataset.describe())

# salary dataset info to find columns and count of the data 
print(salary_dataset.info())

#We count the number of missing values for each feature
print(salary_dataset.isnull().sum())
#below sum shows there are no null values in the dataset so, no need to clean the dataset 

#Finding the special characters in the data frame 
print(salary_dataset.isin(['?']).sum(axis=0))

salary_dataset['country'] = salary_dataset['country'].replace('?',np.nan)
salary_dataset['workclass'] = salary_dataset['workclass'].replace('?',np.nan)
salary_dataset['occupation'] = salary_dataset['occupation'].replace('?',np.nan)
salary_dataset['workclass'] = salary_dataset['workclass'].replace(' ?',np.nan)
salary_dataset['occupation'] = salary_dataset['occupation'].replace(' ?',np.nan)
salary_dataset['workclass'] = salary_dataset['workclass'].replace('? ',np.nan)
salary_dataset['occupation'] = salary_dataset['occupation'].replace('? ',np.nan)
salary_dataset['workclass'] = salary_dataset['workclass'].replace(' ? ',np.nan)
salary_dataset['occupation'] = salary_dataset['occupation'].replace(' ? ',np.nan)
#dropping the nan columns now 
salary_dataset.dropna(how='any',inplace=True)

salary_dataset.to_csv("changedIncomeData.csv")

print("running loop")
#running a loop for value_counts of each column to find out unique values. 
for c in salary_dataset.columns:
    print ("---- %s ---" % c)
    print (salary_dataset[c].value_counts())

#dropping un-used data from the dataset 
salary_dataset.drop(['educational-num','age', 'hours per week', 'fnlwgt', 'capital gain','capital loss', 'country'], axis=1, inplace=True)

# Let's see how many unique categories we have in this property
income = set(salary_dataset['income'])
print(income)

#mapping the data into numerical data using map function
salary_dataset['income'] = salary_dataset['income'].map({' <=50K': 0, ' >50K': 1}).astype(int)

#check the data is replaced 
salary_dataset.head()

#Mapping the values to numerical values 
salary_dataset['gender'] = salary_dataset['gender'].map({' Male': 0, ' Female': 1}).astype(int)

#Mapping the values to numerical values 
salary_dataset['race'] = salary_dataset['race'].map({' Black': 0, ' Asian-Pac-Islander': 1, ' Other': 2, ' White': 3, ' Amer-Indian-Eskimo': 4}).astype(int)

#Mapping the values to numerical values 
salary_dataset['marital'] = salary_dataset['marital'].map({' Married-spouse-absent': 0, ' Widowed': 1, ' Married-civ-spouse': 2, ' Separated': 3, ' Divorced': 4, ' Never-married': 5, ' Married-AF-spouse': 6}).astype(int)

#Mapping the values to numerical values
#salary_dataset['workclass'] = salary_dataset['workclass'].map({' Self-emp-inc': 0, ' State-gov': 1, ' Federal-gov': 2, ' Without-pay': 3, ' Local-gov': 4, ' Private': 5, ' Self-emp-not-inc': 6, " ?" : 7}).astype(int)

# Now we classify them as numbers instead of their names.
"""salary_dataset['occupation'] = salary_dataset['occupation'].map({ ' Farming-fishing': 1, ' Tech-support': 2, ' Adm-clerical': 3, ' Handlers-cleaners': 4, 
                                         ' Prof-specialty': 5,' Machine-op-inspct': 6, 
                                         ' Exec-managerial': 7, 
                                         ' Priv-house-serv': 8,
                                         ' Craft-repair': 9, 
                                         ' Sales': 10, 
                                         ' Transport-moving': 11, 
                                         ' Armed-Forces': 12, 
                                         ' Other-service': 13,  
                                         ' Protective-serv': 14}).astype(int)"""
salary_dataset['occupation'] = salary_dataset['occupation'].map({ ' Farming-fishing': 1, ' Tech-support': 2, ' Adm-clerical': 3, ' Handlers-cleaners': 4, 
                                         ' Prof-specialty': 5,' Machine-op-inspct': 6, 
                                         ' Exec-managerial': 7, 
                                         ' Priv-house-serv': 8,
                                         ' Craft-repair': 9, 
                                         ' Sales': 10, 
                                         ' Transport-moving': 11, 
                                         ' Armed-Forces': 12, 
                                         ' Other-service': 13,  
                                         ' Protective-serv': 14})
#Mapping the values to numerical values
salary_dataset['relationship'] = salary_dataset['relationship'].map({' Not-in-family': 0, ' Wife': 1, 
                                                             ' Other-relative': 2, 
                                                             ' Unmarried': 3, 
                                                             ' Husband': 4, 
                                                             ' Own-child': 5}).astype(int)

#plotting a bar graph for Education against Income to see the co-relation between these columns 
salary_dataset.groupby('education').income.mean().plot(kind='bar')
plt.show()
#plotting a bar graph for Occupation against Income to see the co-relation between these columns 
salary_dataset.groupby('occupation').income.mean().plot(kind='bar')
plt.show()
#plotting a bar graph for Relationship against Income to see the co-relation between these columns 
salary_dataset.groupby('relationship').income.mean().plot(kind='bar')
plt.show()
#plotting a bar graph for Race against Income to see the co-relation between these columns 
salary_dataset.groupby('race').income.mean().plot(kind='bar')
plt.show()
#plotting a bar graph for Race against Income to see the co-relation between these columns 
salary_dataset.groupby('gender').income.mean().plot(kind='bar')
plt.show()
#plotting a bar graph for Race against Income to see the co-relation between these columns 
salary_dataset.groupby('workclass').income.mean().plot(kind='bar')
plt.show()
#plotting a bar graph for Race against Income to see the co-relation between these columns 
salary_dataset.groupby('marital').income.mean().plot(kind='bar')
plt.show()
# Density plots

salary_dataset.plot(kind='density', subplots=True, layout=(4,4), sharex=False, legend=True, fontsize=1, figsize=(12,16))
plt.show()