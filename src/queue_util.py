from log_util import print_message
import queue

send_q = queue.Queue()
recv_q = queue.Queue()
message_inbox = queue.Queue()


def main():
    print_message("Queue Util")


if __name__ == '__main__':
    main()
