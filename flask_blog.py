from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'John Doe',
        'title': "Let's start!",
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Mister Okon',
        'title': "Let's finish!",
        'content': 'Second post content',
        'date_posted': 'April 21, 2020'
    },

]

@app.route("/home")
@app.route("/")
def hello():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

