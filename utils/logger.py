import os
import queue

def ensure_sensor_log_exists():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/sensor.log"):
        with open("data/sensor.log", "w", encoding="utf-8") as f:
            f.write("")

def log_alert(message: str, attack_type: str = None):
    try:
        os.makedirs("data", exist_ok=True)
        with open("data/alerts.log", "a", encoding="utf-8") as file:
            if attack_type:
                file.write(f"Tip atac: {attack_type} - {message}\n")
                print(f"[ALERT LOG] Tip atac: {attack_type} - {message}")
            else:
                file.write(message + "\n")
                print(f"[ALERT LOG] {message}")
    except Exception as e:
        print(f"[ERROR] Nu s-a putut scrie in fisier: {e}")

log_queue = None

def set_log_queue(q):
    global log_queue
    log_queue = q

def log_sensor(message: str):
    try:
        with open("data/sensor.log", "a", encoding="utf-8") as file:
            file.write(message + "\n")
        print(f"[SENSOR LOG] {message}")

        if log_queue:
            log_queue.put("[SENSOR] " + message)
    except Exception as e:
        print(f"[ERROR] Nu s-a putut scrie in fisier sensor.log: {e}")