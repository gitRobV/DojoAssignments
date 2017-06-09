from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message = "No Ninja Here!")

@app.route('/ninja')
def ninja():
    return render_template('ninjas.html')

@app.route('/ninja/<color>')
def ninja_color(color):
    colors = {
    'blue': 'leonardo.jpg',
    'orange':'michelangelo.jpg',
    'red':'raphael.jpg',
    'purple': 'donatello.jpg'
    }
    if color in colors:
        result = colors[color]
    else:
        result = "notapril.jpg"
    return render_template('/ninja.html', ninja_image = result)

app.run(debug=True)
