from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask.signals import request_started
from middleHandler import connection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('splash.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        print ("print should work")
        return render_template('playerEntry.html')

@app.route('/red_submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        #print ('route has been met?')
        dataResult = request.get_json(force=True)
        print (type(dataResult))
        for id, codeName in dataResult.items():
            connection(id, codeName)
        dataReply = {'this':'works'}
        return jsonify(dataReply)
    
    
@app.route('/red_submit', methods = ['GET','POST'])
def submit_2():
    if request.method == 'POST':
        print ('route has been met?')
        dataResult = request.get_json(force=True)
        #print (dataResult)

        dataReply = {'this':'works'}
        return jsonify(dataReply)



app.run(debug=True)