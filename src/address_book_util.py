# Util for server to keep track of addresses of connected users
from transmission_util import server_public_address
from transmission_util import server_recv_port
from transmission_util import server_send_port

address_book = {"SERVER": [(server_public_address, server_recv_port), (server_public_address, server_send_port)]}


def add_to_address_book(user: str, recv_address, send_address):
    address_book[user.upper()] = [recv_address, send_address]


def remove_from_address_book(user: str):
    address_book.pop(user.upper())