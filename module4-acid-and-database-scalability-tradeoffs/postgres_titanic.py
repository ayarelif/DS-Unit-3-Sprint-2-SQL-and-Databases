import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_name=os.getenv('DB_NAME_2', default="OOPS")
db_user=os.getenv('DB_USER_2', default="OOPS")
db_pass=os.getenv('DB_PASS_2', default="OOPS")
db_host=os.getenv('DB_HOST_2', default="OOPS")

connection = psycopg2.connect(dbname=db_name, user=db_user, password=db_pass, host=db_host)

cur=connection.cursor()

# How many passengers survived, and how many died?

print("How many passengers survived and how many dies")

query_1='''
SELECT
  survived, 
  COUNT(survived)

FROM  titanic
GROUP BY survived;
'''
result=cur.execute(query_1).fetchall()
print(result)

# How many passengers were in each class?
query_2='''
SELECT 
  pclass,
  COUNT(pclass)  
FROM titanic 
GROUP BY pclass;
'''
result=cur.execute(query_2).fetchall()
print(result)

#How many passengers survived/died within each class?

# query_3='''
# SELECT 
#   pclass,
#   COUNT(pclass)  
# FROM titanic 
# GROUP BY pclass;
# '''
# result=cur.execute(query_3).fetchall()
# print(result)