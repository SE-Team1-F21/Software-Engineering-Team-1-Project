import socket
import random
import time

bufferSize  = 1024
serverAddressPort   = ("127.0.0.1", 7501)


with open('./files/rednames.txt') as f:
	redTeam = f.readlines()[0].split(',')
with open('./files/greennames.txt') as f:
	greenTeam = f.readlines()[0].split(',')

counter = 100

# Create datagram socket
UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# counter number of events, random player and order
i = 1

#time.sleep(30) #could use to wait the 30 seconds on the timer
while i < int(counter): #could set time.sleep to 1 second each time and then set counter to 6 minutes in seconds

	if random.randint(1,2) == 1:
		message = "r" + ":" + str(random.randint(1,len(redTeam)-1)) + ":" + str(random.randint(1,len(greenTeam)-1))
	else:
		message = "g" + ":" + str(random.randint(1,len(greenTeam)-1)) + ":" + str(random.randint(1,len(redTeam)-1))
	print(message)
	i+=1;
	UDPClientSocketTransmit.sendto(str.encode(str(message)), serverAddressPort)
	time.sleep(random.randint(1,3))
	
print("program complete")