# Class socket

> Adapted from [Python_Tutorial.pdf](../Python_Tutorial.pdf) — Chapter 29, TCP/IP

Before each use of `socket`, add the statement `import socket` to the top of the Python file.

- **`socket([af, type, proto])`**: Creates a socket.
  - `af`: Address family.
    - `socket.AF_INET`: IPv4
    - `socket.AF_INET6`: IPv6
  - `type`: Socket type.
    - `socket.SOCK_STREAM`: TCP stream
    - `socket.SOCK_DGRAM`: UDP datagram
    - `socket.SOCK_RAW`: Raw socket
    - `socket.SO_REUSEADDR`: Reusable socket
  - `proto`: Protocol number.
    - `socket.IPPROTO_TCP`: TCP mode
    - `socket.IPPROTO_UDP`: UDP mode
- **`socket.setsockopt(level, optname, value)`**: Sets socket options.
  - `level`: Level of the socket option.
    - `socket.SOL_SOCKET`: Level of socket option. Default is 4095.
  - `optname`: Option name.
    - `socket.SO_REUSEADDR`: Allows a socket to bind to an address already in use.
  - `value`: An integer or a bytes-like object representing a buffer.
- **`socket.connect(address)`**: Connects to a server.
  - `address`: Tuple or list of the server's address and port number.
- **`send(bytes)`**: Sends data and returns the number of bytes sent.
- **`recv(bufsize)`**: Receives data and returns a bytes object representing the data received.
- **`close()`**: Closes the socket.

> To learn more, visit: http://docs.micropython.org/en/latest/
