import pandas as pd 
import sqlite3

df=pd.read_csv('titanic.csv')
print(df.shape)

conn=sqlite3.connect("titanic.sqlite3")

df.to_sql("Titanic", con=conn, if_exists="replace")

cursor=conn.cursor()
results=cursor.execute("SELECT * FROM Titanic;").fetchall()
print(results)