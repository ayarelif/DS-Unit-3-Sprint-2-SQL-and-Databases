# First install the psycopg2 "pipenv install python-dotenv psycopg2-binary"
#  in the terminal
import psycopg2

#Create a connection between the the file on elephantsql.com and tableplus
DB_NAME="knworjgk"
DB_USER="knworjgk"
DB_PASS="qqK7DZjGxTDrpxSNPr2pq6d_PqwxEbAL"
DB_HOST="lallah.db.elephantsql.com"

conn=psycopg2.connect(dbname=DB_NAME,
                      user=DB_USER,
                      password=DB_PASS,
                      host=DB_HOST) 

cursor=conn.cursor()

cursor.execute("SELECT * from test_table;")

result=cursor.fetchall()

#print(result)

######### connect to SQLite DB for RPG Data#######
# If you have file from different module
#sl_conn=sqlite3.connect("../module1_intor/elephant_rpg.sqlite3") 
import sqlite3
sl_conn=sqlite3.connect("rpg_db.sqlite3")
sl_cursor=sl_conn.cursor()
characters=sl_cursor.execute("SELECT * FROM charactercreator_character;").fetchall()
print(characters)

####### Create the Character table in Postgres and insert data ######

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30),
    level INT,
    exp INT,
    hp INT,
    strength INT, 
    intelligence INT,
    dexterity INT,
    wisdom INT
)
'''
cursor.execute(create_character_table_query)
conn.commit()

for character in characters[0:10]:
    insert_query=f'''INSERT INTO rpg_characters
    (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES
    {character}
    '''

    cursor.execute(insert_query)
conn.commit()


# #ALternatetive approach (faster)


# big_query=f'''INSERT INTO rpg_characters
#     (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES'''

# for character in characters:
#     big_query+=f'{character},'
# print(big_query)

