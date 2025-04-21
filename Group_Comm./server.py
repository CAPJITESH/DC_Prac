# server.py
import socket
import threading

HOST = '127.0.0.1'
PORT = 5001

clients = []
clients_lock = threading.Lock()

def broadcast(message, _sender=None):
    """Send message to all connected clients."""
    with clients_lock:
        for conn, name in clients:
            try:
                # optionally skip echo back to sender:
                # if conn is _sender: continue
                conn.sendall(message.encode())
            except:
                pass

def handle_client(conn, addr):
    try:
        # 1) receive the client's name
        conn.sendall("Enter your name: ".encode())
        name = conn.recv(1024).decode().strip()
        if not name:
            conn.close()
            return

        # 2) add to list and announce
        with clients_lock:
            clients.append((conn, name))
        broadcast(f"*** {name} has joined the chat ***")

        # 3) receive loop
        while True:
            data = conn.recv(1024)
            if not data:
                break
            text = data.decode().strip()
            if text.lower() == 'exit':
                break
            broadcast(f"{name}: {text}", _sender=conn)

    except Exception as e:
        print(f"Error with {addr}: {e}")
    finally:
        # remove client and announce leave
        with clients_lock:
            clients[:] = [(c,n) for c,n in clients if c is not conn]
        broadcast(f"*** {name} has left the chat ***")
        conn.close()

def main():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen()
    print(f"[+] Group chat server listening on {HOST}:{PORT}")

    try:
        while True:
            conn, addr = srv.accept()
            print(f"[+] Connection from {addr}")
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        print("\n[!] Server shutting down")
    finally:
        srv.close()

if __name__ == '__main__':
    main()
