# importing pandas module 
import pandas as pd 
  
# making data frame 
data = pd.read_csv("Datasets/iris.csv") 
  
# calling head() method  
# storing in new variable 
data_top = data.head() 
  
# display 
print(data_top) 


# number of rows to return 
n = 9
  
# creating series 
series = data["sepal_length"] 
  
# returning top n rows 
top = series.head(n = n) 
  
# display 
print(top) 

# calling tail() method  
# storing in new variable 
data_bottom = data.tail() 
  
# display 
print(data_bottom) 

#describe() is used to view some basic statistical details 
#like percentile, mean, std, etc
#The min and max give you the range of values.
#The 25%, 50%, and 75% give you an idea of 
# how the data is spread between the minimum and maximum values.
print(data.describe())

# Gives the typical summary of the data
print(data.info())
# Gives the data types of the data
print(data.dtypes)

