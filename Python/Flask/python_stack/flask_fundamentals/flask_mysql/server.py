from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
from validation import Validation
app = Flask(__name__)
app.secret_key = 'This is some secure issh'

mysql = MySQLConnector(app, 'registration')

@app.route('/')
def index():
    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', users = users)

@app.route('/users/<user_id>')
def user(user_id):
    query = 'SELECT * FROM users WHERE id = :specific_id'
    data = {
    'specific_id': user_id
    }
    user = mysql.query_db(query, data)

    return render_template('/index.html', user = user[0])

@app.route('/users', methods=['POST'])
def add_user():
    request_form = [
        ('alpha','first_name', request.form['first_name']),
        ('alpha','last_name', request.form['last_name']),
        ('email','email', request.form['email']),
        ('pass_check','password', request.form['password'],request.form['confirm_password'], 8,16)
        ]

    sanitize = Validation(request_form)

    if len(sanitize.errors) == 0:
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES ( :first_name, :last_name, :email, :password, now(), now())'
        data = sanitize.data
        user_id = mysql.query_db(query, data)
        flash("You have successfully registered! You user ID is " + str(user_id) + ".")
        if 'data' in session:
            session.pop('data')
        return redirect('/')
    else:
        session['data'] = sanitize.data
        for error in sanitize.errors:
            flash(error)
        return redirect('/')

app.run(debug=True)
