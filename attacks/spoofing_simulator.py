import socket

def start_spoofing(log_func):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        spoofed_ip = "1.2.3.4"
        target_ip = "127.0.0.1"
        target_port = 5000

        s.sendto(b"Test spoofing", (target_ip, target_port))
        log_func(f"[ALERT LOG] Tip atac: Spoofing - Packet spoofed de la {spoofed_ip} catre {target_ip}:{target_port}")
        s.close()
    except Exception as e:
        log_func(f"[ALERT LOG] Tip atac: Spoofing - Eroare spoofing: {e}")
