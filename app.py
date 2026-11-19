OPERATIONS = {
    "add":      lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide":   lambda a, b: a / b,
}

def calculate(operation, a_text, b_text):
    if operation not in OPERATIONS:
        return None, "Unknown operation"
    try:
        a, b = float(a_text), float(b_text)
    except (TypeError, ValueError):
        return None, "Please enter two valid numbers"
    if operation == "divide" and b == 0:
        return None, "Cannot divide by zero"
        
    return OPERATIONS[operation](a, b), None