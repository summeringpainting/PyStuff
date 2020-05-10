# Socket server in python using select function

import socket, select

if __name__ == &quot;__main__&quot;:

    CONNECTION_LIST = []# list of socket clients
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((&quot;0.0.0.0&quot;, PORT))
    server_socket.listen(10)


    # Add server socket to the list of readable connections
    CONNECTION_LIST.append(server_socket)

    print &quot;Chat server started on port &quot; + str(PORT)

    while 1:
        # Get the list of sockets so they can be read through selct
        read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])

        for sock in read_sockets:

            # New connection
            if sock == server_socket:
                # Handle the case of the new connection at server_socket
                sockfd, addr = server_socket.accept()
                CONNECTION_LIST.append(sockfd)
                print &quot;Client (%s, %s) connected&quot; % addr

            # Incoming message from client
            else:
                # Data from client
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        sock.send('OK ...' + data)
            except:
                broadcast_data(sock, &quot;Client (%s, %s) is offline&quot; addr)
                print &quot;Client (%s, %s) is offline&quot; % addr
                sock.close()
                CONNECTION_LIST.remove(sock)
                continue
server_socket.close()
