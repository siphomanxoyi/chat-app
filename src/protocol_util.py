# Protocol for handling messages

from log_util import print_message
from queue_util import recv_q
from queue_util import send_q
from gram_class import Gram
from message_class import Message
from threading import Thread
from queue_util import message_inbox

import address_book_util
import message_util


def sort_messages_in():
    """ Process incoming messages."""
    from queue_util import in_connect
    from queue_util import in_fetch_users
    from queue_util import in_acks
    from queue_util import in_texts
    from queue_util import in_disconnect

    while True:
        message = message_inbox.get()
        print_message(repr(message))

        if message.action == Message.BLANK:
            return message
        elif message.action == Message.CONNECT:
            in_connect.put(message)
        elif message.action == Message.CONNECT_ACK:
            in_connect.put(message)
        elif message.action == Message.FETCH_USERS:
            in_fetch_users.put(message)
        elif message.action == Message.ACK:
            in_acks.put(message)
        elif message.action == Message.TEXT:
            in_texts.put(message)
        elif message.action == Message.DISCONNECT:
            in_disconnect.put(message)


def send_message(message: Message):
    """Send message."""

    gram = Gram()
    address = find_destination_address(message)
    gram.destination_address = address
    gram.payload = repr(message).encode()
    send_q.put(gram)


def find_destination_address(message: Message):
    """ Returns a tuple of the appropriate destination address and port for this message."""

    return address_book_util.address_book.get(message.target_user.upper())[0]


def start():
    """Start the protocol."""
    process_inbox = Thread(target=sort_messages_in, args=())
    process_inbox.start()


def main():
    print_message("Protocol Util")


if __name__ == "__main__":
    main()
