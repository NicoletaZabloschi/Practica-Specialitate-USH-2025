import os

def ensure_sensor_log_exists():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/sensor.log"):
        with open("data/sensor.log", "w", encoding="utf-8") as f:
            f.write("")