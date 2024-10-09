import pandas as pd
# Loading the data from a file
data = pd.read_csv("L3/titanic.csv")
print(data.head())
print(data.info())
# Prints the datatypes of each column
print(data.dtypes)

# Selecting multiple columns together
nameAndAge = data[["Name", "Age"]]

print(nameAndAge.head())
print(nameAndAge.shape)


# Filtering out rows
above35 = data[data["Age"] > 35]
print(above35.head())
print(above35.shape) # To confirm the number of rows, open the csv in excel and filter on the same column

# Combining multiple conditions together
class2And3 = data[data["Pclass"].isin([2, 3])]
print(class2And3[["Name", "Pclass"]].head())
print(class2And3.shape)

class2And3 = data[(data["Pclass"] == 2) | (data["Pclass"] == 3)] # Combining condition by OR (|), show one example by AND (&) also
print(class2And3[["Name", "Pclass"]].head())
print(class2And3.shape)

# Task - Get the mean fare of people travelling in each Pclass wrt Sex

maleFirstClass = data[(data["Sex"] == "male") & (data["Pclass"] == 1)]
print("The mean age of male first class passenger is", maleFirstClass["Fare"].mean())
# Repeat for other 5 combinations namely
# femaleFirstClass
# maleSecondClass
# femaleSecondClass
# maleThirdClass
# femaleThirdClass


# Get the particular column out of a condition
adult_names = data.loc[data["Age"] > 18, "Name"]
print(adult_names)


# Changing the value in the dataset
# Specify the number of rows and the particular column to change
data.iloc[0:3, 3] = "Pulkit Chawla"
print(data["Name"])

# Save the data to local to verify changes
# Creating a new column in the dataFrame
data["Test"] = data["Fare"] + 2
data["Test2"] = data["Fare"] * data["Pclass"] # Any mathematical operation could be considered
data.to_csv("pandas/changedData.csv")

# Renaming the column names
data_renamed = data.rename(
    columns = {
        "Pclass": "Passenger Class",
        "Siblings/Spouses Aboard": "Sibling"
    }
)

print(data_renamed.columns)

# Performing mathematical operation on multiple columns together
print(data["Age"].mean())

print(data[["Age", "Fare"]].mean())

print(data.agg({
    "Age": ["min", "max", "median"],
    "Fare": ["min", "max", "median"]
}))

# Group by data categorically

print(data[["Sex", "Age"]].groupby("Sex").mean())

print(data.groupby("Sex")["Age"].mean())

# Task - Get the mean ticket price for each of sex and cabin class combination
print(data.groupby(["Sex", "Pclass"])["Fare"].mean())

# Get the count of rows in each category
print(data["Pclass"].value_counts())

print(data.groupby("Pclass")["Pclass"].count())

# Sorting the data
x = data.sort_values(by = "Age", ascending = True)
print(x.head())
print(x[["Name", "Age"]].head())

data.sort_values(by = ["Pclass", "Age"], ascending = False)

# Operations on Text Data
data["NameLowercase"] = data["Name"].str.lower()
data.to_csv("pandas/changedData.csv")
# Other Examples to be shown
#data["Name"].str.split(",")
#data["Surname"] = data["Name"].str.split(",").str.get(0)
#data["Sex_short"] = data["Sex"].replace({"male": "M", "female": "F"})
