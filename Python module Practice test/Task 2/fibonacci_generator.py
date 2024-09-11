def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Test Fibonacci generator
for number in fibonacci_generator(10):
    print(number)
