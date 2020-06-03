# Miaouh
Miaouh is a simple client/server chat write in python.

# Usage
1. Open new shell then setup the server
`python Server.py`
2. In a separate shell setup the client
`python Client.py`

The client.py is the first to start the discussion.
The server is also a client but it handle the server socket.

# How it works ?
It use Tkinter as GUI and use alternaly mechanisms for the discussion between client and server.
A round is as following :
1. the client start a discussion then the client is in standby,
2. the server answers to the client then the server is in standby.

and it return to first phase.

# Authors
**LzOggar**
