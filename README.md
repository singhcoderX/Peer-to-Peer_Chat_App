# PeerChat: A Robust Peer-to-Peer Chat Application in Python3
PeerChat is a feature-rich, peer-to-peer chat application built using Python3 and Socket Programming. It offers a seamless communication experience for multiple clients, allowing them to chat directly with each other without any intermediary server.
***
     
## Installation
* Clone the Repo
 
  `git clone https://github.com/as10071999/Peer-to-Peer_Chat_App.git`
### Requirements
* Python 3
### Procedure
1. Install [python](https://www.python.org/downloads/) in your environment(pre-installed on Ubuntu)
2. Navigate to cloned directory

   `cd <project_directory_name> #Peer-to-Peer_Chat_App`
## Case I: Only 2 clients
1. Run Peer 1 on one terminal



    `python3 Peer1.py `

2. Run Peer 2 on other terminal

    `python3 Peer2.py `

> Note:Always run Peer 1 before Peer 2

## Case II: Multiple Clients

1. Navigate to multiple directory

   `cd multiple`

2. Run Server

   `python3 server.py`

3. Run clients
 
```   
   python3 client0.py 
   python3 client1.py 
   python3 client2.py 
```

>Note: Run Server first. Chatting will start only after 3 clients are connected.

* For more details see about.pdf
