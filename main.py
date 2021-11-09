from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask.signals import request_started
from middleHandler import connection

#http://127.0.0.1:5000/ 

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
    return render_template('playAction.html')



app.run(debug=True)
