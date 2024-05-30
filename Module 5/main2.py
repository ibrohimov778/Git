import product1



conn = None
cur = None

try:
    with product1.connect(
        dbname='n42',
        user='postgres',
        password='1',
        host='localhost',
        port=5432
    ) as conn:
        with conn.cursor() as cur:
            # select_employees_query = '''select * from employees;'''
            # cur.execute(select_employees_query)
            insert_into_query = '''insert into employees(name,salary,department_id) values (%s,%s,%s)'''
            insert_data_list = [('Temur', 24, 2), ('Sherali', 30, 1), ('Anna', 40, 1)]
            cur.executemany(insert_into_query, insert_data_list)
            # cur.execute(insert_into_query, insert_data)
            conn.commit()

except product1.OperationalError as e:
    print(e)


else:
    print('Successfully inserted')
    pass
