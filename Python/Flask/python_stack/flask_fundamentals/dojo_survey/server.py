from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'This is some secure issh'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    errors = False

    if ( len( request.form['name'] ) < 2 ):
        flash("Name cannot be empty!")
        errors = True
    if ( len( request.form['location'] ) < 2 ):
        flash("Location cannot be empty!")
        errors = True
    if ( len( request.form['language'] ) < 2 ):
        flash("Language cannot be empty!")
        errors = True
    if ( len( request.form['comment'] ) > 120 ):
        flash("Comment is too long!")
        errors = True
    if errors == True:
        return redirect('/')
    else:
        data = {
        "name": request.form['name'],
        "location": request.form['location'],
        "languge":request.form['language'],
        "comment": request.form['comment']
        }
        return render_template('/results.html', data = data)

app.run(debug=True)
