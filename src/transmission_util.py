# Util for sending and receiving messages over UDP
# Usage:
# 	1. create_sockets (is_server:bool) : Set to True if util is being used by server. False if client. 
# 	2. send (bytes_to_send, address: str, port: int) : Send bytes to recipient address and specified port.

import socket
from threading import Thread
from log_util import print_message
from queue_util import recv_q
from queue_util import send_q
# from src.address_book_util import add_to_address_book
# from protocol_util import *

buffer_size = 1024
send_socket = None
recv_socket = None
server_local_address = "127.0.0.1"
server_public_address = "127.0.0.1"
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


def send(bytes_to_send, address):
    """Send to recipient address."""

    global send_socket

    if send_socket is None:
        raise Exception("Socket has not been created.")

    send_socket.sendto(bytes_to_send, address)
    print_message("TO: " + str(address))


def listen():
    """Listens for incoming messages in background thread."""

    global recv_socket

    if recv_socket is None:
        raise Exception("Socket has not been created.")

    return recv_socket.recvfrom(buffer_size)


def q_sender():
    """ Sends datagrams."""

    print_message("Send Queue Active.")
    while True:
        gram = send_q.get(block=True)
        send(gram.payload, gram.destination_address)


def q_listener():
    """ Receives datagrams."""
    from gram_class import Gram

    print_message("Listen Queue Active.")
    while True:
        datagram = listen()
        gram = Gram()
        gram.payload = datagram[0]
        gram.source_address = datagram[1]
        recv_q.put(gram)
        print_message("FROM: " + str(datagram[1]))

def q_process():
    """Processes incoming messages"""
    from message_class import Message
    from message_util import create_ack_message
    from protocol_util import send_message
    from address_book_util import address_book
    from address_book_util import add_to_address_book
    
    while True:
        gram = recv_q.get()
        message = eval(gram.payload.decode()) # Remember to go over this again because q.get() removes messages from queue
        print_message(repr(message))
        if message.action == Message.BLANK:
            return message
        elif message.action == Message.ACK:
            return message
        elif message.action == Message.PING:
            ack = create_ack_message(message)
            if address_book.get(message.source_user.upper())==None:
                add_to_address_book(message.source_user, gram.source_address)
            print_message(ack)
            send_message(ack)
            print_message("Reached end of message process")
            return message
    

def process_send_recv():
    """Creates new thread to sending and listening for messages."""

    thread_recv = Thread(target=q_listener, args=())
    thread_recv.start()
    thread_send = Thread(target=q_sender, args=())
    thread_send.start()
    thread_process = Thread(target=q_process, args=())
    thread_process.start()


def main():
    print_message("Transmission Util")


if __name__ == '__main__':
    main()
