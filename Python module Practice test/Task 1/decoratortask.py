import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Decorator to convert function output to uppercase
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

# Function to greet
@uppercase_decorator
def say_hello(name):
    return f"Hey, {name}"

# Test uppercase_decorator
greet = say_hello
print(greet("Muskan"))  # Output: "HEY, MUSKAN"

# Decorator to measure execution time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

# Apply timing_decorator to greet
@timing_decorator
def timed_greet(name):
    return greet(name)

# Test timed_greet
print(timed_greet("Bob"))

# Decorator to log arguments and result of the function
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Called {func.__name__} with arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Result: {result}")
        return result
    return wrapper

# Math class with decorators
class Math:
    @staticmethod
    @logging_decorator
    def add(a, b):
        return a + b

    @staticmethod
    @logging_decorator
    def subtract(a, b):
        return a - b

# Test Math class methods
math = Math()
print(math.add(5, 3))  # Logs: Called add with arguments: (5, 3), {}. Result: 8
print(math.subtract(10, 4))  # Logs: Called subtract with arguments: (10, 4), {}. Result: 6
