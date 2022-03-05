# This util formats output printed to screen with a timestamp

from datetime import datetime


def print_message(message):
    print(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), " | ", message)
