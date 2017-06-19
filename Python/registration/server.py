from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = 'This is some secure issh'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    errors = False
    pw_verified = False
    data = {}
    required_fields = ['f_name', 'l_name', 'email', 'password', 'confirm_password']

    for input in required_fields:
        # Verify inputs are not empty
        if len(request.form[input]) == 0:
            flash(input + " cannot be empty!")
            errors = True
        # Verify Email input is Valid
        if input == 'email':
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(request.form[input]):
                flash(request.form[input] + " is not a valid email.")
                errors = True
        # Verify PW is greater than 8 characters and pw and confirm pw match
        elif input == 'password' or input == 'confirm_password':
            if len(request.form[input]) < 8:
                flash("Your password is too short!")
                errors = True
            if pw_verified == False:
                if request.form[input] == request.form['confirm_password']:
                    pw_verified = True
                else:
                    flash("Please confirm your passwords match")
                    errors = True
            # Continue to not store password info in session
            continue
        # check if f_name and l_name are only alpha chars
        elif input == 'f_name' or input == 'l_name':
            if not request.form[input].isalpha():
                flash("Your " + input + " contains invalid characters.")
                errors = True
        # add non pw inputs to data object
        data[input] = request.form[input]
    # If we have errors pass data obj to sessions and redirect to index route
    if errors == True:
        session['data'] = data
        return redirect('/')
    # If no errors pop data from session and pass data obj to results.html
    else:
        flash("You have successfully registered!")
        session.pop('data')
        return render_template('/results.html', data = data)

app.run(debug=True)
