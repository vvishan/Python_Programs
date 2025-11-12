def decorator(func):
    def wrapper():
        print("before strat of function")
        func()
        print("after completion of funtion")
    return wrapper



@ decorator
def say_hello():
    print("hello")

#say_hello()

import time
def decorator1(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time .time()
        print(f"{func.__name__} took {end- start:.4f} seconds")
        return result
    return wrapper

@decorator1
def train_model():
    time.sleep(2)
    print("model train complete")


train_model()

### AI/ML ues case example

def log_metrics(func):
    def wrapper(*args,**kwargs):
        print(f"Running the {func.__name__}")
        result = func(*args,**kwargs)
        print(f"completed the {func.__name__}:{result}")
        return result
    return wrapper

@log_metrics
def evaluate_model(*args,**kwargs):
    a = 4
    accuracy = 0.2
    return {"accuracy": accuracy,"also":a}

evaluate_model()


# ###| Syntax     | Meaning                                                                             |
# | ---------- | ----------------------------------------------------------------------------------- |
# | `*args`    | Used to pass a **variable number of positional arguments** to a function.           |
# | `**kwargs` | Used to pass a **variable number of keyword (name=value) arguments** to a function. |

