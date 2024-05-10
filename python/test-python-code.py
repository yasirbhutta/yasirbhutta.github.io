import pandas as pd
import mysql.connector

# Establish connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="abc1234",
    database="library"
)

# Define your SQL query
sql = "SELECT * FROM books"  # Replace with your specific query

# Read the results into a DataFrame
df = pd.read_sql(sql, mydb)  # mydb is the connection object

# Close the connection
mydb.close()

# Now you can work with the data in your DataFrame (df)
print(df.head())  # View the first few rows
