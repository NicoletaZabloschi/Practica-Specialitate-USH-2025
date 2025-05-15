import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server asculta pe {HOST}:{PORT} ...")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Conexiune de la {addr}")
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(b'HTTP/1.1 200 OK\r\nContent-Length: 2\r\n\r\nOK')
