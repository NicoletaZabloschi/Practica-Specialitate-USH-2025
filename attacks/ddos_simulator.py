import socket
import threading
import time
from utils.logger import log_alert

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5000
CONNECTIONS = 30

def attack():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET_IP, TARGET_PORT))
        s.send(b"GET / HTTP/1.1\r\nHost: target\r\n\r\n")
        time.sleep(1)
        s.close()
        log_alert(f"Conexiune trimisă către {TARGET_IP}:{TARGET_PORT}", attack_type="DDoS")
    except Exception as e:
        log_alert(f"Eroare conexiune: {e}", attack_type="DDoS")

def start_ddos():
    print(f"[INFO] Pornire simulare DDoS pe {TARGET_IP}:{TARGET_PORT} cu {CONNECTIONS} conexiuni...")
    threads = []

    for i in range(CONNECTIONS):
        t = threading.Thread(target=attack)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("[INFO] Simulare DDoS finalizata.")
