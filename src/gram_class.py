# Class that encapsulates message to be sent

class Gram:
    def __init__(self, source_address="", source_port=0, destination_address="", destination_port=0, payload="".encode()):
        self.destination_address = destination_address
        self.destination_port = destination_port
        self.source_address = source_address
        self.source_port = source_port
        self.payload = payload