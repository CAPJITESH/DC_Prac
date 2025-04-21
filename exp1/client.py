# client.py
import socket

HOST = '127.0.0.1'
PORT = 5001

with socket.socket() as cli:
    cli.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")
    while True:
        msg = input("Enter integer (or 'exit'): ").strip()
        cli.sendall(msg.encode())
        if msg.lower() == 'exit':
            break
        resp = cli.recv(1024).decode()
        print("Square is:", resp)
    print("Client exiting.")
