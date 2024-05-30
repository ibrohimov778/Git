# class Fibonacci:
#     def __init__(self, stop):
#         self._current = 0
#         self._stop = stop
#         self._index = 0
#         self._next = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self._index < self._stop:
#             self._index += 1
#             fibo_number = self._current
#             self._current, self._next = self._next, self._current + self._next
#
#             return fibo_number
#         else:
#             raise StopIteration
#
#
# fibo_iterator = Fibonacci(5)
# for i in fibo_iterator:
#     print(i)
#
#
# # 0 1 1 2 3 5 8 13 ..












import psycopg2

conn = psycopg2.connect(dbname='n42',
                        user='postgres',
                        password='1',
                        port=5432,
                        host='localhost')
cur = conn.cursor()

select_car_query = '''select * from users ;'''
cur.execute(select_car_query)
# for user in cur.fetchall():
#     print(user)


get_user_with_username = """select * from users where username = %s;"""


# username = input('?:')

# cur.execute(get_user_with_username, (username,))
# print(cur.fetchone())
#
# create_table_query = """create table if not exists departments
# (
#     id serial PRIMARY KEY,
#     name varchar(50) not null
# );
#
# """
# cur.execute(create_table_query)
# conn.commit()

#
# create_table_employee = """create table if not exists employees
# (
#     id serial PRIMARY KEY,
#     name varchar(50) not null,
#     salary float not null,
#     department_id int references departments(id)
#
# );
# """
# cur.execute(create_table_employee)
# conn.commit()

def insert_query_departments():
    insert_into_query = """insert into departments (name)
    values (%s)
    """
    insert_multiple_rows = [('Developer',), ('Marketing',), ('Engineering',)]
    for record in insert_multiple_rows:
        cur.execute(insert_into_query, record)
    conn.commit()

    cur.close()
    conn.close()


# def delete_query_departments(department_id):
#     delete_into_query = """delete from departments where id = %s;"""
#
#     cur.execute(delete_into_query, (department_id,))
#     conn.commit()
#     cur.close()
#     conn.close()

#
# def update_query_departments(department_id, name):
#     update_query = """update departments set name = %s where id = %s;"""
#     data = (name,department_id )
#     cur.execute(update_query, data)
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# update_query_departments(1, 'qwe')
