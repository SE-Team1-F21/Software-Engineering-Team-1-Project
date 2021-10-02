from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/splash')
def splash():
    return render_template('splash.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        return render_template('game.html')





app.run(debug=True)