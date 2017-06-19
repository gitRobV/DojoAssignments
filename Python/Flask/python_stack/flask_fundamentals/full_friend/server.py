from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from validation import Validation
import md5
app = Flask(__name__)

app.secret_key = 'This is some secure issh'

mysql = MySQLConnector(app, 'flask_project')

@app.route('/')
def index():
    if 'user' not in session or session['user']['status'] != 'active':
        return redirect('/login')
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('/login.html')

@app.route('/login', methods=['POST'])
def auth_user():
    email_query = 'SELECT * FROM users WHERE email = :email'
    user_exists = mysql.query_db(email_query, {'email': request.form['email']})

    if len(user_exists) !=0:
        pw_attempt = md5.new(request.form['password'] + user_exists[0]['salt']).hexdigest()
        if user_exists[0]['password'] == pw_attempt:
            session['user'] = {
            'status':'active',
            'user_id': user_exists[0]['id'],
            'first_name': user_exists[0]['first_name'],
            'last_name': user_exists[0]['last_name'],
            'email': user_exists[0]['email']
            }
            if 'data' in session:
                session.pop('data')
            return redirect('/')
    flash('Authentication failed with information provided. Please review your email/password combination')
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

@app.route('/register')
def register():
    return render_template('/register.html')

@app.route('/register', methods=['POST'])
def add_user():
    request_form = [
        ('alpha','first_name', request.form['first_name']),
        ('alpha','last_name', request.form['last_name']),
        ('email','email', request.form['email']),
        ('pass_check','password', request.form['password'],request.form['confirm_password'], 8,16)
        ]

    sanitize = Validation(request_form)

    email_query = 'SELECT id FROM users WHERE email = :email'
    email_exists = mysql.query_db(email_query, {'email': request.form['email']})

    if len(email_exists) > 0:
        sanitize.errors.append('User exists with email provided.')

    if len(sanitize.errors) == 0:
        data = sanitize.data
        query = 'INSERT INTO users (first_name, last_name, email, password, salt, created_at, updated_at) VALUES ( :first_name, :last_name, :email, :password, :salt, now(), now())'
        user_id = mysql.query_db(query, data)
        flash('You have successfully registered! You user ID is ' + str(user_id) + '.')
        session['user'] = {
        'status':'active',
        'user_id': user_id,
        'first_name': sanitize.data['first_name'],
        'last_name': sanitize.data['last_name'],
        'email': sanitize.data['email'],
        }
        if 'data' in session:
            session.pop('data')
        return redirect('/')
    else:
        session['data'] = sanitize.data
        for error in sanitize.errors:
            flash(error)
        return redirect('/register')


@app.route('/friends')
def friends():
    # get_friends_query = "SELECT curr_user.id AS user_id, CONCAT(curr_user.first_name, ' ', curr_user.last_name) AS user_name, curr_user.email AS request_email, friend_user.id AS friends_id, CONCAT(friend_user.first_name, ' ', friend_user.last_name) AS friend_name, friend_user.email AS friend_email FROM users AS curr_user LEFT JOIN friendships as f ON curr_user.id = f.user_id LEFT JOIN users AS friend_user ON  f.friend_id = friend_user.id WHERE f.user_id = :curr_user or f.friend_id = :curr_user;"
    # data = {
    # 'curr_user': session['user']['user_id']
    # }
    # friend_list = mysql.query_db(get_friends_query,data)

    friends_query = "SELECT users.first_name, users.last_name, users.email FROM friendships JOIN users ON friendships.friend_id = users.id WHERE friendships.status = 'Confirmed' AND friendships.user_id = :user_id"
    data = {
    'user_id': session['user']['user_id']
    }
    users_friends = mysql.query_db(friends_query, data)

    request_query ="SELECT users.first_name, users.last_name, users.email FROM friendships JOIN users ON friendships.user_id = users.id WHERE friendships.status = 'Pending' AND friendships.friend_id = :user_id"

    request_list = mysql.query_db(request_query, data)

    result_data = [users_friends,request_list]

    return render_template('/friends.html',result_data = result_data)

@app.route('/friends/add')
def add_friends():
        return render_template('/add_friends.html')

@app.route('/friends', methods=['POST'])
def post_friends():

    request_form = [('email','email', request.form['email'])]
    sanitize = Validation(request_form)

    email_query = 'SELECT id FROM users WHERE email = :email'
    email_exists = mysql.query_db(email_query, {'email': request.form['email']})
    print email_exists[0]['id']

    if len(email_exists) == 0:
        sanitize.errors.append('Email provided does not belong to a current user!')

    if len(sanitize.errors) == 0:
        data = {
        'user_id': int(session['user']['user_id']),
        'friend_id': email_exists[0]['id'],
        'status': request.form['status']
        }
        if data['status'] == 'Confirmed':
            update_query = 'UPDATE friendships SET status="Confirmed" WHERE friend_id = :user_id and user_id = :friend_id'
            mysql.query_db(update_query, data)

        insert_friend = 'INSERT INTO friendships (user_id, friend_id, status, created_at, updated_at) VALUES ( :user_id, :friend_id, :status, now(), now() )'
        row_id = mysql.query_db(insert_friend, data)
        flash("Your friend request is " + data['status'])
        return redirect('/friends')
    else:
        session['data'] = sanitize.data
        for error in sanitize.errors:
            flash(error)
        return redirect('/friends/add')

















app.run(debug=True)
