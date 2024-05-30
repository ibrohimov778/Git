

@password("secret")
def add(a, b):  # constant function, DO NOT MODIFY
    return a + b


add("h", 1, 2)  # ValueError
add(1, 2)  # ValueError
add("secret", 1, 2)  # 3


def password(pswd):
    def password(pswd):
        def decorator(f):
            def wrapper(*args, **kwargs):
                if not f(*args) is pswd:
                    raise ValueError("Invalid password")
                return f(*args, **kwargs)

            return wrapper

        return decorator