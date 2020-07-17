import socket
import threading
PORT = 65432
IP_Address = '192.168.10.1' # give the ip_adress of peer1
def sending (conn):
    while True:
        print("->")
        inp = input("")

        conn.send(bytes(inp,"utf-8"))
        if inp == "exit":
            break
def recieving(conn):
    while True:
        msg = conn.recv(1024)

        if msg.decode("utf-8") == "exit":
            break
        sender,text =  msg.decode("utf-8").split(" ")
        print(sender+": "+text)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((IP_Address,PORT))
    print("Connected to Server!!")
    print("Enter Msg in this format: <ReceiverID> <Message_Without_Whitespace>")
    t1 = threading.Thread(target=sending, args=(s,))
    t2 = threading.Thread(target=recieving, args=(s,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

except:
    print("Connection is Lost!!")
