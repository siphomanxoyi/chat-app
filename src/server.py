
from log_util import print_message
from transmission_util import create_sockets
import protocol_util

import time

username = "SERVER"

def setup():
    """Setup sockets and establish a connection."""
    create_sockets(True)
    time.sleep(1)


def main():
    global username

    print_message("Starting Server")
    setup()
    protocol_util.receive_message()


if __name__ == "__main__":
    main()
