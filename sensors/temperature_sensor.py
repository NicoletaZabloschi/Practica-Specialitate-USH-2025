from utils.logger import log_sensor
import time
import random

def run_sensor(log=None):
    for i in range(5):
        value = round(random.uniform(20.0, 30.0), 2)
        message = f"Temperatura: {value} °C"
        log_sensor(message)
        if log:
            log(message)
        time.sleep(1)
