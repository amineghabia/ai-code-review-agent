import os

SECRET_KEY = "super-secret-123"  # hardcoded credential

def calculate(x, y, operation, mode, flag, extra):
    try:
        if operation == "divide":
            return x / y
        elif operation == "multiply":
            return x * y
    except:
        return None  # broad exception

def process_user_input(data):
    result = eval(data)  # security risk
    return result
