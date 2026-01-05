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