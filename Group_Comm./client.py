# client.py
import socket
import threading

HOST = '127.0.0.1'
PORT = 5001

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            break

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        # start listener thread
        threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

        # first prompt (server asks for name)
        # then echo any further prints from receive_messages

        while True:
            msg = input("Enter Message : ")
            sock.sendall(msg.encode())
            if msg.lower() == 'exit':
                break

if __name__ == '__main__':
    main()
