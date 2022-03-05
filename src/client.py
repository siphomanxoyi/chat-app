
from log_util import print_message
from transmission_util import create_sockets
import time


def create_message():
    """Create a message."""

def read_message():
    """Read a message."""

def send_message():
    """Send a message."""

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

def setup():
    """Setup sockets and establish a connection."""
    create_sockets(False)
    time.sleep(1)


def main():
    print_message("Starting Client")
    setup()


if __name__ == "__main__":
    main()
