from queue_util import recv_q
from queue_util import send_q

import message_class

def get_message():
    """Get a message off the queue."""
    gram = recv_q.get()
    message = message_class.Message()
    message.unpack_from_gram(gram)

    return message
