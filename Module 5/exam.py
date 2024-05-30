# N42-guruh
# Ibrohimov Abdulbori
# 1-misol

from tebulate import Product
    

def __init__(self,id,name,price,color,image):
     self.id = id
     self.name = name
     self.price = price
print(Product())





import psycopg2

host = 'localhost'
user = 'postgres'
password = '123'
database = 'n42'
port = 5432

conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

cur = conn.cursor()
insert_car_query = """
INSERT INTO cars (name,color,item_id)
values ('Gentra','Black',3)
"""

crate_car = """
create table if not exists cars(
     id serial primary key,
     name varchar(25)
);
"""
cur.execute(crate_car)
conn.commit()