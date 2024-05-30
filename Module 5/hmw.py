# def sum(a, b=10):
#     return a+b
#
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         # do something before `sum`
#         result = func(*args, **kwargs)
#         # do something after `sum`
#         return result
#     return wrapper
#
# sum = my_decorator(sum)
# @my_decorator # Equivalent to `sum = my_decorator(sum)` after the method
# def sum(a, b=10):
#     return a+b
# import functools
# import logging
#
# logging.basicConfig(level = logging.DEBUG)
# logger = logging.getLogger()
#
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
#             raise e
#     return wrapper
#
# @log
# def foo():
#     raise Exception("Something went wrong")
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         args_repr = [repr(a) for a in args]
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#         signature = ", ".join(args_repr + kwargs_repr)
#         logger.debug(f"function {func.__name__} called with args {signature}")
#         try:
#             result = func(*args, **kwargs)
#             return result
#         except Exception as e:
#             logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
#             raise e
#     return wrapper


def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout



def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Salom, men argument sifatida qabul qilingan funksiya tomonidan yaratilganman.""")
    print(greeting)


greet(shout)
greet(whisper)


def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))

# importing libraries
import time
import math


# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Qabul qilingan umumiy vaqt : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)
def login_required(func):
    def inner(name,is_login):
        if not is_login==False:
            print('Kindly login')
            return
        return func(name,is_login)
    return inner

@login_required
def home(name,is_login):

    print('Welcome to home page')
@login_required
def order(name,is_login):
    print('Welcome to order page')
def about():
    print('Welcome to about page')
home('user',True)
order('user',False)
about()


# @password("secret")
# def add(a, b):  # constant function, DO NOT MODIFY
#     return a + b
#
#
# add("h", 1, 2)  # ValueError
# add(1, 2)  # ValueError
# add("secret", 1, 2)  # 3
#
#
# def password(pswd):
#     def password(pswd):
#         def decorator(f):
#             def wrapper(*args, **kwargs):
#                 if not f(*args) is pswd:
#                     raise ValueError("Invalid password")
#                 return f(*args, **kwargs)
#
#             return wrapper
#
#         return decorator
#
