### Part 1 - Making and populating a Database

"""Consider the following data:

| s   | x | y |
|-----|---|---|
| 'g' | 3 | 9 |
| 'v' | 5 | 7 |
| 'f' | 8 | 7 |

Using the standard `sqlite3` module:

- Open a connection to a new (blank) database file `demo_data.sqlite3`
- Make a cursor, and execute an appropriate `CREATE TABLE` statement to accept
  the above data (name the table `demo`)
- Write and execute appropriate `INSERT INTO` statements to add the data (as
  shown above) to the database

Make sure to `commit()` so your data is saved! The file size should be non-zero.
"""

import sqlite3

##### Make connection and cursor

connection=sqlite3.connect("demo_data_test.sqlite3")
cursor=connection.cursor()

##### Create the table ######

create_demo_table="""
   CREATE TABLE IF NOT EXISTS demo(
       s VARCHAR(3),
       x INTEGER,
       y INTEGER
)
"""
#### write execute

cursor.execute(create_demo_table)

#### Insert data into database
cursor.execute("INSERT INTO demo (s,x,y) Values ('g',3,9);")
cursor.execute("INSERT INTO demo (s,x,y) Values ('v',5,7);")
cursor.execute("INSERT INTO demo (s,x,y) Values ('f',8,7);")


#### Commit

connection.commit()


# Question 1 Count how many rows you have - it should be 3!

query1 = """
SELECT COUNT(x)
FROM Demo
"""
result1 = cursor.execute(query1).fetchall()
print(result1)

# Question 2 How many rows are there where both `x` and `y` are at least 5?
query2 = """
SELECT *
FROM Demo
WHERE x >= 5 AND y >= 5
"""
result2 = cursor.execute(query2).fetchall()
print(result2)

# Question 3 How many unique values of `y` are there 

query3 = """
SELECT
  COUNT(DISTINCT y)
FROM Demo
"""
result3 = cursor.execute(query3).fetchall()
print(result3)

