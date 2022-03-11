from log_util import print_message
from transmission_util import create_sockets
from threading import Thread
from message_class import Message
from queue_util import message_inbox
import protocol_util
import message_util
import time

username = "SERVER"


def client_connections():
    """Connect to the server."""
    from queue_util import in_connect
    while True:
        message = in_connect.get()

        if message.action == Message.CONNECT:  # SYN from client
            protocol_util.send_message(message_util.create_connect_ack_message(message))
        elif message.action == Message.CONNECT_ACK:  # Final ack from client
            print_message("Connected to: " + message.source_user.upper())


def setup():
    """Setup sockets and establish a connection."""
    create_sockets(True)
    time.sleep(1)
    protocol_util.start()
    time.sleep(1)
    handshaker = Thread(target=client_connections, args=())
    handshaker.start()


def main():
    print_message("Starting Server")
    setup()


if __name__ == "__main__":
    main()
