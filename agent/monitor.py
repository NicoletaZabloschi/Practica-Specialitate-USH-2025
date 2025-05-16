import psutil
import time
from utils.logger import log_alert

CONNECTION_THRESHOLD = 100

def monitor_connections():
    connections = psutil.net_connections()
    active = [c for c in connections if c.status == 'ESTABLISHED']

    if len(active) > CONNECTION_THRESHOLD:
        log_alert(f"Numar mare de conexiuni active detectat: {len(active)}")



def start_monitoring():
    print("[INFO] Agentul de monitorizare ruleaza...")
    try:
        while True:
            monitor_connections()
            time.sleep(5)
    except KeyboardInterrupt:
        print("[INFO] Monitorizare oprita.")
