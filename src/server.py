
from log_util import print_message
from transmission_util import create_sockets

import time




def setup():
    create_sockets(True)
    time.sleep(1)


def main():
    print_message("Starting Server")
    setup()


if __name__ == "__main__":
    main()
