from utils.logger import log_sensor
import time
import random

def run_sensor(log=None):
    for i in range(5):
        value = round(random.uniform(40.0, 60.0), 2)  # simulare umiditate
        message = f"Umiditate: {value} %"
        log_sensor(message)
        if log:
            log(message)
        time.sleep(1)
