from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/some")
def some():
    return render_template("some.html")


@app.route("/user/<string:name>/<int:identifier>")
def user(name: str, identifier: int):
    return f"User page: {name} - {identifier}"


if __name__ == "__main__":
    app.run(debug=True)

