import os
import sqlite3
import csv
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values


load_dotenv()

DB_NAME_2 = os.getenv('DB_NAME_2')
DB_USER_2 = os.getenv('DB_USER_2')
DB_PASS_2 = os.getenv('DB_PASS_2')
DB_HOST_2 = os.getenv('DB_HOST_2')

conn = psycopg2.connect(f'''dbname={DB_NAME_2}
                        user={DB_USER_2}
                        password={DB_PASS_2}
                        host={DB_HOST_2}''')
cur = conn.cursor()


# Review shape of titanic.csv in terminal
# to determine schema
# 8 columns:
"""
Survived INT
Pclass INT
Name TEXT
Sex TEXT
Age FLOAT
Siblings/Spouses Aboard INT
Parents/Children Aboard INT
Fare FLOAT
"""

# Create titanic table

create_titanic_table_query = '''

CREATE TABLE IF NOT EXISTS titanic (
    Survived INT,
    Pclass INT,
    Name TEXT,
    Sex VARCHAR,
    Age FLOAT,
    Siblings_SpousesAboard INT,
    Parents_ChildrenAboard INT, 
    Fare FLOAT
);
'''
cur.execute(create_titanic_table_query)
conn.commit()

with open('titanic.csv', 'r') as db:
    next(db)
    cur.copy_from(db, 'titanic', sep=',')

   
conn.commit()
conn.close()