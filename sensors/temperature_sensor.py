import socket
import time
import random

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000

def simulate_temperature():
    return round(random.uniform(20.0, 30.0), 2)

def run_sensor():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            temp = simulate_temperature()
            message = f"TEMP:{temp}C"
            s.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
            print(f"[TEMP SENSOR] Trimis: {message}")
            time.sleep(2)

if __name__ == "__main__":
    run_sensor()
