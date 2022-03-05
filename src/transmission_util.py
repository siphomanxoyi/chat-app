# Util for sending and receiving messages over UDP
# Usage:
# 	1. create_sockets (is_server:bool) : Set to True if util is being used by server. False if client. 
# 	2. send (bytes_to_send, address: str, port: int) : Send bytes to recipient address and specified port.

import socket
import time
from threading import Thread
from log_util import print_message
from queue_util import recv_q
from queue_util import send_q

buffer_size = 1024
send_socket = None
recv_socket = None
server_local_address = "127.0.0.1"
server_public_address = "192.143.121.98"
server_send_port = 5678
server_recv_port = 8765


def create_udp_send_socket(is_server: bool):
    """Creates and binds UDP socket for sending."""

    global send_socket

    send_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    if is_server:
        print_message("Created UDP send socket on SERVER.")
        send_socket.bind((server_local_address, server_send_port))
    else:
        print_message("Created UDP send socket on CLIENT.")
        send_socket.bind(('', 0))


def create_udp_recv_socket(is_server: bool):
    """Creates and binds UDP socket for receiving."""

    global recv_socket

    recv_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    if is_server:
        print_message("Created UDP receive socket on SERVER.")
        recv_socket.bind((server_local_address, server_recv_port))
    else:
        print_message("Created UDP receive socket on CLIENT.")
        recv_socket.bind(('', 0))


def create_sockets(is_server: bool):
    """Creates send and receive sockets and starts listening for messages."""

    create_udp_send_socket(is_server)
    create_udp_recv_socket(is_server)
    process_send_recv()


def send(bytes_to_send, address: str, port: int):
    """Send to recipient address at specified port."""

    global send_socket

    if send_socket == None:
        raise Exception("Socket has not been created.")

    server_address_port = (address, port)
    send_socket.sendto(bytes_to_send, server_address_port)


def listen():
    """Listens for incoming messages in background thread."""

    global recv_socket

    if recv_socket == None:
        raise Exception("Socket has not been created.")

    return recv_socket.recvfrom(buffer_size)


def q_sender():
    print_message("Send Queue Active.")
    while (True):
        gram = send_q.get(block=True)
        send(gram.payload, gram.destination_address, gram.destination_port)


def q_listener():
    print_message("Listen Queue Active.")
    while (True):
        recv_q.put(listen())
        ###################### listen() returns a pair of (bytes, address). turn this into a Gram and put on recv_q


def process_send_recv():
    """Creates new thread to sending and listening for messages."""

    thread_recv = Thread(target=q_listener, args=())
    thread_recv.start()
    thread_send = Thread(target=q_sender, args=())
    thread_send.start()


def main():
    print_message("Transmission Util")


if __name__ == '__main__':
    main()
