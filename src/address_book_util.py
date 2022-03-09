# Util for server to keep track of addresses of connected users
from transmission_util import server_public_address
from transmission_util import server_recv_port

address_book = {"SERVER": (server_public_address, server_recv_port)}


def add_to_address_book(user: str, address):
    address_book[user.upper()] = address


def remove_from_address_book(user: str):
    address_book.pop(user.upper())
