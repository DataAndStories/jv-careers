# FLASK WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# from flask module, import class Flask
from flask import Flask

# create app, an object of class Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


if __name__ == "__main__":
    print("I am inside if now")
    app.run(host="0.0.0.0", port=80, debug=True)