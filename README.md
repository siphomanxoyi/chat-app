# chat-app
An assignment where we had to implement our own protocol for a chat app that uses sockets and the UDP protocol to communicate.

# Required Features:
### Application Layer Protocol
- must support client-server architecture
- must use UDP as its transport layer
- users of the application need confirmation that their messages have been received by either the server or destination client 
- must verify that messages are correctly received (error detection)
- verify/confirm that all messages sent are received (loss detection)
- a mechanism for exchanging acknowledgement passages between clients and servers

### Client-Server Architecture
- implement a server that should manage the interaction between clients
- the different clients and the server should be able to run on different hosts over a network
- The client interface may have either a GUI or CLI, with appropriate user menus

### Chat Features
- must allow multiple pairs/groups of users to exchange messages in
real-time

### Additional Features
- authentication
- the ability for a user to retrieve historical messages from the server  (e.g if a user was offline when the messages were sent to them should be able to retrieve those messages when they come online)

# Protocol Design
- includes specification for the pattern of communication, message structure, as well communications rules
- uses text-based messaging (ASCII) in this application protocol design (like HTTP)
- specifies the acceptable sequence of messages at every
stage of communication (For example, a protocol may dictate that message exchange will only occur after a communication session has been set up)
- the message structure comprises at least the header and body
