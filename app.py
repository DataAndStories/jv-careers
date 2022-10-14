# FLASK WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# from flask module, import class Flask
from flask import Flask, render_template

# create app, an object of class Flask
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)