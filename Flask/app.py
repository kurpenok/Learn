from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

from datetime import datetime


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///articles.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Article(db.Model):
    identifier = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return "<Article %r>" % self.identifier


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/articles")
def articles():
    data = Article.query.order_by(Article.date.desc()).all()

    return render_template("articles.html", data=data)


@app.route("/articles/<int:identifier>")
def article(identifier: int):
    data = Article.query.get(identifier)
    return render_template("article.html", data=data)


@app.route("/create", methods=["POST", "GET"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        intro = request.form["intro"]
        text = request.form["text"]

        article = Article(title=title, intro=intro, text=text)
        
        try:
            db.session.add(article)
            db.session.commit()
            return redirect("/articles")
        except:
            return "[-] ERROR! Article was not added!"
    else:
        return render_template("create.html")


@app.route("/articles/<int:identifier>/edit", methods=["POST", "GET"])
def edit(identifier: int):
    data = Article.query.get(identifier)
    if request.method == "POST":
        data.title = request.form["title"]
        data.intro = request.form["intro"]
        data.text = request.form["text"]

        try:
            db.session.commit()
            return redirect("/articles")
        except:
            return "[-] ERROR! Article was not added!"
    else:
        return render_template("edit.html", data=data)


@app.route("/articles/<int:identifier>/delete")
def delete(identifier: int):
    data = Article.query.get_or_404(identifier)

    try:
        db.session.delete(data)
        db.session.commit()
        return redirect("/articles")
    except:
        return "[-] ERROR! An error occured while deleting!"



if __name__ == "__main__":
    app.run(debug=True)

