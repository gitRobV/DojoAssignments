from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'This is some secure issh'

@app.route('/')
def index():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template('index.html')

@app.route('/double_up')
def double():
    session['visits'] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session['visits'] = 0
    return redirect('/')

app.run(debug=True)
