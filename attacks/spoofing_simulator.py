import socket
from utils.logger import log_alert

def start_spoofing():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        spoofed_ip = "1.2.3.4"
        target_ip = "127.0.0.1"
        target_port = 5000

        s.sendto(b"Test spoofing", (target_ip, target_port))
        log_alert(f"Packet spoofed de la {spoofed_ip} catre {target_ip}:{target_port}", attack_type="Spoofing")
        s.close()
    except Exception as e:
        log_alert(f"Eroare spoofing: {e}", attack_type="Spoofing")
