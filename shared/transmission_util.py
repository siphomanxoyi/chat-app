# Util for sending and receiving messages over UDP
# Usage:
# 	1. create_sockets (is_server:bool) : Set to True if util is being used by server. False if client. 
# 	2. send (bytes_to_send, address: str, port: int) : Send bytes to recipient address and specified port.

import socket
from threading import Thread
from log_util import print_message


buffer_size = 1024
send_socket = None
recv_socket = None
server_address = "127.0.0.1"
server_send_port = 5678
server_recv_port = 8765


def create_udp_send_socket (is_server:bool):
	"""Creates and binds UDP socket for sending."""

	global send_socket

	send_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	if is_server:
		print_message("Created UDP send socket on SERVER.")
		send_socket.bind((server_address, server_send_port))
	else:
		print_message("Created UDP send socket on CLIENT.")
		send_socket.bind(('', 0))


def create_udp_recv_socket (is_server:bool):
	"""Creates and binds UDP socket for receiving."""

	global recv_socket

	recv_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	if is_server:
		print_message("Created UDP receive socket on SERVER.")
		recv_socket.bind((server_address, server_recv_port))
	else:
		print_message("Created UDP receive socket on CLIENT.")
		recv_socket.bind(('', 0))


def create_sockets (is_server:bool):
	"""Creates send and receive sockets and starts listening for messages."""

	create_udp_send_socket(is_server)
	create_udp_recv_socket(is_server)
	recv_start_listening()


def send (bytes_to_send, address: str, port: int):
	"""Send to recipient address at specified port."""

	global send_socket

	if send_socket == None:
		raise Exception ("Socket has not been created.")

	server_address_port = (address, port)
	send_socket.sendto(bytes_to_send, server_address_port)
	print_message("Sending to host " + address + ":" + str(port))
	
def listen ():
	"""Listens for incoming messages in background thread."""

	global recv_socket

	if send_socket == None:
		raise Exception ("Socket has not been created.")

	while(True):
		bytes_address_pair = recv_socket.recvfrom(buffer_size)
		# put these messages into a queue 


def recv_start_listening ():	
	"""Creates new thread to start listening for messages."""
	
	thread = Thread(target = listen, args = ())
	thread.start()
	print_message("Listening.")
	


def main ():
	print_message("Transmission Util")


if __name__ == '__main__':
	main()