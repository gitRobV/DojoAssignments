from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'This is some secure issh'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect('/show')
@app.route('/show')
def show_user():
    name = session['name']
    email = session['email']
    return render_template('user.html', name = name, email = email)

app.run(debug=True)
