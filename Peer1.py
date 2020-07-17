import socket
import threading

PORT = 65432

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),PORT))
s.listen(5)
conn, adrr = s.accept()


print(f"Connected By{adrr}")
filename = 'mychat.txt'
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
        print(f"{socket.gethostname()}:"+msg.decode("utf-8"))
        f.write(f"{socket.gethostname()}:" + msg.decode("utf-8") + "\n")



t1 = threading.Thread(target = sending,args=(conn,))
t2 = threading.Thread(target = recieving,args=(conn,))

t1.start()
t2.start()

t1.join()
t2.join()
f.close()
print("")
