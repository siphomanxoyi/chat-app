
from log_util import print_message
from transmission_util import create_sockets
from queue_util import recv_q
from queue_util import send_q

import time

def setup():
    """Setup sockets and establish a connection."""
    create_sockets(True)
    time.sleep(1)


def main():
    print_message("Starting Server")
    setup()
    print_message(str(get_message()))


if __name__ == "__main__":
    main()
