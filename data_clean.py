import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\HP\Desktop\python\indexing and slicing in numpy\Employee dataset\employees (1).csv")
print(df.head())
print("Missing values in each column")
print(df.isnull().sum())

mode_name=df["First Name"].mode()[0]
df["First Name"]=df["First Name"].fillna(mode_name)

gender_mode = df["Gender"].mode()[0]
df["Gender"] = df["Gender"].fillna(gender_mode)

senior_mode = df["Senior Management"].mode()[0]
df["Senior Management"] = df["Senior Management"].fillna(senior_mode)

team_mode = df["Team"].mode()[0]
df["Team"] = df["Team"].fillna(team_mode)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(df.select_dtypes(include=np.number).mean(), inplace=True)

#remove duplicate records
df.drop_duplicates(inplace=True)
#remove negative salaries
df["Salary"]=np.where(df["Salary"]<0, df["Salary"].mean(), df["Salary"])

salary_mean=df["Salary"].mean()
salary_std=df["Salary"].std()
lower_bound=salary_mean-(3*salary_std)
upper_bound=salary_mean+(3*salary_std)

#remove rows where salary is too high or too low
df=df[(df["Salary"]>=lower_bound)& (df["Salary"]<=upper_bound)]

df.to_csv("cleaned_employee_Data.csv",index=False)

print('Data cleaning completed! Saved as "cleaned_employee_Data.csv"')


# Import pandas for data manipulation and numpy for numerical operations
# import pandas as pd
# import numpy as np

# # Read the employee dataset from the specified CSV file path
# df = pd.read_csv(r"C:\Users\HP\Desktop\python\indexing and slicing in numpy\Employee dataset\employees (1).csv")

# # Display the first 5 rows of the dataset
# print(df.head())

# # Print a message indicating missing value analysis
# print("Missing values in each column")

# # Display the count of missing values in each column
# print(df.isnull().sum())

# # Find the most frequent (mode) value in the 'First Name' column
# mode_name = df["First Name"].mode()[0]

# # Replace missing values in 'First Name' with the mode
# df["First Name"] = df["First Name"].fillna(mode_name)

# # Find the most frequent (mode) value in the 'Gender' column
# gender_mode = df["Gender"].mode()[0]

# # Replace missing values in 'Gender' with the mode
# df["Gender"] = df["Gender"].fillna(gender_mode)

# # Find the most frequent (mode) value in the 'Senior Management' column
# senior_mode = df["Senior Management"].mode()[0]

# # Replace missing values in 'Senior Management' with the mode
# df["Senior Management"] = df["Senior Management"].fillna(senior_mode)

# # Find the most frequent (mode) value in the 'Team' column
# team_mode = df["Team"].mode()[0]

# # Replace missing values in 'Team' with the mode
# df["Team"] = df["Team"].fillna(team_mode)

# # Replace infinite values (positive or negative) with NaN
# df.replace([np.inf, -np.inf], np.nan, inplace=True)

# # Fill remaining missing numeric values with the mean of their respective columns
# df.fillna(df.select_dtypes(include=np.number).mean(), inplace=True)

# # Remove duplicate rows from the dataset
# df.drop_duplicates(inplace=True)

# # Replace negative salary values with the mean salary
# df["Salary"] = np.where(df["Salary"] < 0, df["Salary"].mean(), df["Salary"])

# # Calculate the mean salary
# salary_mean = df["Salary"].mean()

# # Calculate the standard deviation of salary
# salary_std = df["Salary"].std()

# # Define the lower bound for salary using the 3-sigma rule
# lower_bound = salary_mean - (3 * salary_std)

# # Define the upper bound for salary using the 3-sigma rule
# upper_bound = salary_mean + (3 * salary_std)

# # Remove rows with salary values outside the defined bounds
# df = df[(df["Salary"] >= lower_bound) & (df["Salary"] <= upper_bound)]

# # Save the cleaned dataset to a new CSV file without index
# df.to_csv("cleaned_employee_Data.csv", index=False)

# # Print confirmation message after successful data cleaning
# print('Data cleaning completed! Saved as "cleaned_employee_Data.csv"')
