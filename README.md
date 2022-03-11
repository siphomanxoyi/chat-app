# chat-app
An assignment where we had to implement our own protocol for a chat app that uses sockets and the UDP protocol to communicate.

# Features:
- GUI client interface.
- multiple pairs/groups of users to exchange messages in
  real-time
- client-server architecture.
- uses UDP as its transport layer.
- users of the application receive confirmation that their messages have been received by the server.
- verification of that messages to ensure they are correctly received (error detection).
- simulated reliability via acknowledgement passages between client and server.


# Setup and Run:
1. Start the server.

    ```python src/server.py```

2. Start a client.

    ``python src/driver.py``