import psycopg2
from colorama import Fore

conn = psycopg2.connect(dbname='n42',
                        user='Abdulbori',
                        password='0800',
                        host='localhost',
                        port=5432
                        )
cur = conn.cursor()

create_table_query = '''
    create table if not exists books(
        id serial PRIMARY KEY,
        name varchar(100) not null,
        author varchar(100) not null
    1
    );
    
'''
cur.execute(create_table_query)
conn.commit()


def print_response(message: str):
    print(Fore.BLUE + message + Fore.RESET)


def insert_book():
    name = str(input('Enter book name: '))
    author = str(input('Enter book author : '))
    insert_into_query = "insert into books(name,author) values (%s,%s);"
    insert_into_params = (name, author)
    cur.execute(insert_into_query, insert_into_params)
    conn.commit()
    print_response('INSERT 0 1')


def select_all_books():
    select_query = 'select * from books;'
    cur.execute(select_query)
    rows = cur.fetchall()
    for row in rows:
        print_response(str(row))


def select_one_book():
    _id = int(input('Enter book id : '))
    select_query = 'select * from books where id = %s;'
    cur.execute(select_query, (_id,))
    book = cur.fetchone()
    if book:
        print_response(book)
    else:
        print_response('No such book')


def update_book():
    select_all_books()
    _id = int(input('Enter book id : '))
    name = str(input('Enter new book name : '))
    author = str(input('Enter new author : '))
    update_query = 'update books set name = %s, author = %s where id =%s;'
    update_query_params = (name, author, _id)
    cur.execute(update_query, update_query_params)
    conn.commit()
    print_response('Successfully updated book')


def delete_book():
    select_all_books()
    _id = int(input('Enter book id : '))

    delete_query = 'delete from books where id = %s;'
    cur.execute(delete_query, (_id,))
    conn.commit()
    print_response('Successfully deleted book')


def menu():
    try:
        print('Insert book      => 1')
        print('Select all books => 2')
        print('Delete book      => 3')
        print('Select one book  => 4')
        print('Update book      => 5')
        choice = int(input('Enter your choice : '))

    except ValueError as e:

        choice = -1

    return choice


def run():
    while True:
        choice = menu()
        match choice:
            
            case 1:
                insert_book()
            case 2:
                select_all_books()
            case 3:
                delete_book()
            case 4:
                select_one_book()
            case 5:
                update_book()
            case _:
                break


if __name__ == '__main__':
    run()
