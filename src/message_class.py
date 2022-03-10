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

    def __init__(self, action=0, source_user="", target_user="", message_id=str(uuid1()), body="", hash64=""):
        self.body = body
        self.action = action
        self.message_id = message_id
        self.source_user = source_user
        self.target_user = target_user
        self.hash64 = (base64.b64encode(("action="+str(action)+"\n"+"source_user="+self.source_user+"\n"+"target_user="+self.target_user+"\n"+"message_id="+self.message_id+"\n"+"body="+self.body).encode('ascii'))).decode('ascii')
        
    def __repr__(self):
        rep = f'Message(action={self.action}, source_user="{self.source_user}", target_user="{self.target_user}", message_id="{self.message_id}", body="{self.body}")'
        return rep
