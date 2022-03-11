from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, Flask!</h1>"


@app.route("/some")
def some():
    return "<h1>Some page</h1>"


if __name__ == "__main__":
    app.run(debug=True)

