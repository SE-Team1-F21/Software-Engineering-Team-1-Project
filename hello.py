from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

@app.route('/splash', methods=['GET', 'POST'])
def splash():
    return render_template('splash.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        return render_template('game.html')




if __name__ == '__main__':
    app.run(debug=True)