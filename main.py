from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask.signals import request_started
from middleHandler import connection
from python_udpserver import listen
import subprocess
import os
from sys import platform

#http://127.0.0.1:5000/ 

app = Flask(__name__)

p = None

@app.route("/")
def home():
    return render_template('splash.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    if(p is not None):
        p.kill()
    if request.method == 'GET':
        print ("print should work")
        with open("files/rednames.txt", "w") as fo:
            fo.write("")
        with open("files/greennames.txt", "w") as fo:
            fo.write("")
        return render_template('playerEntry.html')

@app.route('/red_submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        #print ('route has been met?')
        playerInfo = []
        dataResult = request.get_json(force=True)
        for i in dataResult.keys():
            for j in dataResult.values():
                playerInfo.append(i)
                playerInfo.append(j)
        playerInfo.append('R')
        print(playerInfo)
  

        ##playerInfo contains the following
        #[id,name,team_color]


        for id, codeName in dataResult.items():
            connection(id, codeName)
        dataReply = {'this':'works'}
        return jsonify(dataReply)
    
##To be worked on
@app.route('/green_submit', methods = ['GET','POST'])
def submit_2():
    if request.method == 'POST':
        playerInfo = []
        print ('route has been met?')
        dataResult = request.get_json(force=True)
        #print (dataResult)
        for i in dataResult.keys():
            for j in dataResult.values():
                playerInfo.append(i)
                playerInfo.append(j)
        

        ##playerInfo = [id,name,team_color]
        playerInfo.append('G')
        print(playerInfo)
        
        for id, codeName in dataResult.items():
            connection(id, codeName)
        dataReply = {'this':'works'}
        return jsonify(dataReply)

@app.route('/action',methods=['GET', 'POST'])
def playerAction():
    global p
    cmd_line = 'python3 python_trafficgenerator.py' 
    p = os.popen(cmd_line)

    return render_template('playAction.html')

@app.route('/set_string',methods=['GET', 'POST'])
def redSet():
    if request.method == 'POST':
        print (request.data)
        with open("files/rednames.txt", "w") as fo:
            fo.write(request.data.decode("utf-8"))
        return "hi lol"

@app.route('/set_string_green',methods=['GET', 'POST'])
def greenSet():
    if request.method == 'POST':
        print (request.data)
        with open("files/greennames.txt", "w") as fo:
            fo.write(request.data.decode("utf-8"))
        return "hi lol"

@app.route('/rednames',methods=['GET', 'POST'])
def redPull():
    with app.open_resource("files/rednames.txt") as f:
        content = f.read()
    return content

@app.route('/greennames',methods=['GET', 'POST'])
def greenPull():
    with app.open_resource("files/greennames.txt") as f:
        content = f.read()
    return content

@app.route('/receive',methods=['GET', 'POST'])
def receive():
    return listen()



app.run(debug=True)
