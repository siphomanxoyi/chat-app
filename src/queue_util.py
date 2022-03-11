from log_util import print_message
import queue

send_q = queue.Queue()
recv_q = queue.Queue()
message_inbox = queue.Queue()


# Organised Queues for Incoming Messages
in_connect = queue.Queue()
in_fetch_users = queue.Queue()
in_texts = queue.Queue()
in_acks = queue.Queue()
in_disconnect = queue.Queue()

def main():
    print_message("Queue Util")


if __name__ == '__main__':
    main()
