# Server-Side that receives json packets from client over the network using port 5000. Then it saves the json packet to a file with the filename of current time.

import socket
import json
import sys
import os
import time
import threading
import queue
import random
import string


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind the socket to the port
server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)


# Listen for incoming connections
sock.listen(1)


# Function to receive json packets from client
def receive_json(conn):
    data = conn.recv(1024)
    data = data.decode('utf-8')
    data = json.loads(data)
    return data


# Saves json packets to file and name it with id


def save_json(data):
    filename = ''.join(random.choice(
        string.digits) for _ in range(3))
    filename = filename + '.json'
    with open(filename, 'w') as f:
        json.dump(data, f)


if __name__ == '__main__':
    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)

            # Receive the data in json format
            data = receive_json(connection)
            print('received {!r}'.format(data))

            # Save the json packet to a file
            filename = save_json(data)
            print('saved to', filename)

        finally:
            # Clean up the connection
            connection.close()
