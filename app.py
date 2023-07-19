from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
#db = SQLAlchemy(app)
#app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'



#class User(db,Model,UserMixin):
    #username = db.Column(db.String(20), nullable=false)
    #password = db.Column(db.String(80), nullable=false)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
