# def fib (n):
#     a = 0
#     b = 1
#
#     if n == 1:
#        print(a)
#
#     else:
#         print(a)
#         print(b)
#
#     for i in range (2,n):
#         c = a + b
#         a = b
#         b = c
#         print(c)
# fib(-3)


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