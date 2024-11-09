from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'secret'
# app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite://users.sqlite3'
# app.config['SQLAlchemy_DATABASE_URI'] = False
# app.permanent_session_lifetime = timedelta(minutes=30)

# db = SQLAlchemy(app)

# class user(db.Model):
#     _id = db.Column('id', db.Integer, primary_key=True)
#     username = db.Column('username', db.String(100))
#     email = db.Column('username', db.String(100))
#     first_name = db.Column('firstname', db.String(100))
#     last_name = db.Column('lastname', db.String(100))

    # def __init__(self, username, email, first_name, last_name):
    #     self.username = username
    #     self.email = email
    #     self.first_name = first_name
    #     self.last_name = last_name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
        return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template('user.html', user=user)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # db.create_all()
    app.run(port=8080, debug=True)