# Import socket module
import socket
import time
import sys, errno  

timeTakenNet = 0
countNet = 0

def AverageTimeCalculator():
	if countNet != 0:
		print("\nNumber of Calls:", countNet)
		print("Average processing time each call: ", timeTakenNet/countNet - 10)
	sys.exit()

def Main():
	# local host IP '127.0.0.1'
	host = '127.0.0.1'

	# Define the port on which you want to connect
	port = 12345

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# connect to server on local computer
	s.connect((host,port))

	count =10
	# message you send to server
	message = "this is the message being sent"
	while count>0:
		start_time = time.time()
		# message sent to server
		s.send(message.encode('ascii'))
		
		data = s.recv(1024)
		time_taken = time.time() - start_time
		global timeTakenNet, countNet
		timeTakenNet += time_taken
		countNet += 1

		print('Time Taken =',time_taken)
		# time.sleep(1)
		count -= 1
		continue

	# close the connection
	s.close()
	AverageTimeCalculator()


if __name__ == '__main__':
	Main()

