from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('splash.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        return render_template('playerEntry.html')

@app.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'GET':
        return render_template('splash.html')




app.run(debug=True)