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
    TEXT = 6
    FETCH_USERS = 7

    def __init__(self, action=0, source_user="", target_user="", convo_partner="", message_id=str(uuid1()), body="", hash=""):
        self.body = body
        self.action = action
        self.message_id = message_id
        self.source_user = source_user
        self.target_user = target_user
        self.convo_partner = convo_partner
        self.hash = hash

    def __repr__(self):
        rep = f'Message(action={self.action}, source_user="{self.source_user}", target_user="{self.target_user}", convo_partner="{self.convo_partner}", message_id="{self.message_id}", body="{self.body}", hash="{self.hash}")'
        return rep

    def hash64(self):
        self.hash = (base64.b64encode((repr(self)).encode('ascii'))).decode('ascii')

    def validate(self):
        old_hash = self.hash
        self.hash = ""
        self.hash64()

        if old_hash == self.hash:
            return True
        else:
            self.hash = old_hash
            return False
