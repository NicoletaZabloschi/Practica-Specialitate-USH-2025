import socket

HOST = "0.0.0.0"
PORT = 5000

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[SERVER] Astept date pe {HOST}:{PORT}...")

        while True:
            data, addr = s.recvfrom(1024)
            print(f"[RECEPTIE] De la {addr}: {data.decode()}")

if __name__ == "__main__":
    run_server()
