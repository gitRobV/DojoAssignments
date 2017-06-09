from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'This is some secure issh'

@app.route('/')
def index():
    data = {}
    if 'rand_num' not in session:
        session['rand_num'] = random.randrange(0, 101)
        data['message'] = "I am thinking of a number between 1 and 100. Take a Guess!"
    elif 'result' in session:
        if session['result'] == "high":
            data['message'] = "Too High"
            data['color'] = "red"
            data['reset'] = False
        elif session['result'] == "low":
            data['message'] = "Too Low"
            data['color'] = "yellow"
            data['reset'] = False
        elif session['result'] == "win":
            data['message'] = "That's a Bingo!"
            data['color'] = "green"
            data['reset'] = True
    return render_template('index.html', data = data)

@app.route('/check', methods=['POST'])
def check():
    if int(request.form['user_guess']) == session['rand_num']:
        session['result'] = "win"
    elif int(request.form['user_guess']) > session['rand_num']:
        session['result'] = "high"
    elif int(request.form['user_guess']) < session['rand_num']:
        session['result'] = "low"
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('rand_num')
    session.pop('result')
    return redirect('/')

app.run(debug=True)
