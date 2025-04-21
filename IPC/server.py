# server.py
import socket

HOST = '127.0.0.1'
PORT = 5001

with socket.socket() as srv:
    srv.bind((HOST, PORT))
    srv.listen(1)
    print(f"Server listening on {HOST}:{PORT}…")
    conn, addr = srv.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            text = data.decode().strip()
            if text.lower() == 'exit':
                break
            try:
                n = int(text)
                result = str(n * n)
            except ValueError:
                result = "Error: send an integer"
            conn.sendall(result.encode())
    print("Connection closed.")
