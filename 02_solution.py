def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ", ".join([str(a) for a in args])
        kwargs_values = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        print(f"Calling {func.__name__} with arguments: {args_values}, {kwargs_values}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


@debug
def great(name, greating="Hello"):
    return f"{greating}, {name}"


print(great("John", greating="Good Morning"))
