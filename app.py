from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/brianhaller/Desktop/dogs_flask/names.db'

db = SQLAlchemy(app)

class Names(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

# I had some trouble setting up the database and the names table.
# I had to do a number of steps in the command line that I didn't
# quite understand although I think they are just a part of how
# sqlite works.

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addname", methods=["POST"])
def addName():
    newName = request.form['name']
    post = Names(name = newName)
    db.session.add(post)
    db.session.commit()
    return redirect("/")

@app.route("/getnames")
def getNames():
    names = Names.query.all()
    return render_template("getDogs.html", names=names)

if __name__ == "__main__":
    app.run(debug=True)
