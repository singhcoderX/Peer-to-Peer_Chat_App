import socket
import threading
PORT = 65432
IP_Address = '172.30.11.91' # give the ip_adress of peer1
def sending (conn):
    while True:
        inp = input("")

        conn.send(bytes(inp,"utf-8"))
        if inp == "exit":
            break
        f.write(inp + "\n")

def recieving(conn):
    while True:
        msg = conn.recv(1024)

        if msg.decode("utf-8") == "exit":
            break
        print(f"{socket.gethostname()}:" + msg.decode("utf-8"))
        f.write(f"{socket.gethostname()}:" + msg.decode("utf-8") + "\n")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((IP_Address,PORT))

filename = 'clientchat.txt'
try:
	f = open(filename)
	# Do something with the file
except IOError:
	#print("File not accessible")
	f = open(filename,'a+')
finally:
	for x in f:
		print(x)
	f.close()

f = open(filename,'a+')
t1 = threading.Thread(target = sending,args=(s,))
t2 = threading.Thread(target = recieving,args=(s,))

t1.start()
t2.start()

t1.join()
t2.join()
