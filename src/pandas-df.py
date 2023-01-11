import pandas as pd

df = pd.read_excel("Salary Info.xlsx")
print(df)
print(df.info()) # check data types of values
print("size:", df.size)
print("columns:", df.columns) # print the column name
print("length:", len(df)) # print number of rows in excel
print("query:", df.query("`Monthly Salary` > 10000")) # print rows with salary above 10k
print("first five rows:", df.iloc[:4])
print("Employee Salary Data:", df[["Name", "Monthly Salary", "Company"]])

