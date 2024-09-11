class NegativeNumberError(Exception):
    pass

def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        if num1 < 0 or num2 < 0:
            raise NegativeNumberError("Negative numbers are not allowed.")
        result = num1 / num2
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except NegativeNumberError as e:
        print(e)
    else:
        print(f"The result is: {result}")
    finally:
        print("End of program execution.")

# Run the function
divide_numbers()
