import os
import sqlite3

DB_FILEPATH = "rpg_db.sqlite3"

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print(cursor)

query_1='''
SELECT
  COUNT(character_id),
  COUNT(DISTINCT character_id)
FROM charactercreator_character;
'''
result=cursor.execute(query_1).fetchall()
print(result)

# 2) How many of each specific subclass?
# There are 6 subclasses under Characters


# 3) How many total Items?
query_3='''
SELECT
  COUNT(item_id),
  COUNT(DISTINCT item_id)
FROM armory_item;

'''
result=cursor.execute(query_3).fetchall()
print(result)

# 4) How many of the Items are weapons? 
query_4='''
SELECT 
  COUNT(armory_weapon.power)
FROM armory_item 
INNER JOIN armory_weapon
ON armory_item.item_id=armory_weapon.item_ptr_id;
'''
result=cursor.execute(query_4).fetchall()
print(result)

# not weapon
query_4='''
SELECT 
  armory_item.item_id,
  armory_item.name,
  armory_weapon.item_ptr_id,
  armory_weapon.power
FROM armory_item 
LEFT JOIN armory_weapon
ON armory_item.item_id=armory_weapon.item_ptr_id;
'''
result=cursor.execute(query_4).fetchall()
print(result)

# 5)How many Items does each character have? (Return first 20 rows)
query_5='''
SELECT 
  character_id,
  COUNT(DISTINCT item_id)
FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;

'''
result=cursor.execute(query_5).fetchall()
print(result)

# 6)How many Weapons does each character have? (Return first 20 rows)

query_6='''
SELECT 
  charactercreator_character_inventory.character_id,
  armory_item.item_id,
  armory_item.name,
  armory_weapon.item_ptr_id,
  COUNT(DISTINCT armory_weapon.power)
FROM charactercreator_character_inventory
INNER JOIN armory_item ON charactercreator_character_inventory.item_id=armory_item.item_id
INNER JOIN armory_weapon ON armory_item.item_id=armory_weapon.item_ptr_id
GROUP BY character_id
LIMIT 20;


'''
result=cursor.execute(query_6).fetchall()
print(result)

# 7)On average, how many Items does each Character have?
query_7='''
SELECT
  character_id,
  COUNT(DISTINCT item_id)
FROM charactercreator_character_inventory
GROUP BY character_id;
'''
result=cursor.execute(query_7).fetchall()
print(result)



