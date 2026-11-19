# Our first web app using Flask

from flask import Flask

app = Flask(__name__) # This will create the web app 

@app.route("/")  # This is the route for the home page
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True) # Will start listening for requests
