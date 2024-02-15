class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def authentication_decorator(function):
    def wrapper_function(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper_function


@authentication_decorator
def create_new_blog(given_user):
    print(f" the blog has been created by '{given_user.name}'.")


user = User("Mojtaba Parvizi")
user.is_logged_in = True
create_new_blog(user)


# TODO: Create the logging_decorator() function 👇
inputs = [1, 2, 3]


def logging_decorator(function):
    def wrapper_function(*args):
        print(f"You called {function.__name__}{args}\nIt returned: {function(*args)}")
    return wrapper_function


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a * b * c


a_function(inputs[0], inputs[1], inputs[2])
