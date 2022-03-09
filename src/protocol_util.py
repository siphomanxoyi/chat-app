# Protocol for handling messages

from log_util import print_message
from queue_util import recv_q
from queue_util import send_q
from gram_class import Gram
from message_class import Message

import address_book_util
import message_util


def process_message_in(message: Message):
    """ Process incoming messages."""

    print_message(repr(message))
    if message.action == Message.BLANK:
        return message
    elif message.action == Message.ACK:
        return message
    elif message.action == Message.PING:
        ack = message_util.create_ack_message(message)
        send_message(ack)
        return message


def process_message_out(message: Message):
    """ Process outgoing messages."""

    print_message(repr(message))
    if message.action == Message.BLANK:
        return None
    elif message.action == Message.PING:
        send_message(message)


def send_message(message: Message):
    """Send message."""

    gram = Gram()
    address = find_destination_address(message)
    gram.destination_address = address
    gram.payload = repr(message).encode()
    send_q.put(gram)


def receive_message():
    """Return a message from the queue."""
    gram = recv_q.get(block=True)
    message = eval(gram.payload.decode())

    if message.target_user.upper() == "SERVER":
        address_book_util.add_to_address_book(message.source_user, gram.source_address)

    process_message_in(message)


def find_destination_address(message: Message):
    """ Returns a tuple of the appropriate destination address and port for this message."""

    return address_book_util.address_book.get(message.target_user.upper())


def main():
    print_message("Protocol Util")


if __name__ == "__main__":
    main()
