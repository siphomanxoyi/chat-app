
from log_util import print_message
from queue_util import send_q
from queue_util import recv_q
from gram_class import Gram

import message_class
import transmission_util
import time

def create_message():
    """Create a message."""
    #use message class



def create_user():
    """Create a user."""

def fetch_users():
    """Fetch a list of online users."""

def connect_to_server():
    """Connect to the server."""

def disconnect_from_server():
    """Disconnect from the server."""

def get_read_receipt():
    """Get read receipt for specific message."""

def verify_message():
    """Verify that messages are correctly received. (error detection)"""

def confirm_message_received():
    """Confirm that message is received. (loss detection)"""

def read_text_message():
    """Read a text message."""
    gram = recv_q.get()
    message = message_class.Message()
    message.unpack_from_gram(gram)
    return message.get_body()

def send_text_message(body:str):
    """Send a text message."""
    message = message_class.Message(body)
    gram = Gram()
    gram.payload = message.to_string().encode()
    gram.destination_address = transmission_util.server_public_address
    gram.destination_port = transmission_util.server_recv_port
    send_q.put(gram)

def setup():
    """Setup sockets and establish a connection."""
    transmission_util.create_sockets(False)
    time.sleep(1)


def main():
    print_message("Starting Client")
    setup()


if __name__ == "__main__":
    main()
