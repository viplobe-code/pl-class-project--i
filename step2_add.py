from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def add():
    a = request.args.get("a")  # value after ?a=
    b = request.args.get("b")  # value after &b=
    total = float(a) + float(b)
    return f"{a} + {b} = {total}"