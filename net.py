#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected like a mofo", addr)
        while True:
            dat = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
