import pandas as pd 
import numpy as np

# Creating empty series 
ser = pd.Series() 
print("Pandas Series: ", ser) 

# simple array 
data = np.array(['a', 'b', 'c', 'd', 'e']) 
  
ser = pd.Series(data) 
print("Pandas Series:\n", ser)


# Calling DataFrame constructor 
df = pd.DataFrame() 
print(df)

# list of strings 
lst = ['We', 'love', 'coding', 'in', 'JetLearn'] 
  
# Calling DataFrame constructor on list 
df = pd.DataFrame(lst) 
print(df)

# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
df = pd.DataFrame(dict)
 
print(df)
