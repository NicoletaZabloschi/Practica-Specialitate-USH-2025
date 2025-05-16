import socket
import threading
import time

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5000
CONNECTIONS = 5

def attack(log_func, conn_id):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET_IP, TARGET_PORT))
        s.send(b"GET / HTTP/1.1\r\nHost: target\r\n\r\n")
        time.sleep(1)
        s.close()
        log_func(f"[ALERT LOG] Tip atac: DDoS - Conexiune {conn_id} trimisa catre {TARGET_IP}:{TARGET_PORT}")
    except Exception as e:
        log_func(f"[ALERT LOG] Tip atac: DDoS - Eroare conexiune {conn_id}: {e}")

def start_ddos(log_func):
    threads = []
    for i in range(1, CONNECTIONS+1):
        t = threading.Thread(target=attack, args=(log_func, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
