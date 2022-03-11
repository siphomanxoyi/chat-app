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


def send_address_book():
    """Connect to the server."""
    from queue_util import in_fetch_users
    import address_book_util
    while True:
        message = in_fetch_users.get()

        if message.action == Message.FETCH_USERS:
            book = repr(address_book_util.address_book)
            m = message_util.create_fetch_users_message(username, message.source_user, book)
            protocol_util.send_message(m)
        print_message("Sending list of users to: " + message.source_user.upper())

def route_text_messages():
    """Routes TEXT messages to recipients."""
    from queue_util import in_texts
    import address_book_util

    while True:
        message = in_texts.get()

        if message.action == Message.TEXT:
            ack = message_util.create_ack_message(message)
            protocol_util.send_message(ack)


def setup():
    """Setup sockets and establish a connection."""
    create_sockets(True)
    time.sleep(1)
    protocol_util.start()
    time.sleep(1)
    handshaker = Thread(target=client_connections, args=())
    handshaker.start()
    yellow_pages = Thread(target=send_address_book, args=())
    yellow_pages.start()
    grapevine = Thread(target=route_text_messages, args=())
    grapevine.start()


def main():
    print_message("Starting Server")
    setup()


if __name__ == "__main__":
    main()
