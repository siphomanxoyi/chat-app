from log_util import print_message
from queue_util import recv_q
from queue_util import send_q
from message_class import Message
from gram_class import Gram
import transmission_util


def create_blank_message(source_user: str):
    """Create a Message object."""
    return Message(source_user=source_user)


def send_message(message: Message):
    """Send message to specified user."""
    gram = Gram()
    address = find_destination_address(message)
    gram.destination_address = address[0]
    gram.destination_port = address[1]
    gram.payload = repr(message).encode()
    send_q.put(gram)


def get_message():
    """Return a message from the queue."""


def find_destination_address(message: Message):
    """ Returns a tuple of the appropriate destination address and port for this message."""
    if message.target_user.upper() == "SERVER".upper():
        return (transmission_util.server_public_address, transmission_util.server_recv_port)

    # if it's to a user there needs to be a lookup of users addreses

def main():
    print_message("Message Util")
    print(repr(create_blank_message("keeran")))


if __name__ == "__main__":
    main()
