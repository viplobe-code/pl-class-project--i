
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# all the operations are here
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
}


def calculate(op, a, b):

    if op not in operations:
        return None, "Wrong operation"

    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        return None, "Enter valid numbers pls"

    if op == "divide" and b == 0:
        return None, "Can't divide by zero"

    ans = operations[op](a, b)
    return ans, None


# api route for getting result in json
@app.route("/api/<operation>")
def api(operation):

    a = request.args.get("a")
    b = request.args.get("b")

    result, error = calculate(operation, a, b)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "operation": operation,
        "result": result
    })


# main page for calculator
@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    error = None

    if request.method == "POST":

        op = request.form.get("operation")
        a = request.form.get("a")
        b = request.form.get("b")

        result, error = calculate(op, a, b)

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
