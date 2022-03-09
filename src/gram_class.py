# Class that encapsulates message to be sent

class Gram:
    def __init__(self, source_address="", destination_address="", payload="".encode()):
        self.destination_address = destination_address
        self.source_address = source_address
        self.payload = payload
