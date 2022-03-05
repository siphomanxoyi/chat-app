# Class for Messages.
from gram_class import Gram
class Message:
    def __init__(self):
        self.body = ""

    def unpack_from_gram(self, gram: Gram):
        payload = gram.payload.decode()
        self.body = payload # there should be a method to separe body from headers

    def get_body(self) -> str:
        return self.body

    def set_body(self, body):
        self.body = body

    def __str__(self):
        return self.body