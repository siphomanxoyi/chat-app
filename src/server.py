
from log_util import print_message
from transmission_util import create_sockets
from queue_util import recv_q
import time


def setup():
    create_sockets(True)
    time.sleep(1)
    print_message(recv_q.get())


def main():
    print_message("Starting Server")
    setup()


if __name__ == "__main__":
    main()
