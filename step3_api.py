from flask import Flask, request, jsonify

app = Flask(__name__)

def read_numbers():
    a = request.args.get("a")
    b = request.args.get("b")
    
    # Guard 1: Were both sent?
    if a is None or b is None:
        return None, None, "Please send both a and b"
        
    # Guard 2: Are they valid numbers?
    try:
        return float(a), float(b), None
    except ValueError:
        return None, None, "a and b must be numbers"

@app.route("/add")
def add():
    a, b, error = read_numbers()
    if error:
        return jsonify({"error": error}), 400
    return jsonify({"operation": "add", "result": a + b}), 200

## Adding /divide

@app.route("/divide")
def divide():
    a, b, error = read_numbers()
    if error:
        return jsonify({"error": error}), 400
        
    # Business rule: cannot divide by zero
    if b == 0:
        return jsonify({"error": "Cannot divide by zero"}), 400
        
    return jsonify({"operation": "divide", "result": a / b}), 200

