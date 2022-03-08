# Class for Messages.
from uuid import uuid1
from gram_class import Gram
class Message:
    # Gram 'headers' for protocol
    blank = 0
    connect = 1
    data = 2
    disconnect = 3
    ack = 4
    def __init__(self):
        self.body = ""
        self.ack = False
        self.type = 0
        self.id = ''
        self.source = None
        self.destination = None

    def unpack_from_gram(self, gram: Gram):
        payload = gram.payload.decode()
        self.body = payload # there should be a method to separe body from headers

    def get_body(self) -> str:
        return self.body

    def set_body(self, body):
        self.body = body

    def __str__(self):
        return self.body

    def create_message(self, body, type, source, destination):
        self.body = body
        self.type = type
        self.id = str(uuid1())
        self.source = source
        self.destination = destination  
        