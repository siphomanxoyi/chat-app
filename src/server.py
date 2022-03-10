from log_util import print_message
from transmission_util import create_sockets
from threading import Thread
from message_class import Message
from queue_util import message_inbox
import protocol_util
import message_util
import time

username = "SERVER"
connections = 0

def connect_to_client(message: Message):
    """Connect to the server."""
    global connections
    import address_book_util

    if message.action == Message.CONNECT:  # SYN from client
        protocol_util.send_message(message_util.create_connect_ack_message(message))
    elif message.action == Message.CONNECT_ACK:  # Final ack from client
        connections += 1
        print_message("Connections: " + str(connections))


def setup():
    """Setup sockets and establish a connection."""
    create_sockets(True)
    time.sleep(1)


def main():
    print_message("Starting Server")
    setup()
    connect_to_client(message_inbox.get())


if __name__ == "__main__":
    main()
