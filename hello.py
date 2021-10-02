from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)
@app.route('/login')
def hello_world():
    return render_template('screen.html')