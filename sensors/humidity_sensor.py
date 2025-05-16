# humidity_sensor.py
import socket
import time
import random

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5000

def simulate_humidity():
    return round(random.uniform(40.0, 70.0), 2)

def run_sensor():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        while True:
            humidity = simulate_humidity()
            message = f"HUM:{humidity}%"
            s.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
            print(f"[HUMID SENSOR] Trimis: {message}")
            time.sleep(3)

if __name__ == "__main__":
    run_sensor()
