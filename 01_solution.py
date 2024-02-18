import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} - Time Elapsed: {end - start}")
        return result

    return wrapper


@timer
def exmaple_function(n):
    time.sleep(n)
    print("Function Completed")


exmaple_function(2)
