import socket
import threading
from concurrent.futures import ThreadPoolExecutor
PORT = 65432
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(IPAddr)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),PORT))
s.listen(5)

def getMsg(conn):
    while True:
        msg = conn.recv(1024)
        if msg.decode("utf-8") == "exit":
            break

        #print(f"{socket.gethostname()}:" + msg.decode("utf-8"))
        target,text = msg.decode("utf-8").split(' ')
        #print("Target:"+target+" Text:"+text)
        #print(nodes[int(target)])
        nodes[int(target)].send(bytes(str(reverse_nodes[conn])+" "+text, "utf-8"))
        #print("Msg Sent To Target")
        print("Msg Transfered from :" + str(reverse_nodes[conn]) + " to : " + target)
def recieving():
    print("Recieving Task started")
    #
    # executor = ThreadPoolExecutor(len(all_connection))
    # for conn in all_connection:
    #     future = executor.submit(getMsg, (conn))
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(getMsg, all_connection)
    for result in results:
        print(result)


all_address = []
all_connection = []
nodes = {}
reverse_nodes = {}
def connection():
    key = 0
    while key<3:
        conn, adrr = s.accept()
        s.setblocking(1)  # prevents timeout
        all_address.append(adrr)
        all_connection.append(conn)
        nodes[key] = conn
        reverse_nodes[conn] = key
        key +=1
        print(f"Connected By{adrr}")
        # print(nodes)


task_connection= threading.Thread(target = connection,args=())
task_connection.start()
task_connection.join()
task_recieving = threading.Thread(target = recieving,args=())
if len(all_connection):
    task_recieving.start()


