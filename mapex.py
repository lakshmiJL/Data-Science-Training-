import pandas as pd


numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)
# 2 4 6 8

data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 92, 78, 88]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


def increase_score(score):
    return score * 1.10  # Increase score 

df['Increased Score'] = df['Score'].map(increase_score)
print("\nDataFrame with Increased Scores:")
print(df)

# Step 1: Get the matrix size (n)
n = int(input("Enter the size of the matrix (n x n): "))


#for input for n*n matrix
# Step 2: Use a loop and map to gather inputs for each row of the matrix
matrix = []

print(f"Enter the matrix row by row (space-separated values):")
for i in range(n):
    # Step 3: Input the row values and split them into a list, then convert to integers
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    
    # Step 4: Append the row to the matrix
    matrix.append(row)

# Step 5: Display the matrix
print("\nThe matrix you entered is:")
for row in matrix:
    print(row)