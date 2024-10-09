#basic operations on columns 
#like selecting, deleting, adding and renaming.

import pandas as pd
 
# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
print(df[['Name', 'Qualification']])

#make a new list as a column and add to a existing Dataframe
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna']
df['Address'] = address
print(df)
#make a new DF as a row and add to a existing Dataframe
new_row = pd.DataFrame({'Name':'Laksh', 
                        'Age':33, 
                        'Address':'Chennai',
                        "Qualification":"BTech"},
                        index =[0])
df = pd.concat([new_row, df]).reset_index(drop = True)
print(df)

#Columns is deleted by dropping columns with column names
#dropping passed columns
#df.drop(["Qualification", "Age"], axis = 1, inplace = True)
#print(df)
#Row deletion
#df.drop(["Laksh"], inplace = True)
#print(df)


#selcting and storing one or more columns

#.loc[] (Label-based indexing)
#.iloc[] (Integer-based indexing)
print("using iloc")
firstsecond = df.iloc[0:4]
print(firstsecond)
# Extracting a single row by index
row_laksh = df.iloc[0, :]
print(row_laksh)
# Extracting multiple rows using a slice
row_123 =df.iloc[0:4,:]
print(row_123)

# retrieving row by loc method
#first = df.loc["Laksh"]
#second = df.loc["Jai"]

#print(first, "\n\n\n", second)

# Set 'Name' as the index
df.set_index('Name', inplace=True)

# retrieving row by loc method after set index
first = df.loc["Laksh"]
second = df.loc["Jai"]

print(first, "\n\n\n", second)

firstsecond = df.loc["Laksh":"Jai"]
print(firstsecond)





