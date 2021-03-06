from log_util import print_message

from message_class import Message


def create_blank_message(source_user: str):
    """Create a Message object."""
    return Message(source_user=source_user)


def is_blank_message(message: Message):
    """Checks if Message action is BLANK"""
    if message.action == Message.BLANK:
        return True
    return False


def create_connect_message(source_user: str, target_user: str):
    """Create a Message object with action = CONNECT."""
    return Message(source_user=source_user, target_user=target_user, action=Message.CONNECT)


def is_connect_message(message: Message):
    """Checks if Message action is CONNECT"""
    if message.action == Message.CONNECT:
        return True
    return False


def create_connect_ack_message(message: Message):
    """Create a Message object with action = CONNECT_ACK."""
    return Message(source_user=message.target_user, target_user=message.source_user, action=Message.CONNECT_ACK,
                   body=message.message_id)


def is_connect_ack_message(message: Message):
    """Checks if Message action is CONNECT_ACK"""
    if message.action == Message.CONNECT_ACK:
        return True
    return False


def create_disconnect_message(source_user: str, target_user: str):
    """Create a Message object with action = DISCONNECT."""
    return Message(source_user=source_user, target_user=target_user, action=Message.DISCONNECT)


def create_disconnect_response_message(messsage: Message):
    """Create a Message object with action = DISCONNECT."""
    return Message(source_user=messsage.target_user, target_user=messsage.source_user, action=Message.DISCONNECT)


def create_ping_message(source_user: str, target_user: str):
    """Create a Message object with action = PING."""
    return Message(source_user=source_user, target_user=target_user, action=Message.PING)


def create_ack_message(message: Message):
    """Create a Message object with action = ACK."""
    return Message(source_user=message.target_user, target_user=message.source_user, action=Message.ACK,
                   body=message.message_id)


def is_ack_message(message: Message):
    """Checks if Message action is ACK"""
    if message.action == Message.ACK:
        return True
    return False


def create_fetch_users_message(source_user: str, target_user: str, body=""):
    """Create a Message object with action = FETCH_USERS."""
    return Message(source_user=source_user, target_user=target_user, action=Message.FETCH_USERS, body=body)


def is_fetch_users_message(message: Message):
    """Checks if Message action is FETCH_USERS"""
    if message.action == Message.FETCH_USERS:
        return True
    return False


def create_text_message(source_user: str, target_user: str, convo_partner: str, body: str):
    """Create a Message object with action = TEXT."""
    m = Message(source_user=source_user, target_user=target_user, action=Message.TEXT, body=body)
    m.convo_partner = convo_partner
    return m


def main():
    print_message("Message Util")


if __name__ == "__main__":
    main()
