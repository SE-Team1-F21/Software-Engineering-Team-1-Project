from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask.signals import request_started
from middleHandler import connection



import socket


#http://127.0.0.1:5000/ 

# def loadSocket():
ip = "127.0.0.1"
port = 7501
sock = socket.socket(socket.AF_INET,
                    socket.SOCK_DGRAM)
sock.bind((ip, port))



# loadSocket()






app = Flask(__name__)

@app.route("/")
def home():
    return render_template('splash.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    
    
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


##LOOK HERE!!!!!!!
@app.route('/action',methods=['GET', 'POST'])
def playerAction():
    print(f'Start listening to {ip}:{port}')
    while True:
        data, addr = sock.recvfrom(1024) # buffer
        print(f"received message: {data}")
        break
    return render_template('playAction.html',name = data)

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



app.run(debug=True)
