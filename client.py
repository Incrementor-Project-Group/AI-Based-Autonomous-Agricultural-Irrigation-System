# Sends random json packets to server over port 5000

import socket
import json
import random
import time


# Generate random json packet
def generate_json_packet():
    # Generate random json packet with hashed data bits
    return {
        "id": random.randint(1, 100),
        "timestamp": time.time(),
        "data": hash(str(random.randint(1, 100)))
    }


# Send json packet to server
def send_json_packet(sock, json_packet):
    # Send json packet to server
    sock.send(json.dumps(json_packet).encode())


ip = "127.0.0.1"
port = "5000"


if __name__ == "__main__":

    while True:

        # Create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to server
        sock.connect((ip, int(port)))

        # Generate random json packet
        json_packet = generate_json_packet()
        # Send json packet to server
        send_json_packet(sock, json_packet)
        time.sleep(1)
        sock.close()
