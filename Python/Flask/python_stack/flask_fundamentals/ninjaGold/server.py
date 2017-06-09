from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import random
app = Flask(__name__)
app.secret_key = 'This is some secure issh'

@app.route('/')
def index():
    if 'user_gold' not in session:
        session['user_gold'] = 0
    if 'user_log' not in session:
        session['user_log'] = []

    return render_template('index.html')


@app.route('/process_money',methods=['POST'])
def process():
    if request.form['building'] == 'farm':
        reward = random.randrange(10, 20)
    elif request.form['building'] == 'cave':
        reward = random.randrange(5, 10)
    elif request.form['building'] == 'house':
        reward = random.randrange(2, 5)
    elif request.form['building'] == 'casino':
        reward = random.randrange(-50, 50)
    session['user_gold'] += reward
    date = datetime.now().strftime('%Y-%m-%d %I:%M')
    log = (request.form['building'],reward,date)
    session['user_log'].insert(0,log)
    return redirect('/')


app.run(debug=True)
