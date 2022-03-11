# Class for Messages.
import base64
from uuid import uuid1
from gram_class import Gram


class Message:
    # Static variables that represent different types of messages
    BLANK = 0
    ACK = 1
    CONNECT = 2
    CONNECT_ACK = 5
    DISCONNECT = 3
    PING = 4

    def __init__(self, action=0, source_user="", target_user="", message_id=str(uuid1()), body="", hash=""):
        self.body = body
        self.action = action
        self.message_id = message_id
        self.source_user = source_user
        self.target_user = target_user
        self.hash = self.hash64(self)
        
    def __repr__(self):
        rep = f'Message(action={self.action}, source_user="{self.source_user}", target_user="{self.target_user}", message_id="{self.message_id}", body="{self.body}", hash="{self.hash}")'
        return rep

    def hash64(message):
        return (base64.b64encode(f'Message(action={message.action}, source_user="{message.source_user}", target_user="{message.target_user}", message_id="{message.message_id}", body="{message.body}")'.encode('ascii'))).decode('ascii')

    # def unhash64(message):
    #     base64_message = message.hash64
    #     base64_bytes = base64_message.encode('ascii')
    #     message_bytes = base64.b64decode(base64_bytes)
    #     uncoded_message = message_bytes.decode('ascii')
    #     return uncoded_message
    
    def validate(self):
        return self.hash64 == self.hash