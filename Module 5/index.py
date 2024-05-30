# import utils
# from db import cur, conn
# from models import User, UserRole, UserStatus
# from session import Session
# from db import commit
# from dto import UserRegisterDTO
# from validators import check_validators
# from utils import is_authenticated
# from models import TodoType

# session = Session()


# @commit
# def login(username: str, password: str) -> utils.ResponseData:
#     user: User | None = session.check_session()
#     if user:
#         return utils.ResponseData('This User already logged in.', False)

#     get_user_by_username = '''select * from users where username = %s;'''
#     cur.execute(get_user_by_username, (username,))
#     user_data = cur.fetchone()
#     if not user_data:
#         return utils.ResponseData('Bad credentials', False)

#     user = User.from_tuple(user_data)

#     if user.login_try_count >= 3:
#         return utils.ResponseData('User has been blocked', False)

#     if not utils.match_password(password, user.password):
#         update_user_try_count = '''update users set login_try_count = login_try_count + 1 where username = %s;'''
#         cur.execute(update_user_try_count, (username,))
#         return utils.ResponseData('Bad credentials', False)

#     session.add_session(user)
#     return utils.ResponseData('User Successfully logged in', True)


# @commit
# def register(dto: UserRegisterDTO) -> utils.ResponseData:
#     try:
#         check_validators(dto)
#         check_username_by_query = '''select * from users where username = %s;'''
#         cur.execute(check_username_by_query, (dto.username,))
#         user = cur.fetchone()
#         if user:
#             return utils.ResponseData('This user already registered', False)

#         insert_user_query = '''insert into users(username,password,role,status,login_try_count) values (%s,%s,%s,%s,%s);'''
#         insert_data_params = (
#             dto.username, utils.hash_password(dto.password), UserRole.USER.value, UserStatus.INACTIVE.value, 0)
#         cur.execute(insert_user_query, insert_data_params)
#         return utils.ResponseData('User Successfully registered', True)


#     except AssertionError as e:
#         return utils.ResponseData(e, False)


# def logout() -> utils.ResponseData:
#     global session
#     if session.session:
#         session.session = None
#     return utils.ResponseData('User Successfully logged out', True)


# @is_authenticated
# @commit
# def add_todo(title: str):
#     insert_todo_query = '''insert into todos(title,todo_type,user_id) values (%s,%s,%s);'''
#     insert_data_params = (title, TodoType.PERSONAL.value, session.session.id)
#     cur.execute(insert_todo_query, insert_data_params)
#     return utils.ResponseData('Todo Successfully added', True)




import psycopg2
import utils

conn = psycopg2.connect(database="n42",
                        user="postgres",
                        password="123",
                        host="localhost",
                        port=5432)

cur = conn.cursor()

create_users_table = """
    create table if not exists users(
        id serial PRIMARY KEY,
        username varchar(100) not null unique,
        password varchar(255) not null,
        role varchar(20),
        status varchar(25) ,
        login_try_count int not null
    );
"""

create_todo_table = """
    create table if not exists todos(
        id serial PRIMARY KEY,
        title varchar(100) not null,
        todo_type varchar(20),
        user_id int references users(id)
    );
"""


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        conn.commit()
        return result

    return wrapper


@commit
def create_tables():
    cur.execute(create_users_table)
    cur.execute(create_todo_table)


@commit
def migrate():
    insert_admin_query = '''insert into users(username,password,role,status,login_try_count)
         values (%s,%s,%s,%s,%s);
    '''
    insert_data_params = ('admin', utils.hash_password('123'), 'ADMIN', 'ACTIVE', 0)
    cur.execute(insert_admin_query, insert_data_params)


def init():
    create_tables()
    migrate()

# if __name__ == '__main__':
#     init()







# class Todo:
#   todos = []
  
# def add_todo(self, todo):
#     self.todos.append(todo) 
    
# def delete_todo_by_index(self, index):
#    print('List is empty') if len(self.todos) == 0 else self.todos.remove(self.todos[index])

# # list is empty else remove todo
# def delete_todo(self, todo):
#      print('List is empty') if self.todos == [] else self.todos.remove(todo)
  
  
# # iterate in list and check for todo then check if todo is correct
# def checked_todo(self, isChecked, todoCheck):
#     for todo in self.todos:
#       if todoCheck == todo: isChecked = True
#       print('(x)', todoCheck) if isChecked is True else print('( )', todoCheck)             
    
    
# def displayTodos(self):
#      todo = [print(todo) for todo in self.todos ]
#      return todo
 
# def get_first_or_last_todo(self, position):
#      if self.todos == []: print('List is empty')
#      if position == 'first':
#        return self.todos[0]  
#      elif position == 'last':
#        return self.todos[-1]
#      else:
#        return self.todos    
   
   
#    # iterate in list and check for todo then update
# def update_todo(self, old_todo, new_todo):
#     for i in self.todos:
#      if i == old_todo: old_todo = new_todo
#     else: print('Todo is not in the list') 