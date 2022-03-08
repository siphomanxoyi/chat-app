from log_util import print_message

from message_class import Message



def create_blank_message(source_user: str):
    """Create a Message object."""
    return Message(source_user=source_user)

def create_ping_message(source_user: str, target_user: str):
    """Create a Message object with action = PING."""
    return Message(source_user=source_user, target_user=target_user, action=Message.PING)

def create_ack_message(message: Message):
    """Create a Message object with action = ACK."""
    return Message(target_user=message.source_user, action=Message.ACK, body=message.message_id)

def main():
    print_message("Message Util")


if __name__ == "__main__":
    main()
