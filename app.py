from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    link = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)
    clicks = db.Column(db.INTEGER, default=0)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/home', methods=['POST', 'GET'])
def home():
    articles = Article.query.order_by(Article.clicks.desc()).all()
    return render_template("index.html", articles=articles)


@app.route('/rer', methods=['POST', 'GET'])
def rer():
    art = Article.query.get(id)
    try:
        art.clicks = request.form['clicks']
        db.session.commit()
        return redirect('/')
    except:
        return "Plak"

    return redirect('/')


@app.route('/add', methods=['POST', 'GET'])
def ad():
    if request.method == "POST":
        link = request.form['link']
        name = request.form['name']
        article = Article(link=link, name=name)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/add')
        except:
            return "Что-то не так..."
    else:
        return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)
