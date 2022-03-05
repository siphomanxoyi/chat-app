# Class for Messages.

class Message:
    def __init__(self, headers, body):
        self.headers = headers
        self.body = body

    def get_body(self) -> str:
        return self.body