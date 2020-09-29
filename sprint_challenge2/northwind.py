import sqlite3

conn=sqlite3.connect("northwind_small.sqlite3")
cur=conn.cursor()

# Question 1 : What are the ten most expensive items (per unit price) in the database?

query1 = """
SELECT DISTINCT 
       ProductName,
       UnitPrice
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

result1 = cur.execute(query1).fetchall()
print(result1)

# Question 2: What is the average age of an employee at the time of their hiring?

query2 = """
SELECT
  
  AVG(HireDate - BirthDate)
FROM Employee;
"""

result2 = cur.execute(query2).fetchall()
print(result2)
# Question Strestch: How does the average age of employee at hire vary by city?

query_stretch1 = """
SELECT
  AVG(HireDate - BirthDate)
FROM Employee
GROUP BY City;
"""
result_stretch1 = cur.execute(query_stretch1).fetchall()
print(result_stretch1)

#### Part 3 - Sailing the Northwind Seas

#  Question 3:  What are the ten most expensive items (per unit price)
#  in the database *and their suppliers?

query3 = """
SELECT 
  ProductName,
  UnitPrice,
  CompanyName
FROM Product
INNER JOIN Supplier
ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC;
"""
result3 = cur.execute(query3).fetchall()
print(result3)
# Question 4: What is the largest category (by number of unique products in it)?

query4 = """

SELECT 
    COUNT(Product.CategoryId)as product_count,
       Category.CategoryName
FROM Product
JOIN Category on Product.CategoryId = Category.Id
GROUP BY Product.CategoryId
ORDER BY product_count DESC
LIMIT 1;
"""

result4 = cur.execute(query4).fetchall()
print(result4)

# Question stretch:*Stretch*) Who's the employee with the most territories? Use `TerritoryId`
# (not name, region, or other fields) as the unique identifier for territories.

query_stretch2 = """
SELECT
  TerritoryId,
  COUNT(EmployeeId)
FROM EmployeeTerritory
LIMIT 1;
"""
result_stretch2 = cur.execute(query_stretch1).fetchall()
print(result_stretch2)
# I will do later if I have time


### Part 4 - Questions (and your Answers)

#In the Northwind database, what is the type of relationship between the
# `Employee` and `Territory` tables?

""" The type of relationship between the "Employee" and "Territory" is many to many
There are three connection path from employee to territory. First Employee has a key column to
connect with Orders table by usinf CostumerId. Second, CostumerId at the Orders column
has a connection with EmployeeTerritories. Then their is a path between EmployeeTerritories and Territories
"""

# What is a situation where a document store (like MongoDB) is appropriate\

"""  MongoDB is the document store to be used for unstructed big datasets. 
It has a lot of tools and models to be used to manupulate and clean the data for daya anaylsis.
On the other hand, it is unapproriiate because it does not provide transaction so SQL is better to use if we need transaction
"""
# What is "NewSQL", and what is it trying to achieve?

""" NewSQL is a new appraoch to relational databases that wants to combine transactional ACID
and horizontal NoSQL. I founf this defination from "https://softwareengineeringdaily.com/2019/02/24/what-is-new-about-newsql/"
Based on this defination we could conclude that NewSQL is an improved version of both to provide
functionality and services better. Speed is better and faster than SQL and NoSQL.
"""
