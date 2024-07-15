import time

def log_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

@log_time
def add_numbers(x, y):
    return x + y

result = add_numbers(10, 20)  # Output: Function 'add_numbers' executed in 0.0001 seconds. 30