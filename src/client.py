from log_util import print_message
from queue_util import send_q
from queue_util import recv_q
from queue_util import message_inbox
from gram_class import Gram

import message_class
import transmission_util
import time
import protocol_util
import message_util

username = "USER_"
server_username = "SERVER"
connected = False


def set_username(nickname: str):
    """Set the username of the current user."""
    global username
    username = nickname


def connect_to_server():
    """Connect to the server."""
    global connected
    from queue_util import in_connect

    handshake_state = 0

    while not connected:
        if handshake_state == 0:  # SYN1
            syn = message_util.create_connect_message(username, server_username)
            protocol_util.send_message(syn)
            handshake_state += 1
        elif handshake_state == 1:  # SYN2-ACK1
            syn_ack = in_connect.get()
            if message_util.is_connect_ack_message(syn_ack):
                handshake_state += 1
        elif handshake_state == 2:  # SYN3-ACK2
            ack = message_util.create_connect_ack_message(syn_ack)
            protocol_util.send_message(ack)
            handshake_state += 1
        elif handshake_state == 3:
            connected = True
    time.sleep(1)
    print_message("Client-Server Handshake Complete.")
    return True


def fetch_users():
    """Fetch a list of online users."""
    from queue_util import in_fetch_users
    import address_book_util

    if connected:
        request = message_util.create_fetch_users_message(username, server_username)
        protocol_util.send_message(request)
        response = in_fetch_users.get()
        address_book_util.address_book = eval(response.body)
        return True
    return None


def send_text_message(body: str, recipient: str):
    """Send a text message to another user."""

    from queue_util import in_acks

    timeout = 5
    count = 5
    send_count = 0
    acked = False

    while not acked:
        count += 1

        if count > 3:
            message = message_util.create_text_message(username, server_username, recipient, body)
            protocol_util.send_message(message)
            count = 0
            send_count += 1
        try:
            ack_message = in_acks.get(timeout=timeout)  # retry after x seconds
            if ack_message.body == message.message_id:
                acked = True
            else:
                in_acks.put(ack_message)
                time.sleep(timeout)
        except:
            if send_count == 3:
                return False
            pass
    return True  # messaged received by SERVER

def get_next_text_message():
    """Receive TEXT messages."""
    from queue_util import in_texts
    from message_class import Message

    message = in_texts.get()
    return [message.convo_partner, message.target_user, message.body] # FROM , TO (THIS USER) , BODY

def disconnect_from_server():
    """Disconnect from the server."""
    global connected
    from queue_util import in_disconnect
    from message_util import Message

    close_state = 0

    while connected:
        if close_state == 0:
            dis = message_util.create_disconnect_message(username, server_username)
            protocol_util.send_message(dis)
            close_state += 1
        elif close_state == 1:
            dis_ack = in_disconnect.get()
            if dis_ack.action == Message.DISCONNECT:
                close_state += 1
        elif close_state == 2:
            connected = False
    time.sleep(1)
    return True


def verify_message():
    """Verify that messages are correctly received. (error detection)"""


def confirm_message_received():
    """Confirm that message is received. (loss detection)"""


def setup():
    """Setup sockets and establish a connection."""
    transmission_util.create_sockets(False)
    time.sleep(1)
    protocol_util.start()
    time.sleep(1)


def main():
    print_message("Starting Client")
    setup()
    if connect_to_server():
        fetch_users()


if __name__ == "__main__":
    main()
