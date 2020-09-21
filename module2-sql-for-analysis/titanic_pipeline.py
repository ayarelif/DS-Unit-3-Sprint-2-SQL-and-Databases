import psycopg2

DB_NAME="pfpcgctw"
DB_USER="pfpcgctw"
DB_PASS="3KXHVMpV6FqoON9fiEQ3shZRCMXZLfs_"
DB_HOST="lallah.db.elephantsql.com"


conn=psycopg2.connect(dbname=DB_NAME,
                      user=DB_USER,
                      password=DB_PASS,
                      host=DB_HOST) 

import sqlite3
conn_titanic=sqlite3.connect("titanic.sqlite3")

cursor_titanic=conn_titanic.cursor()

titanic=cursor_titanic.execute("SELECT * FROM titanic;").fetchall()
print(titanic)

####### Create the titanic table in Postgres and insert data ######

create_titanic_table_query = '''
CREATE TABLE IF NOT EXISTS titanic_characters (
    id SERIAL PRIMARY KEY,
    Survived VARCHAR(2),
    Pclass VARCHAR(2), 
    Name VARCHAR(30),
    Sex VARCHAR(10),
    Age INT,
    Siblings/Spouses Aboard VARCHAR(2),
    Parent/Children Aboard VARCHAR(2), 
    Fare INT 
)
'''
cursor_titanic.execute(create_titanic_table_query)
conn.commit()


