# Class that encapsulates message to be sent

class Gram:
    def __init__(self):
        self.destination_address = None
        self.destination_port = None
        self.source_address = None
        self.source_port = None
        self.payload = None